# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 22:18:27 2017

@author: arnab
"""

"""
dictionary sorting
"""

d = {'B':5, 'a':2, 'S':12, 'f':10}

# sort d by keys and return the list of sorted keys
sorted(d)

# sort d by values and return a list of sorted keys
sorted(d, key = d.get)

# To get a list of tuples ordered by value
sorted(d.items(), key=lambda x:x[1])

# To get a list of tuples sorted by key
sorted(d.items(), key=lambda x:x[0])