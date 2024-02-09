#!/usr/bin/env python

#doesnt work yet!#

import numpy as np

def pop(n, m):
    # make an array that reflects the number of months lived on one axis and the generation on the other axis.
    population = np.zeros((n,m))
    # initialize with 1 pair 
    population[0][0] = 1
    # for every month we are interested in
    for i in range(1,n):
        # newborns = sum of the adults from the previous generation - newborns from the previous generation
        population[i][0] = population[i-1].sum() - population[i-1][0]
        # update the values of the next row in the array of adults shifting 1 year over as they age 
        for b in range(1,m):
            population[i][b] = population[i-1][b-1]

    #return the sum of the population at month n (n-1 because python is 0-based)
    total_pop = int(population[n-1].sum())
    return total_pop, population

total_pop, population = pop(6,3)
print(population)
print(total_pop)