# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 07:53:59 2017

@author: arnab
"""

"""
reference: https://www.hackerrank.com/challenges/minimum-average-waiting-time
"""

import heapq

if __name__ == '__main__':
    n = int(raw_input())
    
    heap, arr = [], []
    # add each item (cook_time, start_time) to arr and sort arr by start_time
    for _ in xrange(n):
        stime, ptime = map(int, raw_input().strip().split(" "))
        arr.append((ptime, stime))
    arr.sort(key = lambda x: x[1])

    # initalize heap with all items that start at earliest time
    i = 0
    while i < n and arr[i][1] == arr[0][1]:
        heapq.heappush(heap, arr[i])
        i += 1

    wtime, t = 0, 0
    while heap:
        # get the item with least cook_time, update current time 't' and wait time
        ptime, stime = heapq.heappop(heap)
        if stime > t:
            t += (stime - t) + ptime
        else:
            t += ptime
        wtime += t - stime
        
        # push items that have start time <= current time to heap
        while i < n and arr[i][1] <= t:
            heapq.heappush(heap, arr[i])
            i += 1
        
        # if heap is empty and items still left in arr to be cooked
        if i < n and not heap:
            tmp = arr[i][1]
            while i < n and arr[i][1] == tmp:
                heapq.heappush(heap, arr[i])
                i += 1
    print (wtime/n)
    