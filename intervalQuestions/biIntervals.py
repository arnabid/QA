# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:10:56 2017

@author: arnab
"""

"""
returns busyTimes, totalBusyTime, idleTimes, totalIdleTime from [start...end]
busyTimes = list[list[int]]
idletimes = list[list[int]]

notes: check for intersection between interval1 and interval2
if interval1[0] < intrerval2[1] and interval1[1] > interval2[0]:
    intersection = True
"""

def findBusyIdleTimes(meetings, start, end):
    # merge all the overlapping intervals
    meetings.sort(key = lambda x: x[0])
    final_meetings = [meetings[0]]
    for meeting in meetings[1:]:
        if meeting[0] > final_meetings[-1][1]:
            final_meetings.append(meeting)
        else:
            final_meetings[-1][1] = max(meeting[1], final_meetings[-1][1])
    
    # list of intervals of idle times and busy times
    idleTimes, busyTimes = [], []
    # total idle time, total busy time
    tidle, tbusy = 0, 0

    lastEndtime = start    
    for meeting in final_meetings:
        if not (meeting[1] <= start or meeting[0] >= end): # if overlap with [start...end]
            # s = start of the busy interval between [start...end]
            s = max(start, meeting[0])
            # e = end of the busy interval between [start...end]
            e = min(end, meeting[1])
            
            if s > lastEndtime:
                idleTimes.append([lastEndtime, s])
                tidle += s - lastEndtime
            
            busyTimes.append([s,e])
            tbusy += e-s
            
            lastEndtime = e
    
    if end > lastEndtime:
        idleTimes.append([lastEndtime, end])
        tidle += end - lastEndtime
    
    return busyTimes, tbusy, idleTimes, tidle

if __name__ == '__main__':
    meetings = [[10,15]]
    print (findBusyIdleTimes(meetings, 18, 22))