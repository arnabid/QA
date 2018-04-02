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
    buffer = [None] * (N+1)
    return fib_RM_helper(N, buffer)

def fib_RM_helper(N, buffer):
    if buffer[N]:
        return buffer[N]

    if N == 1 or N == 2:
        res = 1
    else:
        res = fib_RM_helper(N-1, buffer) + fib_RM_helper(N-2, buffer)

    buffer[N] = res
    return buffer[N]


"""
iterative solution
"""
def fib_I(N):
    if N == 1 or N == 2:
        return 1
    buffer = [None] * (N+1)
    buffer[1] = buffer[2] = 1
    for i in range(3, N+1):
        buffer[i] = buffer[i-1] + buffer[i-2]
    return buffer[N]

if __name__ == '__main__':
    n = 60
    
    # iterative solution
    print (fib_I(n))

    # recursive solution with memoization
    print (fib_RM(n))

    