🧬 openbio_tools
Engineered for executing specific workflows in molecular biology and PCR.

This repository is under active development to transform manual, repetitive data curation tasks into a suite of highly-optimized automation targets.

🗺️ System Workflow Architecture
This Mermaid diagram maps out the inputs, core processes, and exact execution paths for each tool in the toolkit:

Code snippet
graph TD
    %% Style Definitions
    classDef target fill:#1e1e2e,stroke:#3b82f6,stroke-width:2px,color:#cdd6f4;
    classDef input fill:#11111b,stroke:#a6adc8,stroke-dasharray: 4 4,color:#bac2de;
    classDef output fill:#111b16,stroke:#a6e3a1,stroke-width:2px,color:#a6e3a1;

    %% Tool 1: gDNA to qPCR
    I1[💾 Raw Genomic DNA Metadata] --> T1("🎯 Target 1: gDNA to qPCR to Asana")
    T1 --> |"Extracts columns & reformats"| P1["🧬 qPCR Sample Layouts"]
    P1 --> |"Automated API push"| O1["📝 Task Created in Asana Teams"]

    %% Tool 2: Plate Map Generator
    I2["🧫 Strain ID & Sample Count (N)"] --> T2("🎯 Target 2: plate_map_generator")
    T2 --> |"Calculates spatial coordinates"| O2["🧫 10x5 Array or 3x5 Assay Plate Maps"]

    %% Tool 3: 16s Closest Relatives
    I3["🧬 Raw 16S rRNA Sequence"] --> T3("🎯 Target 3: 16s_closest_relatives")
    T3 --> |"Queries phylogenetic DB"| O3["🌳 Closest Taxonomic Relatives Matched"]

    %% Tool 4: Filter Contigs
    I4["💻 Raw Assembly Contigs (FASTA)"] --> T4("🎯 Target 4: filtercontigs")
    T4 --> |"Evaluates length thresholds"| O4["🔬 Verified Contigs (Desired Length)"]

    %% Apply Classes
    class T1,T2,T3,T4 target;
    class I1,I2,I3,I4 input;
    class O1,O2,O3,O4 output;
🎯 Individual Tool Workflows
🧪 Target 1: gDNA to qPCR request to asana
Input: gDNA extraction data and operational hand-off metrics.

The Workflow:

Parses raw laboratory data hand-off sheets between dry and wet lab teams.

Isolates and maps specific metadata columns required to convert genomic DNA to quantitative PCR samples.

Integrates with the Asana API to instantly populate cross-team tracking tasks for downstream validation.

Output: 🚀 Fully formatted Asana tasks ready for wet-lab execution tracking.

🧫 Target 2: plate_map_generator
Input: Strain identifier details multiplied by total sample count.

The Workflow:

Accepts dynamic, user-defined dimensions for high-throughput screening assays.

Map layout algorithms process your variables (Strain * Number of Samples).

Automatically maps indexes onto physical grid representations, preventing manual Excel configuration mistakes.

Output: 📋 Structured plate arrays formatted perfectly into 10x5 or 3x5 maps.

🌳 Target 3: 16s_closest_relatives
Input: Standardized FASTA format or raw sequence strings of 16S rRNA genes.

The Workflow:

Normalizes the target sequence query data.

Automatically searches taxonomic and local sequence databases.

Returns high-confidence, closest genetic matches to establish lineage and source classification.

Output: 🔍 Top-tier taxonomic relatives ranking table.

✂️ Target 4: filtercontigs
Input: Raw genome assembly files.

The Workflow:

Scans across raw genomic contigs dynamically.

Compares sequence parameters against your strict minimum and maximum baseline thresholds.

Strips away background noise, fragment artifacts, and low-quality data.

Output: 🧬 A curated file containing only verified contigs matching your exact length requirements.

🔓 Open-Source: All scripts are designed to be run as modular components. Clone the repo, specify your targets, and start automating your pipeline!
