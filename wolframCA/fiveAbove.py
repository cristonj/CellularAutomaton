import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import random
from createRule import createRule


width = 5000
height = 5000




gen1 = np.zeros(width)
indexVal = 0
choices = [0,1]
for i in gen1:
    gen1[indexVal] = random.choice(choices)
    indexVal+=1

def createRule(ruleList):
    ruleDict = { 
        tuple([0,0,0,0,0]):ruleList[0],
        tuple([0,1,0,0,0]):ruleList[1],
        tuple([0,0,1,0,0]):ruleList[2],
        tuple([0,1,1,0,0]):ruleList[3],
        tuple([0,0,0,1,0]):ruleList[4],
        tuple([0,1,0,1,0]):ruleList[5],
        tuple([0,0,1,1,0]):ruleList[6],
        tuple([0,1,1,1,0]):ruleList[7],
        tuple([1,0,0,0,0]):ruleList[8],
        tuple([1,1,0,0,0]):ruleList[9],
        tuple([1,0,1,0,0]):ruleList[10],
        tuple([1,1,1,0,0]):ruleList[11],
        tuple([1,0,0,1,0]):ruleList[12],
        tuple([1,1,0,1,0]):ruleList[13],
        tuple([1,0,1,1,0]):ruleList[14],
        tuple([1,1,1,1,0]):ruleList[15],
        tuple([0,0,0,0,1]):ruleList[16],
        tuple([0,1,0,0,1]):ruleList[17],
        tuple([0,0,1,0,1]):ruleList[18],
        tuple([0,1,1,0,1]):ruleList[19],
        tuple([0,0,0,1,1]):ruleList[20],
        tuple([0,1,0,1,1]):ruleList[21],
        tuple([0,0,1,1,1]):ruleList[22],
        tuple([0,1,1,1,1]):ruleList[23],
        tuple([1,0,0,0,1]):ruleList[24],
        tuple([1,1,0,0,1]):ruleList[25],
        tuple([1,0,1,0,1]):ruleList[26],
        tuple([1,1,1,0,1]):ruleList[27],
        tuple([1,0,0,1,1]):ruleList[28],
        tuple([1,1,0,1,1]):ruleList[29],
        tuple([1,0,1,1,1]):ruleList[30],
        tuple([1,1,1,1,1]):ruleList[31]
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
        if position-2>=0:
            upLeftLeft = currentGenArray[position-2]
        else:
            upLeftLeft = 0
        center = currentGenArray[position]
        if position+1<len(currentGenArray):
            upRight = currentGenArray[position+1]
        else:
            upRight = 0
        if position+2<len(currentGenArray):
            upRightRight = currentGenArray[position+2]
        else:
            upRightRight = 0
        nextGen[position] = mainDict[tuple([upLeftLeft, upLeft, center, upRight, upRightRight])]
        position +=1

    return nextGen


#rules = createRule([1,0,1,0,0,1,1,0,1,0,1,0,0,1,1,0,1,0,1,0,0,1,1,0,1,0,1,0,0,1,1,0]) #Rule 2,795,939,494
#rules = createRule([0,0,1,1,0,1,1,0,1,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1]) #Rule 916,907,703
#rules = createRule([1,1,1,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0]) #Rule 4,206,900,000
#rules = createRule([0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0]) #Rule 133,823,864
#rules = createRule([1,1,0,1,0,0,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1,0,1,1,0,1,1,0,0,1,1,0]) #Rule 3,513,944,934
#rules = createRule([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]) #Rule 2,863,311,530
#rules = createRule([0,1,1,1,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1])  # Ted Rule
rules = createRule([0,1,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,1])





mainArray = np.zeros((height,width))
currentGenArray = np.array(gen1)

for generation in range(height):
    mainArray[generation] = currentGenArray
    currentGenArray = getNextGen(currentGenArray, rules)
    if generation%500==0:
        print(f'{generation}/{height}')


print("Trying imshow...")
plt.imshow(mainArray, cmap='hot', interpolation='none', norm=mpl.colors.Normalize(vmin=0, vmax=1))
print("Complete. Trying savefig...")
plt.savefig('./wolframOut/ted25bit.png', dpi=3000, bbox_inches="tight")
print("Complete.")
