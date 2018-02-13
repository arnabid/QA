# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 00:24:56 2017

@author: arnab
"""

"""
break word into a valid combination of simple words
reference: https://leetcode.com/problems/concatenated-words/#/description


a good test case where the memoization is useful:
word = aaaab
dic = set(["a", "aa"])
work out the code and see where the savings are achieved
"""

dictionary = set(["apple", "pear", "pie", "cream", "applepie"])

# set of strings which cannot be broken down into 2 or more words
# used for memoization while backtracking
notValid = set()

def wordbreak(s):
    n = len(s)
    for i in xrange(1, n+1):
        prefix = s[:i]
        
        if prefix in dictionary:
            if i == n:
                return 1
            if s[i:] not in notValid:
                l = wordbreak(s[i:])
                if l:
                    return l + 1
                else:
                    notValid.add(s[i:])
    return 0

if __name__ == '__main__':
    output = []

    for word in dictionary:
        """
        # if l = 1; it is a simple word; 
        # if l > 1; it is a valid composite word
        """
        l = wordbreak(word)
        if l > 1:
            output.append(word)
    print (output)

"""
dictionary = set(["apple", "pear", "pie", "pearcream", "cream", "applepeaf"])


def wb(s):
    if s == "":
        return 0

    n, i= len(s), 1
    count = 0
    while i < n+1:
        if s[:i] in dictionary:
            if i == n:
                count = 1
            else:
                count = 1 + wb(s[i:])
            break
        i += 1
    return count

if __name__ == '__main__':
    output = []
    for word in dictionary:
        nwords = wb(word)
        if nwords > 1:
            output.append(word)
    print (output)
"""
