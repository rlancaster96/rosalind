#!/usr/bin/env python

from Bio import Entrez

filename = "rosalind_gbk.txt"

with open(filename, "r") as fh:
    genus = fh.readline().strip()
    start = fh.readline().strip()
    end = fh.readline().strip()

searchstring = f'("{genus}"[Organism]) AND ("{start}"[Publication Date] : "{end}"[Publication Date])'

Entrez.email = "rubenl@uoregon.edu"
handle = Entrez.esearch(db="nucleotide", term=searchstring)
record = Entrez.read(handle)
counts = record["Count"]
print(counts)

