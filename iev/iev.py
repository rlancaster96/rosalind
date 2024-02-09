#!/usr/bin/env python

def prob(inputstr:str) -> float:
    # convert str to list
    input = inputstr.split()
    # convert to int from str
    alleles = [eval(i) for i in input]

    #define probabilities for each position (AA-AA = 100, Aa Aa = 75, etc.)
    probabilities = [100, 100, 100, 75, 50, 0]
    #initialize empty list to hold predicted offspring with dominant phenotype
    offspring = []

    # for every pair in our list of 6 positions
    for i, pair in enumerate(alleles):
        # grab the corresponding probability
        probability = probabilities[i]
        # calculate the predicted number of offspring to have the dominant phenotype
        pair_prob = pair*2*probability
        offspring.append(pair_prob)
    
    #sum up all predicted offspring and divide by 100 to account for percentage
    total = sum(offspring)/100

    return total

print(prob("17349 18492 16336 18418 18594 18469"))


