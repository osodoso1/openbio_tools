def filter_contigs(input_file, output_file, min_length, max_length):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        contig_name = ''
        contig_sequence = ''

        for line in infile:
            if line.startswith('>'):
                if contig_name and len(contig_sequence) >= min_length and len(contig_sequence) <= max_length:
                    outfile.write(contig_name + '\n')
                    outfile.write(contig_sequence + '\n')
                contig_name = line.strip()
                contig_sequence = ''
            else:
                contig_sequence += line.strip()

        if contig_name and len(contig_sequence) >= min_length and len(contig_sequence) <= max_length:
            outfile.write(contig_name + '\n')
            outfile.write(contig_sequence + '\n')

# Replace these values with your input file, output file, min length, and max length
input_file = ''
output_file = 'filtered_contigs.fasta'
min_length = 300
max_length = 500

filter_contigs(input_file, output_file, min_length, max_length)