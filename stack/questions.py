# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 07:58:38 2016

@author: arnab
"""

"""
Design a stack to support the folllowing operations:
push, pop, min/max/average??

You have an empty sequence, and you will be given  queries. Each query is one of these three types:
1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
"""

# find max in the stack
if __name__ == '__main__':
    stack, stackm = [], []
    T = int(raw_input())

    for _ in xrange(T):
        q = map(int, raw_input().strip().split(" "))
        if q[0] == 1: # push
            stack.append(q[1])
            if stackm:
                if q[1] >= stackm[-1]:
                    stackm.append(q[1])
            else:
                stackm.append(q[1])
                
        elif q[0] == 2: # pop
            v = stack.pop()
            if v == stackm[-1]:
                stackm.pop()
        else: # return max element in the stack
            print (stackm[-1])
 
# find the average in the stack           
if __name__ == '__main__':
    stack = []
    T = int(raw_input())

    total, n = 0, 0
    for _ in xrange(T):
        q = map(int, raw_input().strip().split(" "))
        if q[0] == 1: # push
            stack.append(q[1])
            total += q[1]
            n += 1
        elif q[0] == 2: # pop
            v = stack.pop()
            total -= v
            n -= 1
        else: # return average of lements in the stack
            print (total/float(n))

"""
Largest area in a histogram
https://www.hackerrank.com/challenges/largest-rectangle
"""
def largestArea(bars, n):
    ans, stack = 0, [(bars[0], 0)]
    
    for i in xrange(1,n):
        """
        if bar[i] > top of stack, this bar starts from index i
        """
        if bars[i] > stack[-1][0]: 
            stack.append((bars[i], i))
        else:
            """keep popping till you find a smaller bar or stack is empty,
            and bar[i] starts from the last popped index
            """
            while stack and bars[i] <= stack[-1][0]:
                temp = stack.pop()
                ans = max(ans, (i-temp[1])*temp[0])
                if not stack:
                    break
            stack.append((bars[i], temp[1]))

    # pop the remaining items in stack
    i = n
    while stack:
        temp = stack.pop()
        ans = max(ans, (i-temp[1])*temp[0])
    return (ans)



"""
Poisonous plants question
https://www.hackerrank.com/challenges/poisonous-plants
"""
if __name__ == '__main__':
    n = int(raw_input())
    plants = map(int, raw_input().strip().split(" "))
    
    ans, stack = 0, [(plants[0],0)]
    for plant in plants[1:]:
        temp = stack[-1]
        if plant > temp[0]:
            stack.append((plant, 1))
            ans = max(ans, 1)
        else:
            pr = temp[1]
            while stack and plant <= temp[0]:
                stack.pop()
                pr = max(pr, temp[1])
                if not stack:
                    break
                temp = stack[-1]
            if not stack:
                stack.append((plant, 0))
            else:
                stack.append((plant, pr+1))
                ans = max(ans, pr+1)
    print (ans)


"""
given a permutation of integers from
1...n, check if it is a valid permutation
resulting from a sequence of stack operations
pop - prints the integer 
push - adds integer to stack
push can be done only in increasing order
"""

if __name__ == '__main__':
    arr = map(int, raw_input().strip().split(" "))
    n = len(arr)
    
    stack, lastpushed = [], 0
    ans = True
    for i in xrange(n):
        if arr[i] > lastpushed:
            stack.extend(xrange(lastpushed+1, arr[i]+1))
            lastpushed = arr[i]
        if arr[i] != stack.pop():
            ans = False
            break
