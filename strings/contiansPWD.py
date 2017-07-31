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
PWD = "xyz"

def containsPWD(s):
    return PWD in s

def findPassword1(s):
    # return None if the input string does not contain the password
    if not containsPWD(s):
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

def findPassword2(s):
    # return None if the input string does not contain the password
    if not containsPWD(s):
        return None

    n = len(s)
    i, j = 0, n-1
    status = True
    # keep 2 pointers i, j and advance them if the remaining part of string
    # contains the password
    while status:
        status =  False
        if containsPWD(s[i+1:j+1]):
            i += 1
            status = True
        if containsPWD(s[i:j]):
            j -= 1
            status = True
    return s[i:j+1]


if __name__ == '__main__':
    s = ""
    ans = findPassword1(s)
    print (ans)
    print (ans == PWD)

    