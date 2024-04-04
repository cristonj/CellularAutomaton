import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import time
size = 128
arrayValues = np.zeros((size, size), dtype=int)


arrayValues[0][0]=100
arrayValues[size-1][size-1]=100
arrayValues[int(size/2)][int(size/2)]=100


arrayValues = np.array(arrayValues)


def applyrules(cellVal, rownum, colnum, frame, curArrayValues, size):
    cellVal = int(cellVal)

    #Get the values of adjacent cells
    try:
        if (rownum+1)!=size:
            cellAbove = int(curArrayValues[rownum+1][colnum])
        else:
            cellAbove = cellVal
    except: 
        cellAbove = cellVal
    try:
        if rownum != 0:
            cellBelow = int(curArrayValues[rownum-1][colnum])
        else:
            cellBelow = cellVal
    except: 
        cellBelow = cellVal
    try:
        if colnum != 0:
            cellLeft = int(curArrayValues[rownum][colnum-1])
        else:
            cellLeft = cellVal
    except: 
        cellLeft = cellVal
    try:
        if (colnum+1)!=size:
            cellRight = int(curArrayValues[rownum][colnum+1])
        else:
            cellRight=cellVal
    except: 
        cellRight = cellVal


    #If any are greater than the current cell, increase current cell temp by one.
    if (cellAbove>cellVal) or (cellBelow>cellVal) or (cellRight>cellVal) or (cellLeft>cellVal):
        cellVal = cellVal + 1
    




    
    return cellVal


frame = 0
def nextframe(frame, arrayValues, size): #Loop
    frame = frame+1
    plt.imshow(arrayValues, cmap='cool', interpolation='none', norm=mpl.colors.Normalize(vmin=0, vmax=90))
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






