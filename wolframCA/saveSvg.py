import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import random
from createRule import createRule


width = 30720
height = 30720

gen1 = np.zeros(width)

gen1[int(width/2)]=1

indexVal = 0
choices = [0,1,2,3,4]
#for i in gen1:
#    gen1[indexVal] = random.choice(choices)
#    indexVal+=1


def getNextGen(currentGenArray, mainDict):
    nextGen = np.zeros(width)
    position = 0
    for i in nextGen:
        if position-1>=0:
            upLeft = int(currentGenArray[position-1])
        else:
            upLeft = 0
        if position-2>=0:
            upLeftLeft = int(currentGenArray[position-2])
        else:
            upLeftLeft = 0
        center = int(currentGenArray[position])
        if position+1<len(currentGenArray):
            upRight = int(currentGenArray[position+1])
        else:
            upRight = 0
        if position+2<len(currentGenArray):
            upRightRight = int(currentGenArray[position+2])
        else:
            upRightRight = 0
        nextGen[position] = mainDict[tuple([upLeft, center, upRight])]
        position +=1

    return nextGen


#rules = createRule([1,0,1,0,0,1,1,0,1,0,1,0,0,1,1,0,1,0,1,0,0,1,1,0,1,0,1,0,0,1,1,0]) #Rule 2,795,939,494
#rules = createRule([0,0,1,1,0,1,1,0,1,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1]) #Rule 916,907,703
#rules = createRule([1,1,1,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0]) #Rule 4,206,900,000
#rules = createRule([0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0]) #Rule 133,823,864
#rules = createRule([1,1,0,1,0,0,0,1,0,1,1,1,0,0,1,0,1,0,0,0,1,0,1,1,0,1,1,0,0,1,1,0]) #Rule 3,513,944,934
#rules = createRule([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]) #Rule 2,863,311,530
#rules = createRule([0,1,1,1,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1])  # Ted Rule



filecount = 0
while True:
    print('Getting rule....')
    rulelist = []
    rulelist.append(random.choice(choices))
    rules, rule = createRule(5, 3, rulelist)
    print('Done....')
    filecount+=1
    mainArray = np.zeros((height,width))
    currentGenArray = np.array(gen1)

    for generation in range(height):
        mainArray[generation] = currentGenArray
        currentGenArray = getNextGen(currentGenArray, rules)
        if generation%500==0:
            print(f'{generation}/{height}')

    plt.axis('off')
    print("Trying imshow...")
    plt.imshow(mainArray, cmap='Spectral', interpolation='none', norm=mpl.colors.Normalize(vmin=0, vmax=4))
    print("Complete. Trying savefig...")
    
    plt.savefig(f'./wolframOut/auto7/samples/5tone{filecount}32k.svg', dpi=3000, bbox_inches="tight")
    with open(f'./wolframOut/auto7/rules/{filecount}32k.txt', 'w') as file:
        file.write(str(rule))
        file.close()
    print("Complete.")

