#!/usr/bin/env python3
import argparse

from magnumopus import ispcr, needleman_wunsch

def reverse_complement(sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement_dict[base] for base in sequence[::-1])

def process_sequence(sequence):
    # Remove header line starting with '>'
    lines = sequence.split('\n')
    if lines and lines[0].startswith('>'):
        lines.pop(0)
    # Remove newline characters and combine lines
    processed_sequence = '\n'.join(lines).strip()
    return processed_sequence


def main():
    parser = argparse.ArgumentParser(description="Perform in-silico PCR and align amplicons from two assemblies.")
    
    parser.add_argument("-1", "--assembly1", required=True, help="Path to the first assembly file")
    parser.add_argument("-2", "--assembly2", required=True, help="Path to the second assembly file")
    parser.add_argument("-p", "--primers", required=True, help="Path to the primer file")
    parser.add_argument("-m", "--max_amplicon_size", type=int, required=True, help="Maximum amplicon size for isPCR")
    parser.add_argument("--match", type=int, required=True, help="Match score to use in alignment")
    parser.add_argument("--mismatch", type=int, required=True, help="Mismatch penalty to use in alignment")
    parser.add_argument("--gap", type=int, required=True, help="Gap penalty to use in alignment")
    
    args = parser.parse_args()

    # Perform isPCR on both assembly files with the provided primer file
    p_amplicon1 = ispcr(args.primers, args.assembly1, args.max_amplicon_size)
    p_amplicon2 = ispcr(args.primers, args.assembly2, args.max_amplicon_size)
    #print (p_amplicon1)
    # Process the sequences
    amplicon1 = process_sequence(p_amplicon1)
    amplicon2 = process_sequence(p_amplicon2)
    #print(amplicon1)

    # Check which orientation aligns best and get the best alignment
    best_alignment = None
    reverse_amplicon1 = reverse_complement(amplicon1)
    reverse_amplicon2 = reverse_complement(amplicon2)

    # Calculate the score
    alignment_results = []
    alignment1, score1 = needleman_wunsch(amplicon1, amplicon2, args.match, args.mismatch, args.gap)
    alignment_results.append((alignment1, score1))

    alignment2, score2 = needleman_wunsch(amplicon1, reverse_amplicon2, args.match, args.mismatch, args.gap)
    alignment_results.append((alignment2, score2))

    alignment3, score3 = needleman_wunsch(reverse_amplicon1, amplicon2, args.match, args.mismatch, args.gap)
    alignment_results.append((alignment3, score3))

    alignment4, score4 = needleman_wunsch(reverse_amplicon1, reverse_amplicon2, args.match, args.mismatch, args.gap)
    alignment_results.append((alignment4, score4))

    best_alignment = alignment_results[0][0]  # Default to the first alignment result
    best_score = alignment_results[0][1]

    for alignment, score in alignment_results[1:]:
        if score > best_score:
           best_alignment = alignment
           best_score = score
           print(best_alignment[0])
           print(best_score)
           #print(type(best_alignment))



if __name__ == "__main__":
    main()
