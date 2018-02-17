# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 00:24:56 2017

@author: arnab
"""

"""
Determine if the given word can be broken into a sequence of one or more dictionary words.
The dictionary of words is also provided.
reference: https://leetcode.com/problems/word-break/description/

The following solution just finds one valid decomposition if there exists one.
It does not find all valid decompositions. As an addition, it also finds the actual 
decomposition.
"""

dictionary = set(["bat", "dog", "cat", "catbat"])
nvalid = set()

def dfs(s, index, n, stack):
    if index == n:
        return True
    if index in nvalid:
        # print (stack) - debug
        stack.pop()
        return False
    for i in range(index+1, n+1):
        t = s[index:i]
        if t in dictionary:
            stack.append(i)
            if dfs(s, i, n, stack):
                return True
    nvalid.add(index)
    # print (stack) - debug
    stack.pop()
    return False

if __name__ == '__main__':
    word = "catbatdog"
    n = len(word)
    stack = [0]
    if dfs(word, 0, n, stack):
        print (" ".join(word[stack[k-1]:stack[k]] for k in range(1,len(stack))))
    #print (stack)
