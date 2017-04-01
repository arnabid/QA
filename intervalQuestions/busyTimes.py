# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 18:13:14 2017

@author: arnab
"""

def findBusyTimes(meetings, start, end):
    # array representing 24 hours in the day;
    # example arr[2] = hour from 2 am -> 3 am
    arr = [0] * 24   
    
    # for each meeting set the corresponding interval to 1 in arr
    for meeting in meetings:
        for i in range(meeting[0], meeting[1]):
            arr[i] = 1

    btStart = None # start hour of each busy interval
    if arr[start] == 1:
        btStart = start
    
    busyTimes = []
    for i in range(start, end-1):
        if arr[i] == 0 and arr[i+1] == 1: # busy time begins
            btStart = i+1
        elif arr[i] == 1 and arr[i+1] == 0: # busy time ends
            busyTimes.append((btStart, i+1))
            btStart = None
    if btStart is not None:
        busyTimes.append((btStart, end))
    return busyTimes

if __name__ == '__main__':
    meetings = [(9,10), (9,13), (13,15), (17,20)]
    print (findBusyTimes(meetings, 9, 18))