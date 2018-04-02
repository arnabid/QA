# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 21:13:45 2016

@author: arnab
"""

def findSystemMetrics(processes):
    """
    Given start and stop times of N processes on a machine,
    find the max idle time and total time the machine was active and idle.
    Also, return the max load on the system(# processes running concurrently 
    at any given point in time) 
    """
    events = []
    for item in processes:
        events += [(item[0], 1), (item[1], -1)]
    events.sort(key = lambda x: (x[0], x[1]))

    process1Start, processNEnd = events[0][0], events[-1][0]
    totalTime = processNEnd - process1Start
    activeProcess, lastProcessEnd = 0, process1Start
    totalIdleTime, maxIdleTime = 0, -float('inf')
    maxLoad = 0
    for event in events:
        if event[1] == 1:
            # a process starts
            if activeProcess == 0:
                idleTime = event[0] - lastProcessEnd
                totalIdleTime += idleTime
                maxIdleTime = max(maxIdleTime, idleTime)
            activeProcess += 1
            maxLoad = max(maxLoad, activeProcess)
        else:
            # a process ends
            activeProcess -= 1
            lastProcessEnd = event[0]
    totalActiveTime = totalTime - totalIdleTime
    return (totalActiveTime, totalIdleTime, maxIdleTime, maxLoad)


if __name__ == '__main__':
    #meetings = [[1,2], [2,5], [5,9]]
    #print (minRooms(meetings))
    processes = [[1,3], [2,3], [4,5], [10,12]]
    print (findSystemMetrics(processes))
