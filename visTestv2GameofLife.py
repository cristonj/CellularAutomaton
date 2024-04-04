import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import time
size = 256
arrayValues = np.zeros((size, size), dtype=int)

#Flying Machine
#arrayValues[1][4]=1
#arrayValues[2][2]=1
#arrayValues[2][4]=1
#arrayValues[3][4]=1
#arrayValues[3][3]=1

#Weird fractal type shape
arrayValues[int(size/2)+1][int(size/2)+0]=1
arrayValues[int(size/2)-1][int(size/2)+0]=1
arrayValues[int(size/2)][int(size/2)+0]=1
arrayValues[int(size/2)][int(size/2)+1]=1
arrayValues[int(size/2)][int(size/2)+2]=1
arrayValues[int(size/2)][int(size/2)+3]=1
arrayValues[int(size/2)][int(size/2)+4]=1
arrayValues[int(size/2)][int(size/2)+5]=1
arrayValues[int(size/2)][int(size/2)+6]=1
#Add this to the above for a different pattern
#arrayValues[int(size/2)][int(size/2)+7]=1
#arrayValues[int(size/2)][int(size/2)+8]=1
#arrayValues[int(size/2)][int(size/2)+9]=1
#arrayValues[int(size/2)][int(size/2)+10]=1

arrayValues = np.array(arrayValues)


def applyrules(cellVal, rownum, colnum, frame, curArrayValues, size):
    cellVal = int(cellVal)

    neighborcount = 0

    #Get the values of adjacent cells
    try:
        if (rownum+1)!=size:
            cellAbove = int(curArrayValues[rownum+1][colnum])
            if cellAbove == 1:
                neighborcount+=1
        else:
            cellAbove = cellVal
    except: 
        cellAbove = cellVal
    try:
        if rownum != 0:
            cellBelow = int(curArrayValues[rownum-1][colnum])
            if cellBelow == 1:
                neighborcount+=1
            
        else:
            cellBelow = cellVal
    except: 
        cellBelow = cellVal
    try:
        if colnum != 0:
            cellLeft = int(curArrayValues[rownum][colnum-1])
            if cellLeft == 1:
                neighborcount+=1
        else:
            cellLeft = cellVal
    except: 
        cellLeft = cellVal
    try:
        if (colnum+1)!=size:
            cellRight = int(curArrayValues[rownum][colnum+1])
            if cellRight == 1:
                neighborcount+=1
        else:
            cellRight=cellVal
    except: 
        cellRight = cellVal
    try:
        if (colnum+1)!=size and (rownum+1)!=size:
            cellUpRight = int(curArrayValues[rownum+1][colnum+1])
            if cellUpRight == 1:
                neighborcount+=1
        else:
            cellUpRight=cellVal
    except: 
        cellUpRight = cellVal
    try:
        if colnum!=0 and (rownum+1)!=size:
            cellUpLeft = int(curArrayValues[rownum+1][colnum-1])
            if cellUpLeft == 1:
                neighborcount+=1
        else:
            cellUpLeft = cellVal
    except: 
        cellUpLeft = cellVal
    try:
        if (colnum+1)!=size and rownum!=0:
            cellBelowRight = int(curArrayValues[rownum-1][colnum+1])
            if cellBelowRight == 1:
                neighborcount+=1
        else:
            cellBelowRight=cellVal
    except: 
        cellBelowRight = cellVal
    try:
        if (colnum)!=0 and (rownum)!=0:
            cellBelowLeft = int(curArrayValues[rownum-1][colnum-1])
            if cellBelowLeft == 1:
                neighborcount+=1
        else:
            cellBelowLeft=cellVal
    except: 
        cellBelowLeft = cellVal


    #If any are greater than the current cell, increase current cell temp by one.
    if cellVal == 1:
        if (neighborcount == 0) or (neighborcount == 1) or (neighborcount>=4):
            cellVal = 0
        elif (neighborcount == 2) or (neighborcount == 3):
            cellVal = 1
    
    if cellVal == 0:
        if neighborcount == 3:
            cellVal = 1
    
    




    
    return cellVal


frame = 0
def nextframe(frame, arrayValues, size): #Loop
    frame = frame+1
    plt.imshow(arrayValues, cmap='hot', interpolation='none', norm=mpl.colors.Normalize(vmin=0, vmax=1))
    plt.show(block=False)
    newArrayValues = np.array(arrayValues)
    rownum = 0
    for row in arrayValues:
        colnum = 0
        for i in row:
            newArrayValues[rownum][colnum] = applyrules(i, rownum, colnum, frame, arrayValues, size)
            colnum += 1
        rownum += 1
    arrayValues = np.array(newArrayValues)
    plt.pause(0.01)
    return arrayValues

while True:
    arrayValues = nextframe(frame, arrayValues, size)






