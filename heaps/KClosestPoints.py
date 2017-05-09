# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 15:18:35 2016

@author: arnab
"""
import heapq

"""
O(nlogk), O(k) extra space
"""
def findKClosestPoints(allPoints, refPoint, k):
    # maintain a max heap of k nearest neighbors
    h = []
    for point in allPoints[0:k]:
        dist = (point[0] - refPoint[0]) ** 2 + (point[1] - refPoint[1]) ** 2
        h.append((-dist, point))
    heapq.heapify(h)

    for point in allPoints[k:]:
        dist = (point[0] - refPoint[0]) ** 2 + (point[1] - refPoint[1]) ** 2
        if dist < abs(h[0][0]):
            heapq.heapreplace(h, (-dist, point))

    return [item[1] for item in h]


if __name__ == '__main__':
    allPoints = [(2,0), (4,0), (0,5), (-3,0), (-6,-5), (6,7), (2,-3)]
    refPoint = (0,0)
    k = 3
    
    ans = findKClosestPoints(allPoints, refPoint, k)
    print (ans)