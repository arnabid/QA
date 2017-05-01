# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:04:58 2017

@author: arnab
"""

import random
from collections import Counter

"""
maxNumberMeetings - maximum number of meetings that can be
attended without overlap
scenario: maximize the number of talks that you can attend in a seminar
you earn points for each talk attended. Once you attend a talk,
you cannot leave until the talk is over.
"""
def maxNumberMeetings(meetings):
    meetings.sort(key = lambda x: x[1])
    #sorted_meetings = sorted(meetings, key=operator.itemgetter(1))
    final_meetings = []
    for meeting in meetings:
        overlap = False
        for sample in final_meetings:
            if meeting[0] < sample[1] and meeting[1] > sample[0]:
                    overlap = True
                    break
        if not overlap:
            final_meetings.append(meeting)
    return len(final_meetings)

def maxNumberMeetings2(meetings):
    meetings.sort(key = lambda x: x[1])
    final_meetings = []
    for meeting in meetings:
        overlap = False
        for item in final_meetings:
            if not (meeting[1] <= item[0] or meeting[0] >= item[1]):
                overlap = True
                break
        if not overlap:
            final_meetings.append(meeting)
    return len(final_meetings)

"""
minRooms - minimum number of rooms required to schedule
list of meetings
minRooms = maximum number of active meetings at any given time
time - nlogn; space - n
"""
def minRooms(meetings):
    events = []
    for meeting in meetings:
        events += [(meeting[0], 1), (meeting[1], -1)]
    events.sort(key = lambda x: (x[0], x[1]))
    
    """
    events holds the start and stop times of all meetings
    in increasing order, for start and stop times coinciding, stop times are 
    placed first
    """
    result, occupiedrooms = 0, 0
    for event in events:
        if event[1] == 1:
            # meeting starts
            occupiedrooms += 1
            result = max(result, occupiedrooms)
        else:
            # meeting stops
            occupiedrooms -= 1
    return result

"""
time - n; space - constant
"""
def calcRooms(meetings, start = None, end = None):
    mnStart, mxEnd = 25, -1
    mapM = Counter()
    for meeting in meetings:
        mapM[meeting[0]] += 1
        mapM[meeting[1]] -= 1
        mnStart = min(mnStart, meeting[0])
        mxEnd = max(mxEnd, meeting[1])
    
    if start is None:
        start = mnStart
    
    if end is None:
        end = mxEnd
    
    activeMeetings, result = 0, 0
    for i in xrange(start, end+1):
        if i in mapM:
            activeMeetings += mapM[i]
            result = max(result, activeMeetings)
    return result
        

if __name__ == '__main__':
    meetings = []
    for i in xrange(50):
        start = random.randint(1,7)
        end = random.randint(start+3,11)
        meetings.append([start,end])
#    print (meetings)
#    print (maxNumberMeetings(meetings))
#    print (meetings)
#    print (maxNumberMeetings2(meetings))
    print (minRooms(meetings), calcRooms(meetings))