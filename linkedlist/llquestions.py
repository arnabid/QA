# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 08:12:03 2017

@author: arnab
"""

class ListNode(object):
    def __init__(self, data = None):
        self.val = data
        self.next = None


class TreeNode(object):
    def __init__(self, data = None):
        self.val = data
        self.left = None
        self.right = None


"""
Given a singly linked list, determine if it is a palindrome.
O(N) time and O(1) space
"""
def isPalindrome(self, head):
    # return True if list is empty or has only 1 node
    if head is None or head.next is None:
        return True
    
    fast, slow = head, head
    count = 0
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        count += 1
    
    prev, curr = None, slow
    while curr:
        n = curr.next
        curr.next = prev
        prev = curr
        curr = n
    
    tail = prev
    while count > 0:
        if head.val != tail.val:
            return False
        head = head.next
        tail = tail.next
        count -= 1
    
    return True


"""
convert sorted linked list to a binary search tree
"""
def sortedListToBST(head):
    if head is None:
        return None
    return sortedListToBSTUtil(head, None)

def sortedListToBSTUtil(head, tail):
    if head == tail:
        return None
    
    slow, fast = head, head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    
    node = TreeNode(slow.val)
    node.left = sortedListToBSTUtil(head, slow)
    node.right = sortedListToBSTUtil(slow.next, tail)
    
    return node


"""
clone a linked list; return the head of the cloned linked list
"""
def clone(head):
    if head is None:
        return None
    result = ListNode(head.val)
    result.next = clone(head.next)
    return result

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