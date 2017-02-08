# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 21:03:52 2016

@author: arnab
"""

"""
Tree traversals:

Pre-order traversal
===================

preorder(v):
  if v == null return
  else
     visit(v)
     preorder(v.leftchild())
     preorder(v.rigtchild())
  return

Post-order traversal
====================

postorder(v):
  if v == null return
  else
     postorder(v.leftchild())
     postorder(v.rightchild())
     visit(v)
  return

In-order traversal
==================

inorder(v):
  if v == null return
  else
     inorder(v.leftchild())
     visit(v)
     inorder(v.rightchild())
  return


Given preorder and inorder, we can uniquely determine the tree
Given postorder and inorder, we can uniquely determine the tree
Given preorder and postorder, we can uniquely determine the tree
given an extra condition that all the internal nodes have exactly 2 children

Solving problems on trees

Recursive solutions are simple but are not good for large problem instances.
Need iterative versions for such cases.

A recursive formulation, while the simplest, might quickly get us a 
stack overflow exception due to size of the call stack. Without using recursion,
we can keep all the data we need on the much larger heap.

Questions

Binary Search Tree
1) the common methods: search, insert, delete, findmin, findmax, successor, predecessor
2) is a binary tree a BST
3) sorted array to BST
4) modify BST such that each node is the sum of itself and all nodes greater than it
5) lowest common ancestor in a BST
6) find a pair with a given sum in a balanced BST
7) find if there is a triplet in a balanced BST that adds to zero
8) kth largest/smallest in a BST
9) given two arrays, do they represent the same BST?


"""