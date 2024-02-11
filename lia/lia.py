#!/usr/bin/env python

# Fixed outcome of either yes AaBb or not AaBb. Use binomial distribution
# The probability of offspring being AaBb given the mate is always AaBb is 0.25 for every generation.

from scipy.stats import binom 

def lia(k,N):
    # the population grows at a rate of 2 offspring per parent per generation
    population = 2**k 

    # Set up probability mass function using binom.pmf
    n = population
    p = 0.25
    r = N

    # list of r values, +1 for python 0-based to include 0th and nth in list
    r_values = list(range(n + 1)) 
    dist = []

    # list of pmf values 
    for r in r_values:
        val = binom.pmf(r, n, p)
        dist.append(val)
    
    # we want N or greater, so sum up probability of all successes 
    totalprob = sum(dist[N:])
    return totalprob

print(lia(5,7))