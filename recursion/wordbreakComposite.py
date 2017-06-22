# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 00:24:56 2017

@author: arnab
"""

"""
break word into a valid combination of simple words
"""

dictionary = set(["go", "dcat", "dog", "cat", "god", "goddog", "catdoggod", "goddogbat", "catcat"])

def wordbreak(s):
    return wordbreakUtil(s, len(s))

def wordbreakUtil(s, n):
    for i in xrange(1, n+1):
        prefix = s[0:i]
        
        if prefix in dictionary:
            if i == n:
                return 1
            l = wordbreakUtil(s[i:n], n-i)
            if l:
                return l + 1
    return None

if __name__ == '__main__':
    output = []

    for word in dictionary:
        l = wordbreak(word)
        """
        # if l = 1; it is a simple word; 
        # if l > 1; it is a valid composite word
        # if l is None, the input word cannot be broken into available simple words
        """
        if l and l > 1:
            output.append(word)
    print (output)