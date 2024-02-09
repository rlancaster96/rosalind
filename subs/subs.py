#!/usr/bin/env python

with open("rosalind_subs.txt", "r") as fh:
    big = fh.readline()
    big = big.strip()
    small = fh.readline()
    small = small.strip()

    outlist = []

    length = len(small)

    for i,a in enumerate(big):
        snippet = big[i:i+length]
        
        if len(snippet) != length:
            break
        if snippet == small:
            outlist.append(i+1)

print(*outlist)