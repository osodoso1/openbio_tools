from Bio import pairwise2
import argparse
import re
import pandas as pd

from Bio.pairwise2 import format_alignment

parser = argparse.ArgumentParser()
parser.add_argument('--strain')
args = parser.parse_args()

target_strain = int(args.strain)
sequences = {}
others = []
strains_seen = [target_strain]
best_match = [('test', 0), ('test', 0), ('test', 0)]
wgs_list = []

print('downloading 16s')
all_16s = pd.DataFrame(database.sequences())

strain_16s_list = all_16s.loc[(all_16s['sequenceable_id'] == target_strain) &
                              (all_16s['name'].str.startswith('16')) &
                              (all_16s['source'] == 'sanger')]
print('sorting 16s')
strain_16s_list.sort_values(by=['id'], ascending=True, inplace=True)

target_16s = strain_16s_list.tail(1)  # most recent 16s sequence
target_16s_str = (target_16s.loc[target_16s['sequenceable_id'] ==
                                 target_strain]['body']).values[0].replace('\n', '').replace('\r', '')
for strain in database.strains():  # make a list of strains with official WGS sequences
    if strain['official_assembly_id'] is not None:
        wgs_list.append(str(strain['master_strain_name']))
print('filtering 16s to only sanger')
all_16s = all_16s.loc[(all_16s['sequenceable_id'] != strain) &
                      (all_16s['name'].str.startswith('16')) &
                      (all_16s['source'] == 'sanger')]
# drop our strain from the all_16s table

all_16s.sort_values(by=['created_at'], ascending=False, inplace=True)

for index, row in all_16s.iterrows():

    strain_id = row['sequenceable_id']  # CI number of the strain
    try:  # needs to be a number
        val = int(strain_id)
    except ValueError:
        continue
    sequence = row['body'].replace(
        '\n', '').replace(
        '\r', '')  # format 16S to one line long
    if strain_id not in strains_seen and str(int(strain_id)) in wgs_list:
        others.append([strain_id, sequence])
        strains_seen.append(strain_id)


print('running alignment')
for strain in others:

    alignments = pairwise2.align.globalxx(target_16s_str, str(strain[1]))
    if len(alignments) <= 0:
        continue

    alignment_score = alignments[0][2]
    alignment_length = alignments[0][4]
    pctid = round(100 * (alignment_score / alignment_length), 2)
    # print(best_match, count)
    for x in range(0, len(best_match)):
        if best_match[x][1] < pctid and (
                int(strain[0]), pctid) not in best_match and alignment_score > 750:
            best_match.insert(x, (int(strain[0]), pctid))
            best_match.pop()  # remove the last item
            break
strain_list = [str(target_strain)]

count = 0
for x in best_match:
    strain_list.append(str(x[0]))
print('downloading closest relatives')
for strain in database.get('/strains', params={'q[genotype_eq]': 'wildtype'}):
    if strain['official_assembly_id'] is not None \
            and strain['master_strain_name'] in strain_list:
        official_assembly = strain['official_assembly_id']
        name = strain['master_strain_name']
        assembly = database.assemblies(id=official_assembly)

        if strain['master_strain_name'] == str(
                target_strain):  # first strain in list
            database.download(
                assembly['download_url'],
                out_path='target-strain-{}-assembly.gbk'.format(strain['master_strain_name']))
        else:
            database.download(
                assembly['download_url'],
                out_path='strain-{}-assembly.gbk'.format(strain['master_strain_name']))

        count += 1
print('found %s strains' % count)

if count < 2:
    raise Exception(
        'only found target strain in db for 16s progressiveMauve will fail')
