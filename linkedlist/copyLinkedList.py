# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:59:06 2017

@author: arnab
"""

class Node(object):
    def __init__(self, data = None):
        self.val = data
        self.next = None

    def copylinkedlist(head):
        # return None if head is None
        if head is None:
            return None
        
        head2 = Node(head.val)
        tmp = head2
        head = head.next
        while head:
            node = Node(head.val)
            tmp.next = node
            t = head.next
            head.next = tmp
            tmp.random = head
            tmp = tmp.next
            head = t
        
        tmp = head2
        while tmp:
            tmp.random = tmp.random.random.next
            
        return head2