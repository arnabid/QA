# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 20:10:10 2016

@author: arnab
"""

""" Given an encoded message containing digits, determine the total number
of ways to decode it. """

def decode(msg):
    """ a[i] = # decodings of string of length i """
    n = len(msg)
    if n == 0 or msg[0] == '0':
        return 0
        
    a = [0] * (n+1)
    a[0], a[1] = 1,1
    
    for i in xrange(2,n+1):
        if msg[i-1] > '0':
            a[i] = a[i-1]
        
        if (msg[i-2] > '0' and msg[i-2] < '2') or (msg[i-2] == '2' and msg[i-1] < '7'):
            a[i] += a[i-2]
    
    return a[n]


if __name__ == '__main__':
    msg = "102"
    print (decode(msg))