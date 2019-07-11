# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 09:04:37 2016

@author: arnab
"""
def solution(s1,s2):
    # returns a boolean to indicate if s2 is a rotated version of s1
    if len(s1) != len(s2):
        return False
    s1 = s1+s1
    if s2 in s1:
        return True
    return False
    

if __name__ == '__main__':
    s1 = "lasvegas"
    s2 = "vegaslas"
    print (solution(s1,s2))
