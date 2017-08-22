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

example:
|---|
      |-----|
            |

In the case of edge-cases, where the start time = end time of a meeting,
sorting by end times and then by start times will include all 3 meetings (correct answer)
but not sorting by start times might incude only 2 meetings.

  1
|----|       2
          |-----|
            3
       |--------|

sorting by end time and then by start time also has the nice
side-effect that it minimizes the total idle time of the resource.

meeting 3 is selected instead of meeting 2 in the above example.

*** also calculates the total idle time and total busy time
       
"""
def maxNumberMeetings(meetings):
    meetings.sort(key = lambda x: (x[1], x[0]))
    idleTime = 0
    final_meetings = [meetings[0]]
    for meeting in meetings[1:]:
        if meeting[0] >= final_meetings[-1][1]:
            idleTime += meeting[0] - final_meetings[-1][1]
            final_meetings.append(meeting)
    
    """
    *** extra credit ***
    totalTime = final_meetings[-1][1] - final_meetings[0][0]
    busyTime = totalTime - idleTime
    print "busy time = ", busyTime
    print "idle time = ", idleTime
    """
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
time - n; space - constant
"""
def minMeetingRooms1(meetings):
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
    if the range(mnStart, mxStart) is small
    """
    for i in xrange(mnStart, mxStart+1):
        activeMeetings += mapM[i]
        result = max(result, activeMeetings)
    return result


def minMeetingRooms2(meetings):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    if not meetings:
        return 0
    mxStart = -1
    mapM = Counter()
    for meeting in meetings:
        mapM[meeting.start] += 1
        mapM[meeting.end] -= 1
        mxStart = max(mxStart, meeting.start)
    activeMeetings, result = 0, 0
    """
    get the times in sorted order till mxStart - meetings only end after that
    """
    for key in sorted(mapM):
        if key <= mxStart:
            activeMeetings += mapM[key]
            result = max(result, activeMeetings)
        else:
            break
    return result

     

if __name__ == '__main__':
    meetings = []
    #meetings = [[1,2], [3,5], [4,7], [6,10]]
    for i in xrange(100):
        start = random.randint(1,12)
        end = random.randint(start+3,20)
        meetings.append([start,end])
#    print (meetings)
    print (maxNumberMeetings(meetings))
#    print (meetings)
#    print (maxNumberMeetings2(meetings))
#    print (minRooms(meetings), calcRooms(meetings))