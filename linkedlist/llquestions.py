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
    
    count, current = 0, head
    while current:
        count += 1
        current = current.next
    current = head
    count = (count+1)/2 # number of nodes in the first half
    while count > 0:
        current = current.next
        count -= 1
    return head, current

"""
Write a RemoveDuplicates() function which takes a list sorted in increasing order
and deletes any duplicate nodes from the list. Ideally, the list should only be
traversed once.
"""

def removeDuplicates(head):
    """
    returns head of the modified list
    """
    if head is None: # do nothing if the list is empty
        return
    current = head
    while current.next:
        if current.data == (current.next).data:
            current.next = (current.next).next
        else:
            current = current.next
    return head


"""
Write a function AlternatingSplit() that takes one list and divides up its nodes
to make two smaller lists. The sublists should be made from alternating elements
in the original list. So if the original list is {a, b, a, b, a}, then one sublist
should be {a, a, a} and the other should be {b, b}. 
"""

def alternatingSplit(head):
    """
    returns head1, head2
    head1 - head of one sublist
    head2 - head of the second sublist
    """
    if head is None:
        return None, None
    if head.next is None:
        return head, None
    
    head1, head2 = head, head.next
    while head1 and head2:
        head1.next = head2.next
        if head2.next:
            head2.next = (head2.next).next
        
        head1 = head1.next
        head2 = head2.next
    return head, head.next