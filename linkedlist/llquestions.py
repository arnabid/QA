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
reference: https://leetcode.com/problems/reverse-linked-list-ii/#/description
"""
def reverseBetween(head, m, n):
    if head is None or head.next is None or m == n:
        return head
    
    # s - node before the first node in the range [m,n] 
    s = ListNode(100)
    s.next = head
    head = s

    temp = m
    while temp > 1:
        s = s.next
        temp -= 1

    prev, curr = None, s.next
    last = curr
    t = n - m + 1
    while t > 0:
        n = curr.next
        curr.next = prev
        prev = curr
        curr = n
        t -= 1
    s.next = prev
    last.next = curr
    
    return head.next


"""
insert a node in a sorted list
"""
def sortedInsert(head, x):
    if head is None:
        return x
    
    if x.val < head.val:
        x.next = head
        return x
    
    c = head
    while c.next and c.next.val < x.val:
        c = c.next
    x.next = c.next
    c.next = x
    return head

"""
sort a list using insertion sort
reference: https://leetcode.com/problems/insertion-sort-list/#/description
"""
def insertionSortList(head):
    if head is None or head.next is None:
        return head

    c = head.next
    head.next = None
    while c:
        t = c.next
        head = sortedInsert(head, c)
        c = t
    return head


"""
merge 2 sorted lists
iteratively, recursively
"""
def mergeListsIter(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    
    res = None
    if l1.val <= l2.val:
        res = l1
        l1 = l1.next
    else:
        res = l2
        l2 = l2.next

    t = res
    while l1 and l2:
        if l1.val <= l2.val:
            t.next = l1
            l1 = l1.next
        else:
            t.next = l2
            l2 = l2.next
        t = t.next

    if l1:
        t.next = l1

    if l2:
        t.next = l2

    return res


def mergeListsRecur(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.val <= l2.val:
        l1.next = mergeListsRecur(l1.next, l2)
        return l1
    else:
        l2.next = mergeListsRecur(l1, l2.next)
        return l2


"""
sort a list using merge sort techniue
"""
def mergeSort(head):
    if head is None or head.next is None:
        return head
    lhalf, rhalf = frontBackSplit(head)
    lhalf = mergeSort(lhalf)
    rhalf = mergeSort(rhalf)
    return mergeListsIter(lhalf, rhalf)


"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
reference: https://leetcode.com/problems/swap-nodes-in-pairs/#/description
"""
def swapPairs(self, head):
    if head is None:
        return None

    if head.next is None:
        return head

    p = ListNode() # dummy node
    c = head
    n = c.next
    head = p
    while n:
        t = n.next
        p.next = n
        n.next = c
        c.next = t
        
        p = c
        c = t
        n = t.next if t else None
    return head.next

"""
Given a list, rotate the list to the right by k places, where k is non-negative.
For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""
def rotateRight(head, k):
    if head is None:
        return None
    # find the length of the linked list
    n = 0
    tmp = head
    while tmp:
        n += 1
        tmp = tmp.next

    k = k % n
    if k == 0:
        return head
        
    tmp = head
    for i in xrange(k):
        tmp = tmp.next
    
    last = head
    while tmp.next:
        tmp = tmp.next
        last = last.next
    
    tmp.next = head
    head = last.next
    last.next = None
    return head

"""
push node at the start of a linked list
"""
def pushFront(val, head):
    node = ListNode(val)
    if head is None:
        return node
    node.next = head
    return node

"""
Add 1 to a number represented as a linked list
Input: (7 -> 2 -> 4 -> 3) + 1
Output: 7 -> 2 -> 4 -> 4
"""
def addOneToNumber(l1):
    if l1 is None:
        return None
    curr, res = l1, None
    while curr.next:
        res = pushFront(curr.val)
    res = pushFront(curr.val + 1, res)

    carry = 0
    curr, res = res, None
    while curr:
        curr.val += carry
        carry = curr.val/10
        res = pushFront(curr.val%10, res)
        curr = curr.next
    
    if carry:
        res = pushFront(1, res)
    
    return res


"""
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
reference: https://leetcode.com/problems/add-two-numbers-ii/#/description
"""

def addTwoNumbers(l1, l2):
    n1, n2 = 0, 0
    curr1, curr2 = l1, l2
    
    # get n1
    while curr1:
        n1 += 1
        curr1 = curr1.next
    
    # get n2
    while curr2:
        n2 += 1
        curr2 = curr2.next
    
    res, curr1, curr2 = None, l1, l2
    while n1 > 0 or n2 > 0:
        digitsum = 0
        if n1 >= n2:
            digitsum += curr1.val
            n1 -= 1
            curr1 = curr1.next
        if n2 > n1:
            digitsum += curr2.val
            n2 -= 1
            curr2 = curr2.next
        res = pushFront(digitsum, res)
    
    carry = 0
    curr, res = res, None
    while curr:
        curr.val += carry
        carry = curr.val/10
        res = pushFront(curr.val%10, res)
        curr = curr.next
    
    if carry:
        res = pushFront(1, res)
    
    return res

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
    
    count, curr = 0, head
    # count the number of nodes in the list
    while curr:
        count += 1
        curr = curr.next

    curr = head
    count = (count-1)/2 # number of hops to the last node in the first half
    while count > 0:
        curr = curr.next
        count -= 1
    t = curr.next
    curr.next = None
    return head, t

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