import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import time

arrayValues = np.zeros((128, 128), dtype=int)


arrayValues[0][0]=100
arrayValues[0][127]=100
arrayValues[64][64]=100
arrayValues = np.array(arrayValues)
def applyrules(cellVal, rownum, colnum, frame, curArrayValues):
    cellVal = int(cellVal)

    #Get the values of adjacent cells
    try:
        cellAbove = int(curArrayValues[rownum+1][colnum])
    except: 
        cellAbove = cellVal
    try:
        cellBelow = int(curArrayValues[rownum-1][colnum])
    except: 
        cellBelow = cellVal
    try:
        cellLeft = int(curArrayValues[rownum][colnum-1])
    except: 
        cellLeft = cellVal
    try:
        cellRight = int(curArrayValues[rownum][colnum+1])
    except: 
        cellRight = cellVal


    #If any are greater than the current cell, increase current cell temp by one.
    if cellAbove > cellVal or cellBelow>cellVal or cellRight>cellVal or cellLeft>cellVal:
        cellVal = cellVal + 1
    




    
    return cellVal


frame = 0
while True: #Loop
    frame = frame+1
    plt.imshow(arrayValues, cmap='cool', interpolation='none')
    plt.show(block=False)
    newArrayValues = np.array(arrayValues)
    rownum = 0
    for row in arrayValues:
        colnum = 0
        for i in row:
            newArrayValues[rownum][colnum] = applyrules(i, rownum, colnum, frame, arrayValues)
            colnum += 1
        rownum += 1
    arrayValues = np.array(newArrayValues)
    plt.pause(0.01)








