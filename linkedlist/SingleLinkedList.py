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
        """ returns first node with val = key; null otherwise """
        curr = self.head
        while curr and curr.val != key:
            curr = curr.next
        return curr

    def insert(self, data):
        """ inserts node at front of the linked list O(1) """
        tmp = Node(data)
        tmp.next = self.head
        self.head = tmp
        self.size += 1
    
    def delete(self, key):
        """ deletes the first node with val = key """
        
        tmp = self.head
        
        """ if the first node has val = key """
        if tmp and tmp.val == key:
            self.head = tmp.next
            tmp = None
            return

        prev = None
        while tmp and tmp.val != key:
            prev = tmp
            tmp = tmp.next
        
        """ node with val = key not found """
        if tmp is None:
            return
            
        prev.next = tmp.next
        tmp = None
        self.size -= 1

    def removeNthFromEnd(self, head, n):
        if head is None:
            return None
        tmp = head
        for i in xrange(n):
            tmp = tmp.next
        
        if tmp is None:
            return head.next
        
        stop = head
        while tmp.next:
            tmp = tmp.next
            stop = stop.next

        stop.next = stop.next.next
        return head

    def getHead(self):
        """ returns the first node """
        return self.head
    
    def getTail(self):
        """ returns the last node """
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        return tmp
    
    def reverse(self):
        """ reverses a linked list in place """
        prev, curr = None, self.head
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
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
