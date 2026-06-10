openbio_tools
Engineered for executing specific workflows in molecular biology and PCR.

This repository is under active development to transform manual, repetitive data curation tasks into a suite of automation targets. Each script serves as a dedicated tool designed to bridge the gap between dry-lab data processing and wet-lab execution.

🎯 Automation Targets
Target: gDNA to qPCR request to asana

Objective: Streamline laboratory data hand-offs between teams.

Execution: Parses genomic DNA metadata, formats the specific columns required for quantitative PCR conversion, and automatically generates structured downstream testing requests directly in Asana.

Target: plate_map_generator

Objective: Automate wet-lab assay layouts.

Execution: Eliminates manual grid creation by taking your exact strain and sample counts and instantly generating clean, structured plate maps in standard 10x5 and 3x5 formats.

Target: 16s_closest_relatives

Objective: Rapid phylogenetic screening.

Execution: Directly queries sequence databases using a strain's 16S rRNA sequence to isolate and identify its closest taxonomic relatives.

Target: filtercontigs

Objective: Precision assembly quality control.

Execution: A dedicated filtering script that processes raw assembly data, stripping away noise to isolate only the contigs that meet your specific length requirements.

🔓 Open-Source: All tools in this repository are free to use, modify, and integrate into your local pipelines.

How it works: A dynamic filtering script that slices through assembly data, isolating and extracting contigs that meet your strict, user-defined length thresholds.

graph TD
    %% Style Definitions
    classDef target fill:#1f2937,stroke:#3b82f6,stroke-width:2px,color:#fff;
    classDef input fill:#111827,stroke:#6b7280,stroke-dasharray: 5 5,color:#9ca3af;
    classDef output fill:#064e3b,stroke:#10b981,stroke-width:2px,color:#a7f3d0;

    %% Nodes
    Input[Raw Biological Data & Metadata] --> |Select Target| Targets

    subgraph Targets [Isolated Python Targets]
        T1(gDNA to qPCR -> Asana)
        T2(plate_map_generator)
        T3(16s_closest_relatives)
        T4(filtercontigs)
    end

    %% Workflows
    T1 --> O1[Asana Tasks & Downstream qPCR Tracking]
    T2 --> O2[Assay Layouts: 10x5 & 3x5 Arrays]
    T3 --> O3[Database Match: Phylogenetic Relatives]
    T4 --> O4[Filtered Assembly: Verified Contigs]

    %% Apply Styles
    class T1,T2,T3,T4 target;
    class Input input;
    class O1,O2,O3,O4 output;
