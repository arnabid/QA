# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 16:39:26 2017

@author: arnab
"""

"""
heap - array implementation with 1 based indexing

Notes:
# nodes = n
# internal nodes = floor(n/2)
# leaves = n - internal nodes


Consider a heap of height 'h'
Till the level h-1, the heap is a complete binary tree with 
internal nodes = leaves - 1

After that, if the internal nodes increase by x, the can leaves increase
by x or x-1

At the end, the internal nodes <= leaves
If they are less, they are less by 1
so the number of internal nodes  = floor(n/2)
"""

def findMin(heap):
    """ returns minimum element in the heap
    returns None if heap is empty """
    if len(heap) <= 1: # first element in heap[] is 0
        return None
    else:
        return heap[1]

def heapify(i, heap):
    """ perform heapify at index i
    the 2 sub-trees rooted at index i should be heaps
    """
    if 2*i > len(heap) - 1:
        return
    lc, rc = float('inf'), float('inf')
    lc = heap[2*i]
    if 2*i + 1 <= len(heap) - 1:
        rc = heap[2*i+1]
    
    if heap[i] > lc and lc <= rc: # swap with left child
        heap[i], heap[2*i] = heap[2*i], heap[i]
        heapify(2*i, heap)
    elif heap[i] > rc and rc < lc: # swap with right child
        heap[i], heap[2*i + 1] = heap[2*i + 1], heap[i]
        heapify(2*i + 1, heap)

def deleteMin(heap):
    """ deletes and returns the minimum element in the heap,
    returns None if the heap is empty """
    n = len(heap)
    if n > 2:
        mn = heap[1]
        heap[1] = heap.pop()
        heapify(1, heap)
        return mn
    elif n > 1:
        return heap.pop()
    else:
        return None

def buildHeap(heap):
    """ arranges the items in heap into a min-heap structure, initial
    heap creation """
    heap.insert(0,0)
    n = len(heap) - 1
    i = n/2
    while i > 0:
        heapify(i, heap)
        i -= 1

def insertHeap(x, heap):
    """ inserts item x in the heap, maintaining the heap invariant """

    # check if heap is empty
    if not heap:
        heap += [0,x]
        return

    heap.append(x)
    index = len(heap) - 1
    while index > 1 and heap[index/2] > heap[index]: # parent > child
        heap[index/2] , heap[index] = heap[index], heap[index/2]
        index = index/2

def deleteItem(x, heap):
    """ deletes the first occurence of x from the heap """
    if x not in heap:
        return

    i = heap.index(x) # finds the first occurence of x in heap
    if i == len(heap) - 1: # if last item in heap is deleted
        heap.pop()
        return

    heap[i] = heap.pop()
    if i == 1: # if first item in heap is deleted
        heapify(i, heap)
        return

    pindex = i/2
    if heap[pindex] > heap[i]:
        while pindex >= 1 and heap[pindex] > heap[i]:
            heap[pindex], heap[i] = heap[i], heap[pindex]
            i = pindex
            pindex = i/2
        return
    else:
        heapify(i, heap)


if __name__ == '__main__':
    # inout array with the initial heap elements
    heap = map(int, raw_input().strip().split(" "))
    
    # build the heap
    buildHeap(heap)
    print (heap)
    
    # insert element x in the heap
    x = int(raw_input())
    insertHeap(x, heap)
    
    # delete the minimum element from heap
    print (deleteMin(heap))
    print (heap)
    
    # delete item from the heap
    deleteItem(13, heap)
    print (heap)