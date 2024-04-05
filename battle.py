import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import time
from mayavi import mlab
import random


size = 5
generations = 500
arrayValues = np.zeros((size, size), dtype=int)


#Flying Machine
#arrayValues[1+int(size/4)][4+int(size/4)]=1
#arrayValues[2+int(size/4)][2+int(size/4)]=1
#arrayValues[2+int(size/4)][4+int(size/4)]=1
#arrayValues[3+int(size/4)][4+int(size/4)]=1
#arrayValues[3+int(size/4)][3+int(size/4)]=1

#Weird fractal type shape
#arrayValues[int(size/2)+1][int(size/2)+0]=1
#arrayValues[int(size/2)-1][int(size/2)+0]=1
#arrayValues[int(size/2)][int(size/2)+0]=1
#arrayValues[int(size/2)][int(size/2)+1]=1
#arrayValues[int(size/2)][int(size/2)+2]=1
#arrayValues[int(size/2)][int(size/2)+3]=1
#arrayValues[int(size/2)][int(size/2)+4]=1
#arrayValues[int(size/2)][int(size/2)+5]=1
#arrayValues[int(size/2)][int(size/2)+6]=1
#Add this to the above for a different pattern
#arrayValues[int(size/2)][int(size/2)+7]=1
#arrayValues[int(size/2)][int(size/2)+8]=1
#arrayValues[int(size/2)][int(size/2)+9]=1
#arrayValues[int(size/2)][int(size/2)+10]=1

arrayValues[0][0] = 1
arrayValues[size-1][size-1] = 2
arrayValues[0][size-1] = 3
arrayValues[size-1][0] = 4
#arrayValues[int(size/2)][int(size/2)] = 5

arrayValues = np.array(arrayValues)


def applyrules(cellVal, rownum, colnum, frame, curArrayValues, size):
    cellVal = int(cellVal)

    neighbors = []

    #Get the values of adjacent cells
    try:
        if (rownum+1)!=size:
            cellAbove = int(curArrayValues[rownum+1][colnum])
            neighbors.append(cellAbove)
        else:
            neighbors.append(0)
    except: 
        neighbors.append(0)
    try:
        if rownum != 0:
            cellBelow = int(curArrayValues[rownum-1][colnum])
            neighbors.append(cellBelow)
        else:
            neighbors.append(0)
    except: 
        neighbors.append(0)    
    try:
        if colnum != 0:
            cellLeft = int(curArrayValues[rownum][colnum-1])
            neighbors.append(cellLeft)
        else:
            neighbors.append(0)
    except: 
        neighbors.append(0)
    try:
        if (colnum+1)!=size:
            cellRight = int(curArrayValues[rownum][colnum+1])
            neighbors.append(cellRight)
        else:
            neighbors.append(0)
    except: 
        neighbors.append(0)
    try:
        if (colnum+1)!=size and (rownum+1)!=size:
            cellUpRight = int(curArrayValues[rownum+1][colnum+1])
            if cellUpRight == 1:
                neighborcount+=1
            neighbors.append(cellUpRight)
        else:
            neighbors.append(0)
    except: 
        neighbors.append(0)
    try:
        if colnum!=0 and (rownum+1)!=size:
            cellUpLeft = int(curArrayValues[rownum+1][colnum-1])
            neighbors.append(cellUpLeft)
        else:
            neighbors.append(0)
    except: 
        neighbors.append(0)
    try:
        if (colnum+1)!=size and rownum!=0:
            cellBelowRight = int(curArrayValues[rownum-1][colnum+1])
            neighbors.append(cellBelowRight)
        else:
            neighbors.append(0)
    except: 
        neighbors.append(0)
    try:
        if (colnum)!=0 and (rownum)!=0:
            cellBelowLeft = int(curArrayValues[rownum-1][colnum-1])
            neighbors.append(cellBelowLeft)
        else:
            neighbors.append(0)
    except: 
        neighbors.append(0)

    
    newneighbors = []
    for neighbor in neighbors:
        if neighbor!=0:
            newneighbors.append(neighbor)
    if newneighbors != []:
        cellVal = random.choice(newneighbors)
    
    




    
    return cellVal


frame = 0
def nextframe(frame, arrayValues, size, countPlot): #Loop
    plt.imshow(arrayValues, cmap='hot', interpolation='none', norm=mpl.colors.Normalize(vmin=0, vmax=5))
    plt.show(block=False)
    #plt.savefig(f'./out/frame-{str(frame)}.png') #Record frames into file
    newArrayValues = np.array(arrayValues)
    rownum = 0
    for row in arrayValues:
        colnum = 0
        for i in row:
            newArrayValues[rownum][colnum] = applyrules(i, rownum, colnum, frame, arrayValues, size)
            
            countPlot[rownum][colnum] += newArrayValues[rownum][colnum]
            colnum += 1
        rownum += 1
    arrayValues = np.array(newArrayValues)
    plt.pause(0.01)
    return countPlot, arrayValues


#for the count at the bottom
countPlot = np.zeros((size, size), dtype=int)

#3d array
threeDArray = np.empty((generations, size, size), dtype=object)

while frame<generations:
    threeDArray[frame] = arrayValues
    frame = frame+1
    countPlot, arrayValues = nextframe(frame, arrayValues, size, countPlot)

    #Weird idea I had for plotting smth about the values

    
    #plt.imshow(countPlot, cmap='hot', interpolation='none', norm=mpl.colors.Normalize(vmin=0, vmax=100))
    #plt.savefig(f'./out/heatmap-3frames/heatmap-{str(frame)}.png') #Record into file
    print(frame)

#mlab.contour3d(threeDArray.astype(np.int32)) # a window would pop up
#mlab.savefig('./out/3dmodel.obj')
#mlab.clf()







