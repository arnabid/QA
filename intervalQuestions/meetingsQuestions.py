# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:04:58 2017

@author: arnab
"""

import random
from collections import Counter

"""
maxNumberMeetings - maximum number of meetings that can be
attended/scheduled without overlap
scenario: maximize the number of talks that you can attend in a seminar
you earn points for each talk attended. Once you attend a talk,
you cannot leave until the talk is over.
"""
def maxNumberMeetings(meetings):
    meetings.sort(key = lambda x: (x[1], x[0]))
    final_meetings = [meetings[0]]
    for meeting in meetings[1:]:
        if meeting[0] >= final_meetings[-1][1]:
            final_meetings.append(meeting)
    return len(final_meetings)


"""
merge intervals
reference: https://leetcode.com/problems/merge-intervals/description/
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def merge(meetings):
    """
    :type meetings: List[Interval]
    :rtype: List[Interval]
    """
    if not meetings:
        return []
    meetings.sort(key = lambda x: x.start)
    final_meetings = [meetings[0]]
    for meeting in meetings[1:]:
        if meeting.start > final_meetings[-1].end:
            final_meetings.append(meeting)
        else:
            final_meetings[-1].end = max(meeting.end, final_meetings[-1].end)
    return final_meetings


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
def calcRooms(meetings):
    mnStart, mxStart = 25, -1
    mapM = Counter()
    for meeting in meetings:
        mapM[meeting[0]] += 1
        mapM[meeting[1]] -= 1
        mnStart = min(mnStart, meeting[0])
        mxStart = max(mxStart, meeting[0])
    
    activeMeetings, result = 0, 0
    """
    only consider mnStart to mxStart - meetings only end after that
    """
    for i in xrange(mnStart, mxStart+1):
        activeMeetings += mapM[i]
        result = max(result, activeMeetings)
    return result
        

if __name__ == '__main__':
    meetings = []
    for i in xrange(100):
        start = random.randint(1,12)
        end = random.randint(start+3,20)
        meetings.append([start,end])
#    print (meetings)
    print (maxNumberMeetings(meetings))
#    print (meetings)
#    print (maxNumberMeetings2(meetings))
#    print (minRooms(meetings), calcRooms(meetings))