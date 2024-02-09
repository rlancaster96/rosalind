#!/usr/bin/env python

from Bio.Seq import Seq

# create a sequence object
my_seq = Seq("CGTACGGTCTTACCTGGGCAACTCAAGGGGCCATACGCATCTGTCTACAGGAAGACACGTAGTCGCTTTATTGGTTTTATGCTCTTCCATACGATCATACGTCTGCGATCCCAGCCCCAGGTCCCTCATTCGATTGGGGGGGACAGCAACCCCTGTGTAGACAAGCACTAAGCATACACGAGTCTTGGGTTCCTGCGAGATCACTACGACTTTTTTCGTTGACCGCGACTATCCCTTATATGAACGAGATACGAACCGTATTGCAACGCTTGCGACTGTCAATGGATTTAGGACGCTGGTCGCGCTACGATGGATCGGATGTCCACGGGTCACCTCATGGTATCGCTCGACTGCAATCCAAGAGACTGCTATCCCCACACCATATGGTACTTCTTGGCAGCATGAAGTTCTGGGGACTAATGATGACTTGCATGATTACAAGTGAATCCGCATTAACATTGCCCTCTCTCTCACCGGTTGTTGGAGTCCCGGTAGCGTGTTACTCGGGTTCGAATAATGCCAGGTGCACCACGAAGTGATGTACCAAGTGAGCCGATCGGCGCACGCGTCGCTACGTAGTAGACCACCCTCAAGGCGCACCTGGCGCAATTAATAGCGCTAGGGATACCCGAATATGCATCCGTGGATCCTTGTGAGCCGTTCACAACTTTACGCCTAGCGAAAGCCGCTTCCGACTACCTCTCATAACTGCGGTCTTATCCTACGTCGAGATACCGGAACCATGAAGATAGCTGCTATGTGATGACCGGTGTCAGCAAGTGCCTGCTCTGCAACGGGGGCGACCATTCAATACGGTAATAACTCGTAAT")

# print out some details about it
counts = []
nucleotides = ["A", "C", "G", "T"]
for nucleotide in nucleotides:
    count = my_seq.count(nucleotide)
    counts.append(count)

print(*counts, sep = " ")