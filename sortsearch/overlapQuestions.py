# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 21:13:45 2016

@author: arnab
"""

def findMaxProcesses(meetings):
    """
    returns the maximum number of non-overlapping processes/meetings that
    can be scheduled
    """
    final_meetings = []
    meetings.sort(key = lambda x: x[1])
    for sample in meetings:
        overlapped = False
        for meeting in final_meetings:
            if sample[0] < meeting[1] and sample[1] > meeting[0]:
                overlapped = True
        if not overlapped:
            final_meetings.append(sample)
    
    # final_meetings holds the meetings/processes that can be scheduled/run
    return (len(final_meetings))


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
            

def minRooms(meetings):
    # returns the minimum number of rooms required to hold meetings w/o overlap
    events = []
    for item in meetings:
        events += [(item[0], 1), (item[1], -1)]
    
    # events holds the start and stop times of all meetings
    # in increasing order, for start and stop times coinciding, stop times are 
    # placed first
    events.sort(key = lambda x: (x[0], x[1]))
    totalrooms, occupiedrooms = 0, 0
    for event in events:
        if event[1] == 1:
            # meeting starts
            occupiedrooms += 1
            totalrooms = max(totalrooms, occupiedrooms)
        else:
            # meeting stops
            occupiedrooms -= 1
    return totalrooms

if __name__ == '__main__':
    #meetings = [[1,2], [2,5], [5,9]]
    #print (minRooms(meetings))
    processes = [[1,3], [2,3], [4,5], [10,12]]
    print (findSystemMetrics(processes))