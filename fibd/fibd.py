#!/usr/bin/env python

# Not finished yet #

def rabbits(n, k):
    months = n-1
    litsize = k
    newborn = 1
    Ojuvenile = 0
    Njuvenile = 0
    adult = 0
    
    population = 0 
    
    while months > 0:
        
        Njuvenile = newborn
        adult = adult + Ojuvenile
        newborn = adult*litsize
        Ojuvenile = Njuvenile
        population = adult + newborn + Ojuvenile
        months -= 1
    return population   
                
pop = rabbits(33,5)
print(pop)