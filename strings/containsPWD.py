# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 09:07:43 2017

@author: arnab
"""

"""
Phone interview question:
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

def findPassword(s):
    i, j = -1, len(s)
    
    # keep increasing i from the left till s[i...j] contains password
    while containsPWD(s[i+1:j]):
        i += 1
    
    # keep decreasing j from the right till s[i...j] conatains password
    while containsPWD(s[i:j]):
        j -= 1
    
    if i >= 0:
        return s[i:j+1]
    else:
        return None


if __name__ == '__main__':
    s = "xyzxyzxyz"
    ans = findPassword(s)
    print (ans)
    print (ans == PWD)

    