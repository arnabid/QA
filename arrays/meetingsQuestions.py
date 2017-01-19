# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:04:58 2017

@author: arnab
"""

import random

"""
maxNumberMeetings - maximum number of meetings that can be
attended without overlap
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
        if not overlap:
            final_meetings.append(meeting)
    return len(final_meetings)


"""
minRooms - minimum number of rooms required to schedule
list of meetings
"""
def minRooms(meetings):
    events = []
    for item in meetings:
        events += [(item[0], 1), (item[1], -1)]
    
    # events holds the start and stop times of all meetings
    # in increasing order, for start and stop times coinciding, stop times are 
    # placed first
    events.sort(key = lambda x: (x[0], x[1]))
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

if __name__ == '__main__':
    meetings = []
    for i in xrange(5):
        start = random.randint(1,9)
        end = random.randint(start+1,11)
        meetings.append([start,end])
    print (meetings)
    print (maxNumberMeetings(meetings))
    print (minRooms(meetings))