# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 00:24:56 2017

@author: arnab
"""

"""
break word into a valid combination of simple words
reference: https://leetcode.com/problems/concatenated-words/#/description
"""

dictionary = set(["apple", "pear", "pie", "cream", "applepie"])

def dfs(s, index, n, stack, dictionary, nvalid):
    if index == n:
        return True
    if index in nvalid:
        stack.pop()
        return False
    for i in range(index+1, n+1):
        t = s[index:i]
        if t in dictionary:
            stack.append(i)
            if dfs(s, i, n, stack, dictionary, nvalid):
                return True
    nvalid.add(index)
    stack.pop()
    return False


if __name__ == '__main__':
    output = []
    for word in dictionary:
        n = len(word)
        nvalid = set()
        stack = [0]
        if dfs(word, 0, n, stack, dictionary, nvalid) and len(stack) > 2:
            output.append(word)
    print (output)
