#!/usr/bin/env python

import pandas as pd

#convert to one line fasta 
def oneline_fasta(readfile, writefile):
    '''Converts a fasta file with multiple sequence lines per record to one sequence line per record.'''
    with open(readfile, "r") as readfh, open(writefile, "w") as writefh:
        seq = ""
        while True:
            line = readfh.readline().strip()
            if not line:
                break
            if line.startswith(">"):
                if seq != "":
                    writefh.write(f"{seq}\n")
                seq = ""
                writefh.write(f"{line}\n")
            else:
                seq += line
        writefh.write(seq)
        return
    
oneline_fasta("rosalind_cons_2.txt", "rosalind_cons_2_edited.txt")

with open("rosalind_cons_2_edited.txt", "r") as fh:
    fh.readline()
    line = fh.readline()
    line = line.strip()
    n = len(line)

# make empty lists of length of the read
A = [0] * n
C = [0] * n
G = [0] * n
T = [0] * n

#make seqlist 
with open("rosalind_cons_2_edited.txt", "r") as fh:
    seqlist = []

    for line in fh:
        if line.startswith(">"):
            continue
        else:
            seq = line.strip()
            for i,a in enumerate(seq):
                if a == "A":
                    A[i] += 1
                elif a == "T":
                    T[i] += 1
                elif a == "C":
                    C[i] += 1
                elif a == "G":
                    G[i] += 1

nucA = A.copy()
nucC = C.copy()
nucT = T.copy()
nucG = G.copy()

cons = []
nuc = []
for (A, C, T, G) in zip(A, C, T, G):
    cons.append(A)
    cons.append(C)
    cons.append(T)
    cons.append(G)
    maxpos = pd.Series(cons).idxmax()
    nuc.append(maxpos)
    cons = []

consensus = []
for a in nuc:
    if a == 0:
        consensus.append("A")
    elif a == 1:
        consensus.append("C")
    elif a == 2:
        consensus.append("T")
    elif a == 3: 
        consensus.append("G")

with open("consoutput.txt", "w") as wh:
    for a in consensus:
        wh.write(a)
    wh.write("\n")
    wh.write("A:")
    for a in nucA:
        wh.write(" ")
        wh.write(str(a))
    wh.write("\n")
    wh.write("C:")
    for a in nucC:
        wh.write(" ")
        wh.write(str(a))
    wh.write("\n")
    wh.write("G:")
    for a in nucG:
        wh.write(" ")
        wh.write(str(a))
    wh.write("\n")
    wh.write("T:")
    for a in nucT:
        wh.write(" ")
        wh.write(str(a))
    