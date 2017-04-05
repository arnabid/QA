# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:39:03 2016

@author: arnab
"""

"""
Find a set of words possible for a given phone number 
where each number maps to digits as below

1 - 
2 - a,b,c
3 - d,e,f
4 - g,h,i
5 - j,k,l
6 - m,n,o
7 - p,q,r,s
8 - t,u,v
9 - w,x,y,z
0 - +
"""

def solutionR(dic, number):
    n = len(number)
    if n == 1:
        return dic[int(number[0])]

    prefixes = solutionR(dic, number[0:n-1])
    words = [prefix+c for c in dic[int(number[-1])] for prefix in prefixes]
    return words

def solutionVerbose(keypad, number):
    number = str(number)
    
    words = ['']
    for digit in number:
        temp = []
        for ch in keypad[int(digit)]:
            for prefix in words:
                temp.append(prefix + ch)
        words = temp
    return words
                

def solution(dic, number):
    if number is None:
        return None

    number = str(number)
    words = ['']
    
    for n in number:
        words = [prefix+c for c in dic[int(n)] for prefix in words]
    
    return words
    
if __name__ == '__main__':
    dic = {}
    dic[1] = ['']
    dic[2] = ['a', 'b', 'c']
    dic[3] = ['d', 'e', 'f']
    dic[4] = ['g', 'h', 'i']
    dic[5] = ['j', 'k', 'l']
    dic[6] = ['m', 'n', 'o']
    dic[7] = ['p', 'q', 'r', 's']
    dic[8] = ['t', 'u', 'v']
    dic[9] = ['w', 'x', 'y', 'z']
    dic[0] = ['+']
    
    number = 3314
    
    # find the number of words that can be formed
    n = 1
    for digit in str(number):
        n *= len(dic[int(digit)])
    print (n)

    words = solution(dic, number)
    print (words)
    print (len(words))
    
    #words = solutionVerbose(dic, number)
    words = solutionR(dic, str(number))
    print (words)
    print (len(words))