# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 07:58:38 2016

@author: arnab
"""

"""
Design a stack to support the folllowing operations:
push, pop, min/max/average??

Each query is of the form:
1 x  -Push x into the stack.
2    -Pop from the stack.
3    -Print the maximum item present in the stack.
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
            if stack[-1] == stackm[-1]:
                stackm.pop()
            stack.pop()
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
        else: # return average of elements in the stack
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
        if bars[i] >= stack[-1][0]: 
            stack.append((bars[i], i))
        else:
            """keep popping all bigger bars to the left,
            and bar[i] starts from the last popped index
            """
            temp = None
            while stack and bars[i] < stack[-1][0]:
                temp = stack.pop()
                ans = max(ans, (i-temp[1])*temp[0])
            stack.append((bars[i], temp[1]))

    # pop the remaining items in stack
    while stack:
        temp = stack.pop()
        ans = max(ans, (n-temp[1])*temp[0])
    return (ans)


"""
Poisonous plants question
https://www.hackerrank.com/challenges/poisonous-plants
status = [...,(i,j),...]
The status of each plant after the program finishes is expressed as a tuple (i,j)
i -> 0/1 : dead/alive
j -> day plant dies
"""
if __name__ == '__main__':
    n = int(raw_input())
    plants = map(int, raw_input().strip().split(" "))
    
    ans, stack, status = 0, [(plants[0],0)], [(1,0)]
    for i in xrange(1,n):
        if plants[i] > stack[-1][0]:
            stack.append((plants[i], 1))
            status.append((0,1))
            ans = max(ans, 1)
        else:
            # pop till a smaller plant is found; find the max number
            # of days these popped plants survived
            maxday = 0
            while stack and plants[i] <= stack[-1][0]:
                maxday = max(maxday, stack[-1][1])
                stack.pop()
            if not stack:
                stack.append((plants[i], 0))
                status.append((1,0))
            else:
                stack.append((plants[i], maxday+1))
                status.append((0,maxday+1))
                ans = max(ans, maxday+1)
    print (ans)
    print (status)


"""
given a permutation of integers from
1...n, check if it is a valid permutation
resulting from a sequence of stack operations
pop - prints the integer 
push - adds integer to stack
push can be done only in increasing order
"""

def checkSequence(arr):
    n = len(arr)
    lp, stack = 0, []
    for i in xrange(n):
        if arr[i] > lp:
            for e in xrange(lp+1, arr[i]): # no need to insert arr[i]
                stack.append(e)
            lp = arr[i]
        else:
            if arr[i] != stack[-1]:
                return False
            stack.pop()
    return True

