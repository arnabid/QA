# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 08:12:03 2017

@author: arnab
"""

"""
Given a list, split it into two sublists — one for the front half, and one for the back half.
If the number of elements is odd, the extra element should go in the front list.
So FrontBackSplit() on the list {2, 3, 5, 7, 11} should yield the two lists {2, 3, 5}
and {7, 11}.
"""
def frontBackSplit(head):
    """ returns head1, head2
        head1 - head of the front half of the input list
        head2 - head of the back half of the input list
        head1 and head2 can be None
    """
    # empty list
    if head is None:
        return None, None
    # list with 1 node
    if head.next is None:
        return head, None
    
    count, tmp = 0, head
    while tmp:
        count += 1
        tmp = tmp.next
    head2 = head
    count = (count+1)/2
    while count > 0:
        head2 = head2.next
        count -= 1
    return head, head2
    