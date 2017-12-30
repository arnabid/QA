# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 17:04:35 2017

@author: arnab
"""

"""
Find the nth Fibonacci number
"""

"""
recursive solution
"""
def fib(N):
    if N < 0:
        raise ValueError("invalid N")
    elif N == 0 or N == 1:
        return 1
    else:
        return fib(N-2) + fib(N-1)


"""
recursive solution with memoization
"""
buffer = [1,1]
def fib_RM(N):
    if N < 0:
        raise ValueError("invalid N")
    elif N < len(buffer):
        return buffer[N]
    else:
        t = fib_RM(N-2) + fib_RM(N-1)
        buffer.append(t)
        return t


"""
iterative solution
"""
def fib_I(N):
    if N < 0:
        raise ValueError("invalid N")
    elif N == 0 or N == 1:
        return 1
    else:
        t2, t1 = 1, 1
        res = 0
        while N >= 2:
            res = t2 + t1
            t2 = t1
            t1 = res
            N -= 1
        return res

if __name__ == '__main__':
    n = 10
    
    # iterative solution
    print (fib_I(n))

    # recursive solution with memoization
    print (fib_RM(n))

    