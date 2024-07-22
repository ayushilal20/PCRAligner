# PCRAligner

In this project, I developed a comprehensive bioinformatics package named "Magnum Opus" as part of the Programming for Bioinformatics course (BIOL 7200). The package integrates multiple bioinformatics tools and algorithms to facilitate in-silico PCR and sequence alignment tasks. The project involved the following key components:

    isPCR Module:
        Developed a Python module to simulate in-silico PCR (isPCR).
        The module takes primer and assembly files as input and returns predicted amplicons.
        Unified the different steps of the isPCR process into a single callable function.

    Needleman-Wunsch Algorithm Implementation:
        Implemented the Needleman-Wunsch algorithm for global sequence alignment.
        The function aligns two sequences and returns both the aligned sequences and the alignment score.

    Amplicon Alignment Script:
        Created a script that combines the functionalities of the isPCR and Needleman-Wunsch modules.
        The script performs isPCR on two provided assembly files and aligns the resulting amplicons.
        Included a command-line interface to specify input files, maximum amplicon size, and alignment parameters.
