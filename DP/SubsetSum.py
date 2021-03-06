# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:50:24 2016

@author: arnab
"""

""" Find if a subset from a given set of N non-negative integers sums upto
a given value K """

def solution2(S,k):
    S.insert(0,0)
    n = len(S)
    A = [[0 for i in range(k+1)] for i in range(n)]
    
    # A[i][j] = True if the sum j can be formed with elements in S from index 0 to i, both inclusive
    # make the first column True
    for i in range(n):
        A[i][0] = 1
    
    #print (A)
    for j in range(1,k+1):
        for i in range(1,n):
            if j - S[i] >= 0:  
                A[i][j] = A[i-1][j - S[i]]
            A[i][j] += A[i-1][j]

    print (A[n-1][k])
    print (A)

    # print all subsets that adds to k
    for i in range(n-1, 0, -1):
        if A[i][-1] > A[i-1][-1]:
            ans = []
            ii, j = i, k
            while ii >= 1 and j >= 1:
                if A[ii][j] > A[ii-1][j]: # include S[i]
                    ans.append(S[ii])
                    j = j - S[ii]
                    ii = ii-1
                elif A[ii][j] == A[ii-1][j]:
                    while ii-1 >= 1 and A[ii-1][j] == A[ii][j]:
                        ii -= 1
                    ans.append(S[ii])

            print (ans)


def solution(S,k):
    S.insert(0,0)
    n = len(S)
    A = [[False for i in range(k+1)] for i in range(n)]
    
    # A[i][j] = True if the sum j can be formed with elements in S from index 0 to i, both inclusive
    # make the first column True
    for i in range(n):
        A[i][0] = True
    
    #print (A)
    for j in range(1,k+1):
        for i in range(1,n):
            if A[i-1][j] == True: # the sum can be formed already without S[i]
                A[i][j] = True
            # the sum cannot be formed with the previous elements; check if S[i] can be used to form the sum ie j - S[i] can be
            # formed with the remaining elements
            elif j - S[i] >= 0:  
                A[i][j] = A[i-1][j - S[i]]
            # else: default value is false initially

    print (A[n-1][k])
    
    # print one subset that adds to k
    if A[-1][-1] == True:
        ans = []
        i, j = n-1, k
        while i >= 1 and j >= 1:
            if A[i][j] == True and A[i-1][j] == False: # include S[i]
                ans.append(S[i])
                j = j - S[i]
                i = i-1
            elif A[i][j] == True and A[i-1][j] == True: # include the first element that formed the sum
                while i-1 >= 1 and A[i-1][j] == True:
                    i -= 1
        print (ans)
    else:
        print ("No subset adds to %d" %k)

if __name__ == '__main__':
    k = 12
    S = [5,8,4,6,1]
    solution2(S, k)
