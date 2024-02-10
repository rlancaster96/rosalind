#!/usr/bin/env python

from bioinfo import oneline_fasta

#convert sequence to just one line, if it happens to be on multiple lines and have line breaks
oneline_fasta("rosalind_grph.txt", "onelinegrph.txt")

def makedict(filename:str) -> dict:
    '''Takes a FASTA file and makes a dictionary in format {sequence : read ID}.'''
    readsdict = {}
    with open(filename) as fh:
        for line in fh:
            #remove newline character
            line = line.strip()
            #isolate the read names
            if line.startswith(">"):
                readname = line[1:]
            # append read name and read sequence to dictionary in format {seq : readname}
            else:
                readsdict[line] = readname
    return readsdict

def makeset(filename:str) -> set:
    '''Takes a FASTA file and makes a set of sequences in format (seq1, seq2, etc.)'''
    readsset = set()
    with open(filename) as fh:
        for line in fh:
            line = line.strip()
            if line.startswith(">"):
                continue
            else:
                readsset.add(line)
    return readsset

def edges(readsset, readsdict):
    '''Takes a set of sequences and a dictionary of sequence & seq ID and returns suffix/prefix matches with overlap of 3.'''
    for a in readsdict:
        # grab the last 3 nucleotides of the first sequence
        suffix = a[-3:]
        for b in readsset:
            # grab the first 3 nucleotides of the sequence
            prefix = b[:3]
            # if the suffix and prefix match AND the sequence isnt the same.
            if suffix == prefix and a != b:
                match = str(readsdict[a] + " " + readsdict[b])
                print(match)
    return

readsset = makeset("onelinegrph.txt")
readsdict = makedict("onelinegrph.txt")
edges(readsset, readsdict)