# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 08:30:12 2017

@author: arnab
"""

"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Return the head node of the updated list
 Node is defined below.
"""
 
class Node(object):
   def __init__(self, data = None, next_node = None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node
      
def SortedInsert(head, data):
    
    # empty list
    if head is None:
        return head

    tmp, p = head, None
    while tmp and tmp.data < data:
        p = tmp
        tmp = tmp.next
    
    # insert at end
    if tmp is None:
        nn = Node(data, None, p)
        p.next = nn
    # insert at start
    elif p is None:
        nn = Node(data, head, None)
        head = nn
    # insert between p and tmp
    else:
        nn = Node(data, tmp, p)
        p.next = nn
        tmp.prev = nn
    return head
