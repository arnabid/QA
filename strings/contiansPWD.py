# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 09:07:43 2017

@author: arnab
"""

"""
Amazon phone interview question:
given an input string and a method containsPWD(s), write a method to return the password
The method containsPWD(s) takes an input string as parameter and returns
True if the password is a substring of s and False otherwise in O(1) time.
"""

"""
refer to Algorithms - Sedgewick; pg 218
substring method (in Java) takes constant time
I am assuming that string slicing which is a way to do substring
in Python takes constant time
"""
PWD = "X"

def containsPWD(s):
    return PWD in s

def findPassword(s):
    # return None if the input string is empty
    if s == "":
        return None

    n = len(s)
    pwdFound = False
    # advance i from the left till the substring contains password
    for i in xrange(n):
        if containsPWD(s[:i+1]):
            pwdFound = True
            break
    
    # return None if the password does not exist in string s
    if pwdFound is False:
        return None
    
    # advance j from right to left starting from i till you get the actual password
    for j in xrange(i,-1,-1):
        if containsPWD(s[j:i+1]):
            return s[j:i+1]


if __name__ == '__main__':
    s = "jfhahjhdoXEH"
    ans = findPassword(s)
    print (ans)
    print (ans == PWD)

    