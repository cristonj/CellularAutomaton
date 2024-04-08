import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import random


width = 15360
height = 15360

gen1 = np.zeros(width)
indexVal = 0
choices = [0,1]
for i in gen1:
    gen1[indexVal] = random.choice(choices)
    indexVal+=1

def createRule(ruleList):
    ruleDict = { 
        tuple([1,1,1]):ruleList[0],
        tuple([1,1,0]):ruleList[1],
        tuple([1,0,1]):ruleList[2],
        tuple([1,0,0]):ruleList[3],
        tuple([0,1,1]):ruleList[4],
        tuple([0,1,0]):ruleList[5],
        tuple([0,0,1]):ruleList[6],
        tuple([0,0,0]):ruleList[7]
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


#mainDict = createRule([0,0,0,1,1,1,1,0]) #Rule 30
#mainDict = createRule([0,1,0,1,1,0,1,0]) #Rule 90
#mainDict = createRule([0,1,0,0,1,0,0,1]) #Rule 73
#mainDict = createRule([0,0,1,0,1,1,0,1]) #Rule 45
mainDict = createRule([1,0,1,0,0,1,1,0]) #Rule 166


mainArray = np.zeros((height,width))

currentGenArray = np.array(gen1)

for generation in range(height):
    mainArray[generation] = currentGenArray
    currentGenArray = getNextGen(currentGenArray, mainDict)
    if generation%500==0:
        print(f'{generation}/{height}')


print("Trying imshow...")
plt.imshow(mainArray, cmap='hot', interpolation='none', norm=mpl.colors.Normalize(vmin=0, vmax=1))
print("Complete. Trying savefig...")
plt.savefig('./wolframOut/16khighDPIrandomInitRule166.png', dpi=5000, bbox_inches="tight")
print("Complete.")