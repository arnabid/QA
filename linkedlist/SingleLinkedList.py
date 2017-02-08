# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 10:42:00 2016

@author: arnab
"""
class Node(object):
    def __init__(self, data = None):
        self.val = data
        self.next = None
    
    def __repr__(self):
        return str(self.val)

class SingleLinkedList(object):
    def __init__(self, iterable = []):
        self.head = None
        self.size = 0
        for item in iterable:
            self.insert(item)

    def __repr__(self):
        curr, nodes = self.head, []
        while curr:
            nodes.append(str(curr))
            curr = curr.next
        return "->".join(nodes)
    
    def length(self):
        return self.size
    
    def search(self, key):
        curr = self.head
        while curr and curr.val != key:
            curr = curr.next
        if curr is None:
            raise ValueError("key searched is not in list.")
        return curr

    def insert(self, data):
        tmp = Node(data)
        tmp.next = self.head
        self.head = tmp
        self.size += 1
    
    def delete(self, key):
        prev = None
        curr = self.head
        while curr and curr.val != key:
            prev = curr
            curr = curr.next
        if curr is None:
            raise ValueError("key to be deleted is not in list")
        if prev is None:
            self.head = curr.next
        else:
            prev.next = curr.next
        self.size -= 1
        curr.next = None

    def removeNthFromEnd(self, n):
        # Assume n is always valid
        prev,curr,front = self.head,self.head,self.head
        for i in xrange(1,n):
            front = front.next
        
        while front.next:
            front = front.next
            prev = curr
            curr = curr.next
        if curr == self.head:
            self.head = curr.next
        else:
            prev.next = curr.next
        curr.next = None

    def getHead(self):
        return self.head
    
    def getTail(self):
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        return tmp
    
    def reverse(self):
        prev, curr = None, self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

if __name__ == '__main__':
    list1 = SingleLinkedList(range(0, 100, 10))
    print (list1)
    size = list1.size
    print (size)
#    print (list1)
#    print (list1.search(50))
#    list1.delete(50)
#    print (list1)
#    list1.reverse()
#    print (list1)
    list1.removeNthFromEnd(size)
    print (list1)
