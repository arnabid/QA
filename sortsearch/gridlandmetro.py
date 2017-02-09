# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:42:56 2016

@author: arnab
"""

"""
problem: https://www.hackerrank.com/challenges/gridland-metro
"""

from collections import Counter

if __name__ == '__main__':
    n,m,k = map(int, raw_input().strip().split(" "))    
    rows = Counter()
    
    for _ in xrange(k):
        r, c1, c2 = map(int, raw_input().strip().split(" "))
        if r in rows:
            rows[r] += [(c1,-1), (c2,1)]
        else:
            rows[r] = [(c1,-1), (c2,1)]
    
    total = 0
    for key in rows:
        rows[key].sort(key = lambda x: (x[0], x[1]))
        currentopen, start, stop, freecells = 0,0,0,m
        """
        currentopen - number of trains currently scanned
        freecells - numbers of cells that are not covered by train tracks
        """
        for event in rows[key]:
            if currentopen == 0:
                start = event[0]
            if event[1] == -1:
                currentopen += 1
            else:
                currentopen -= 1
            if currentopen == 0:
                stop = event[0]
                freecells -= (stop - start + 1)
        total += freecells
    total += (n-len(rows))*m
    print (total)


        