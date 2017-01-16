# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 20:50:05 2017

@author: arnab
"""

def divide(dividend, divisor):
    maxintp = 2147483647
    maxintn = -2147483648

    if divisor == 0:
         raise ValueError("divisor is 0")
    
    if dividend == 0:
        return 0

    if divisor == 1:
        return min(max(maxintn, dividend), maxintp)

    if divisor == -1:
        return min(max(maxintn, -dividend), maxintp)
    
    positive = (dividend > 0) is (divisor > 0)
    
    dividend, divisor = abs(dividend), abs(divisor)
    denominator, result = divisor, 1
    while dividend > denominator:
        denominator <<= 1
        result <<= 1
    
    while denominator > dividend:
        denominator -= divisor
        result -= 1
    
    if not positive:
        result = -result
    
    return min(max(maxintn, result), maxintp)

if __name__ == '__main__':
    dividend = int(raw_input())
    divisor = int(raw_input())
    
    print (divide(dividend, divisor))