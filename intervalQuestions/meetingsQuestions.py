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

*** extra credit ***
also calculate the total time(union) of the merged intervals
union of the four intervals [1, 3], [2, 4.5], [6, 9], and [7, 8] is 6.5
"""

def merge(meetings):
    if not meetings:
        return []
    meetings.sort(key = lambda x: x[0])
    final_meetings = [meetings[0]]
    total = 0
    for meeting in meetings[1:]:
        if meeting[0] > final_meetings[-1][1]:
            total += final_meetings[-1][1] - final_meetings[-1][0]
            final_meetings.append(meeting)
        else:
            final_meetings[-1][1] = max(meeting[1], final_meetings[-1][1])

    total += final_meetings[-1][1] - final_meetings[-1][0]
    print (total)
    return final_meetings


"""
find the total number of intersections between meetings
example:

|-----|    |------|
      |------|

result = 2
"""
def numberIntersections(meetings):
    events = []
    for meeting in meetings:
        events.append([meeting[0], -1])
        events.append([meeting[1], 1])
    events.sort(key = lambda x : (x[0], x[1]))
    
    active, intersections = 0, 0
    for event in events:
        # meeting starts
        if event[1] == -1:
            intersections += active
            active += 1
        # meeting ends
        else:
            active -= 1
    return intersections



"""
return the minimum of rooms required to hold meetings
min rooms = maximum number of concurrent meetings at any given time
"""
def minMeetingRooms1(meetings):
    events = []
    for meeting in meetings:
        events.append([meeting[0], 1])
        events.append([meeting[1], -1])
    events.sort(key = lambda x : (x[0], x[1]))
    
    active, result = 0, 0
    for event in events:
        # meeting starts
        if event[1] == 1:
            active += 1
            result = max(result, active)
        # meeting ends
        else:
            active -= 1
    return result


def minMeetingRooms2(meetings):
    if not meetings:
        return 0
    mxStart = -float('inf')
    mapM = Counter()
    for meeting in meetings:
        mapM[meeting[0]] += 1
        mapM[meeting[1]] -= 1
        mxStart = max(mxStart, meeting[0])
    activeMeetings, result = 0, 0
    """
    get the times in sorted order till mxStart - meetings only end after that
    """
    for key in sorted(mapM): # get keys in sorted order
        if key <= mxStart:
            activeMeetings += mapM[key]
            result = max(result, activeMeetings)
        else:
            break
    return result

     

if __name__ == '__main__':
    meetings = []
    for i in xrange(20):
        start = random.randint(1,12)
        end = random.randint(start+3,start+4)
        meetings.append([start,end])
    print (minMeetingRooms2(meetings), minMeetingRooms1(meetings))