# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 20:54:00 2017

@author: arnab
"""

"""
Problem Statement: On a positive integer, you can perform any one of the 
following 3 steps. 1.) Subtract 1 from it. ( n = n - 1 )  , 2.) 
If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )  , 
3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ). 
Now the question is, given a positive integer n, find the minimum number 
of steps that takes n to 1
"""

def sol(n):
    if n == 1:
        return 0
    
    steps = [0] * (n+1)
    for i in xrange(2, n+1):
        steps[i] = steps[i-1] + 1
        if i % 2 == 0:
            steps[i] = min(steps[i], steps[i/2]+1)
        if i % 3 == 0:
            steps[i] = min(steps[i], steps[i/3]+1)
    return steps[n]

if __name__ == '__main__':
    n = int(raw_input())
    print (sol(n))
