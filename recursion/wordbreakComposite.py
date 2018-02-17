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

dictionary = set(["apple", "pear", "pie", "cream", "applepie", "pearpiecake"])

# set of strings which cannot be broken down into 2 or more words
# used for memoization while backtracking
notValid = []

def wordbreakVER(s):
    n = len(s)
    for i in range(1, n+1):
        prefix = s[:i]
        
        if prefix in dictionary:
            if i == n:
                return 1
            l = wordbreak(s[i:])
            if l:
                return l + 1
    return 0


def wordbreak(s):
    n = len(s)
    for i in range(1, n+1):
        prefix = s[:i]
        
        if prefix in dictionary:
            if i == n:
                return 1
            if s[i:] not in notValid:
                l = wordbreak(s[i:])
                if l:
                    return l + 1
                else:
                    notValid.append(s[i:])
            else:
                print ("used notValid")
    return 0


if __name__ == '__main__':
    output = []
        """
        # if l = 1; it is a simple word; 
        # if l > 1; it is a valid composite word
        """
        l = wordbreak(word)
        if l > 1:
            print (l)
            output.append(word)
    print (output)
    print (nvalid)
