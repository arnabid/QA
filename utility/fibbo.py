# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 17:04:35 2017

@author: arnab
"""

"""
Find the nth Fibonacci number
1 1 2 3 5 8 ....
"""

"""
recursive solution
"""
def fib(N):
    if N == 1 or N == 2:
        return 1
    else:
        return fib(N-1) + fib(N-2)


"""
recursive solution with memoization
"""
def fib_RM(N):
    arr = [None] * (N+1)
    arr[1] = arr[2] = 1
    return fib_RM_helper(N, arr)

def fib_RM_helper(N, buffer):
    if arr[N]:
        return arr[N]

    arr[N] = fib_RM_helper(N-1, arr) + fib_RM_helper(N-2, arr)
    return arr[N]


"""
iterative solution
"""
def fib_I(N):
    if N == 1 or N == 2:
        return 1
    arr = [None] * (N+1)
    arr[1] = arr[2] = 1
    for i in range(3, N+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[N]

if __name__ == '__main__':
    n = 60
    
    # iterative solution
    print (fib_I(n))

    # recursive solution with memoization
    print (fib_RM(n))

    