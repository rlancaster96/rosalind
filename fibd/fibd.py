#!/usr/bin/env python

def pop(n,m):
    '''Input months (n) and lifespan in months (m) of rabbits. Returns total population at a certain month. Assume 1 pair of adults has 1 pair of offspring.'''
    
    # initialize first list with 1 pair, with a length of the lifespan of the rabbits
    oldlist = [0] * m
    oldlist[0] = 1
    # initialize empty new list 
    newlist = [0] * m

    # for each month excluding month 0
    for i in range(1,n):
        # make a new list to represent the population, with positions in the list corresponding to age.
        newlist[0] = sum(oldlist[1:])
        # for every position in the new list, update it with the previous position -1. This is the rabbits "aging".
        for b in range(1,m):
            newlist[b] = oldlist[b-1]
        # update lists
        oldlist = newlist
        newlist = [0] * m
    
    # return the sum of the final list, which is the total population.
    population = sum(oldlist)
    return oldlist, population

oldlist, population = pop(90,20)
print(population)


# old strategy works for smaller numbers but breaks for large ones due to overflow scalar subtract error #

# import numpy as np

# def pop(n, m):
#     # make an array that reflects the number of months lived on one axis and the generation on the other axis.
#     population = np.zeros((n,m), dtype=np.int64)
#     # initialize with 1 pair 
#     population[0][0] = 1
#     # for every month we are interested in
#     for i in range(1,n):
#         # newborns = sum of the adults from the previous generation - newborns from the previous generation
#         population[i][0] = population[i-1].sum() - population[i-1][0]
#         # update the values of the next row in the array of adults shifting 1 year over as they age 
#         for b in range(1,m):
#             population[i][b] = population[i-1][b-1]

#     #return the sum of the population at month n (n-1 because python is 0-based)
#     total_pop = population[n-1].sum()
#     return total_pop, population

# total_pop, population = pop(95,19)
# print(population)
# print(total_pop)