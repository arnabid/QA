# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 07:25:55 2017

@author: arnab
"""

"""
XML tree presentation
reference: https://discuss.leetcode.com/topic/52519/xml-tree-presentation
"""
class Node(object):
    def __init__(self, key=None):
        self.key = key
        self.val = None
        self.parent = None
        self.children = []

if __name__ == '__main__':
    input = []
    
    cn = Node("Dummy")
    for item in input:
        tag, content = item.strip().split(",")
        
        if tag == "inner":
            cn.val = content
        elif tag == "open":
            t = Node(content)
            t.parent = cn
            cn.children.append(t)
            cn = t
        else:
            cn = cn.parent
    return cn.children[0]
