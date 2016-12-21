# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 20:57:50 2016

@author: arnab
"""

"""
Skyscraper problem:
https://www.hackerrank.com/challenges/jim-and-the-skyscrapers
"""
from collections import Counter

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().strip().split(" "))
    
    stack, total = [arr[0]], 0
    dic = Counter({arr[0]:1})
    for i in xrange(1,n):
        dic[arr[i]] += 1
        if arr[i] <= stack[-1]:
            stack.append(arr[i])
        else:
            while stack and arr[i] > stack[-1]:
                if dic[stack[-1]] > 1:
                    total += dic[stack[-1]]*(dic[stack[-1]]-1)
                del dic[stack.pop()]
            stack.append(arr[i])
    for key in dic:
        if dic[key] > 1:
            total += dic[key]*(dic[key]-1)
    print (total)
