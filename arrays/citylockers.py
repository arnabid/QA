# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 08:55:12 2016

@author: arnab
"""


"""
2 other approaches:
start a bfs from each locker location and update label accordingly

take all points on the same row and column of a landmark and put them in a queue
while not q is empty do:
    take each point out from the queue
    process its neighbors
    update label and put them in queue if not already present in queue

Question: Is there a way to prove that each point in the grid is written and removed
from the queue only once?

Runtime complxity O(m*n*C); C = small constant

instead of the method below where the run time complexity is O(m*n*L)
L = number of landmarks

"""


import itertools

def solution1(cityLength, cityWidth, lockerXCoordinates, lockerYCoordinates):
    
    # define the output grid
    maxdist = cityLength+cityWidth-2
    grid = [[maxdist for i in xrange(cityWidth)] for i in xrange(cityLength)]
    
    for lockerX, lockerY in itertools.izip(lockerXCoordinates, lockerYCoordinates):
        grid[lockerX-1][lockerY-1] = 0

    for i in xrange(cityLength):
        for j in xrange(cityWidth):
            # get the locker locations
            if grid[i][j] != 0:
                for lockerX, lockerY in itertools.izip(lockerXCoordinates, lockerYCoordinates):
                    dist = abs(i-lockerX+1) + abs(j-lockerY+1)
                    grid[i][j] = min(grid[i][j], dist)
    
    print (grid)

def solution(cityLength, cityWidth, lockerXCoordinates, lockerYCoordinates):
    
    # define the output grid
    grid = [[float('inf') for i in xrange(cityWidth)] for i in xrange(cityLength)]
    
    #numLockers = len(lockerXCoordinates)
    for i in xrange(1,cityLength+1):
        for j in xrange(1,cityWidth+1):
            # get the locker locations
            for lockerX, lockerY in itertools.izip(lockerXCoordinates, lockerYCoordinates):
            #for index in xrange(numLockers):
                #lockerX = lockerXCoordinates[index]
                #lockerY = lockerYCoordinates[index]
                # get the manhattan distance to this locker from (i,j)
                mdist = abs(i-lockerX) + abs(j-lockerY)
                grid[i-1][j-1] = min(grid[i-1][j-1], mdist)
                # if the grid location is a locker, skip remaining lockers
                if grid[i-1][j-1] == 0:
                    break
    
    print (grid)

if __name__ == '__main__':
    cityLength = 4
    cityWidth = 5
    lockerXCoordinates = [2,3,1]
    lockerYCoordinates = [2,4,1]
    solution(cityLength,cityWidth,lockerXCoordinates,lockerYCoordinates)
    print ("=====")
    solution1(cityLength,cityWidth,lockerXCoordinates,lockerYCoordinates)

    
            