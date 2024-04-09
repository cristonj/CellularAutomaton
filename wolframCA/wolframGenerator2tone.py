import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import random


width = 500
height = 500

gen1 = np.zeros(width)
indexVal = 0
choices = [0,1,2]
for i in gen1:
    gen1[indexVal] = random.choice(choices)
    indexVal+=1

def createRule(ruleList):
    ruleDict = { 
        tuple([0,0,0]):ruleList[0],
        tuple([0,0,1]):ruleList[1],
        tuple([0,0,2]):ruleList[2],
        tuple([0,1,0]):ruleList[3],
        tuple([0,1,1]):ruleList[4],
        tuple([0,1,2]):ruleList[5],
        tuple([0,2,0]):ruleList[6],
        tuple([0,2,1]):ruleList[7],
        tuple([0,2,2]):ruleList[8],
        tuple([1,0,0]):ruleList[9],
        tuple([1,0,1]):ruleList[10],
        tuple([1,0,2]):ruleList[11],
        tuple([1,1,0]):ruleList[12],
        tuple([1,1,1]):ruleList[13],
        tuple([1,1,2]):ruleList[14],
        tuple([1,2,0]):ruleList[15],
        tuple([1,2,1]):ruleList[16],
        tuple([1,2,2]):ruleList[17],
        tuple([2,0,0]):ruleList[18],
        tuple([2,0,1]):ruleList[19],
        tuple([2,0,2]):ruleList[20],
        tuple([2,1,0]):ruleList[21],
        tuple([2,1,1]):ruleList[22],
        tuple([2,1,2]):ruleList[23],
        tuple([2,2,0]):ruleList[24],
        tuple([2,2,1]):ruleList[25],
        tuple([2,2,2]):ruleList[26],
    }
    return ruleDict


def getNextGen(currentGenArray, mainDict):
    nextGen = np.zeros(width)
    position = 0
    for i in nextGen:
        if position-1>=0:
            upLeft = currentGenArray[position-1]
        else:
            upLeft = 0
        center = currentGenArray[position]
        if position+1<len(currentGenArray):
            upRight = currentGenArray[position+1]
        else:
            upRight = 0
        nextGen[position] = mainDict[tuple([upLeft, center, upRight])]
        position +=1
    return nextGen



def randomrule(size,states):
    rule = []
    for i in range(size):
        rule.append(random.choice(states))
    return rule

#mainDict = createRule([0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2])

#mainDict = createRule([2,0,2,1,2,1,2,0,0,2,2,1,0,1,2,2,0,0,2,2,2,1,1,1,1,1,2])

rule = randomrule(27,[0,1,2])
#rule = [1, 0, 2, 0, 1, 2, 1, 2, 1, 2, 1, 0, 2, 1, 0, 2, 2, 1, 0, 2, 2, 0, 2, 2, 1, 2, 1]
#rule = [1, 2, 1, 0, 1, 0, 0, 2, 1, 1, 2, 2, 0, 0, 0, 2, 1, 2, 1, 1, 2, 1, 1, 1, 0, 0, 2] #Interesting pattern
print(rule)
mainDict = createRule(rule) #Use a random rule



mainArray = np.zeros((height,width))

currentGenArray = np.array(gen1)

for generation in range(height):
    mainArray[generation] = currentGenArray
    currentGenArray = getNextGen(currentGenArray, mainDict)
    if generation%500==0:
        print(f'{generation}/{height}')


print("Trying imshow...")
plt.imshow(mainArray, cmap='hot', interpolation='none', norm=mpl.colors.Normalize(vmin=0, vmax=2))
print("Complete. Trying savefig...")
plt.savefig('./wolframOut/2toneTest16.png', dpi=1000, bbox_inches="tight")
print("Complete.")