# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 09:32:04 2017

@author: arnab
"""

"""
print permutations of a string
reference: http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
http://introcs.cs.princeton.edu/java/23recursion/Permutations.java.html
"""

def permute1(a, l, r):
    if l == r:
        print (''.join(a))
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute1(a, l+1, r)
            a[l], a[i] = a[i], a[l]
            
def permute2(prefix, s, perms):
    """
    perms holds only distinct permutations
    """
    n = len(s)
    if n == 0:
        perms.add(prefix)
    else:
        for i in xrange(n):
            permute2(prefix+s[i], s[0:i]+s[i+1:n], perms)

def permute3(arr, n):
    if n == 1:
        print (''.join(arr))
    else:
        for i in xrange(n):
            arr[n-1], arr[i] = arr[i], arr[n-1]
            permute3(arr, n-1)
            arr[n-1], arr[i] = arr[i], arr[n-1]


if __name__ == '__main__':
    s = "ABCA"
    a = list(s)
    #permute1(a, 0, len(a)-1)
    perms = set()
    permute2("", s, perms)
    print perms, len(perms)
