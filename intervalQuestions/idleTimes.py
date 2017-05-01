# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 18:09:36 2017

@author: arnab
"""

"""
assumption: all times are in 24 hour format
finds the idle time intervals and the total idle time
"""
def findIdleTimes(meetings, start, end):
    # array representing 24 hours in the day;
    # example arr[2] = hour from 2 am -> 3 am
    arr = [0] * 24   
    
    # for each meeting set the corresponding interval to 1 in arr
    for meeting in meetings:
        for i in range(meeting[0], meeting[1]):
            arr[i] = 1

    ftStart = None # start hour of each free interval
    if arr[start] == 0:
        ftStart = start
    
    idleTimes, totalITime = [], 0
    for i in range(start, end-1):
        if arr[i] == 0 and arr[i+1] == 1: # free time ends
            idleTimes.append((ftStart, i+1))
            totalITime += (i+1 - ftStart)
            ftStart = None
        elif arr[i] == 1 and arr[i+1] == 0: # free time begins
            ftStart = i+1
    if ftStart is not None:
        idleTimes.append((ftStart, end))
        totalITime += (end - ftStart)
    return idleTimes, totalITime

if __name__ == '__main__':
    meetings = [(9,10), (9,13), (13,15)]
    print (findIdleTimes(meetings, 9, 16))