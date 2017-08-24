# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 10:44:39 2016

@author: arnab
"""
"""
reverse the words in a string
this is a string -> string a is this
+= concatenation for strings is not slow
"""

def reverseInPlace(s):
    arr = [ch for ch in s]
    
    n = len(s)
    i, j = 0, n-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    i = 0
    for j in xrange(n):
        if arr[j] == " ":
            k = j - 1
            while i < k:
                arr[i], arr[k] = arr[k], arr[i]
                i += 1
                k -= 1
            i = j + 1

    k = j - 1
    while i < k:
        arr[i], arr[k] = arr[k], arr[i]
        i += 1
        k -= 1
    print ("".join(arr))


def reverse(s):
    n = len(s)
    end = n
    output = ""
    
    for i in xrange(n-1,-1,-1):
        if s[i] == " ":
            output += s[i+1:end]
            output += " "
            end = i
    output += s[0:end]
    print (output)

if __name__ == '__main__':
    s = "x this is a string"
    
    reverseInPlace(s.strip())
