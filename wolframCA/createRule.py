import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import random


def numberToBase(n, b): #Function I stole from google
    if n == 0:
        return list([0])
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return list(digits[::-1])


#Function to return a rules dictionary relating the list of neighbor values to an int new cell value. Parameters(int: number of different cell values/colors, int: number of cells each cell reads (neighbors), Optional rule (must be of len=states**cells)
def createRule(states, cells, rule=[]): 
    #Creating variables
    ruleDict = {}
    numPatterns = states**cells
    statelist = []


    #List of all possible states
    for state in range(states):
        statelist.append(state)


    patternList = []


    #Loop through numPatterns (Big loop)
    for i in range(numPatterns):

        #Fixing weird formatting from the numberToBase function which was causing errors
        patternTemp = list(numberToBase(i,states))
        pattern = []
        for j in patternTemp:
            pattern.append(j)

        #this is for the first few values returned from the numberToBase function are too short, and zeros need to be added to keep the format.
        while len(pattern)<cells:
            patternTemp = list(pattern)
            pattern = []
            pattern.append(0)
            for h in patternTemp:
                pattern.append(h)

        
        patternList.append(pattern)

        #this is for if the rule you gave is too short or was left empty. If it errors it appends a random state.
        try:
            tempVal = rule[i]
        except:
            rule.append(random.choice(statelist))

        #append the pattern at index i with the rule at index i to the ruleDict 
        ruleDict[tuple(patternList[i])] = rule[i]
    
    return ruleDict, rule







ruleDict, rule = createRule(5,8)#Could be used for creating a random rule which takes in an array of 8 neighbors each belonging to 5 possible states, and outputs an int next value of 5 possible states


print(ruleDict)