# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 17:11:54 2017

@author: arnab
"""

"""
Given a stack of integers of size n, 
sort it using only push and pop operations in O(1) space.
reference: https://www.careercup.com/question?id=5721957644369920
"""

def sortStack(stack):
    if stack:
        p = stack.pop()
        sortStack(stack)
        insertInOrder(stack, p)


def insertInOrder(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
    else:
        p = stack.pop()
        insertInOrder(stack, element)
        stack.append(p)


def main():
    stack = map(int, raw_input().strip().split(" "))
    
    # print stack before sort
    print ("stack before sort = {0}".format(stack))
    
    # sort the stack
    sortStack(stack)
    
    # print stack after sort
    print ("stack after sort = {0}".format(stack))


if __name__ == '__main__':
    main()
    
    