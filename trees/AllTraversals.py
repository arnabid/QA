# -*- coding: utf-8 -*-
"""
Created on Sat May 27 08:07:29 2017

@author: arnab
"""

"""
preorder = reverse(postorder')

postorder = reverse(preorder')

inorder = reverse(inorder')

* ' indicates that the right child of a node is visited 
before the left child.
"""

"""
Recursive solutions
"""
# Inorder: LC, root, RC
def traverseInOrder(root):

    if root:
        traverseInOrder(root.left)
        print(root.val),
        traverseInOrder(root.right)

# Preorder: root, LC, RC
def traversePreOrder(root):

    if root:
        print(root.val),
        traversePreOrder(root.left)
        traversePreOrder(root.right)

# Postorder: LC, RC, root
def traversePostOrder(root):

    if root:
        traversePostOrder(root.left)
        traversePostOrder(root.right)
        print(root.val),



"""
Iterative solutions using DFS
"""

#############################################################
# preOrder - print node when you visit it
# in order of preference
def preorderTraversal1(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []
    
    stack, pre_ordered_list = [root], []
    
    while stack:
        v = stack.pop()
        pre_ordered_list.append(v.val)
        if v.right:
            stack.append(v.right)
        if v.left:
            stack.append(v.left)
    return pre_ordered_list


def preorderTraversal12(root):
    stack = []
    while True:
        while root:
            stack.append(root)
            print (root.val),
            root = root.left
        if stack:
            root = stack.pop().right
        else:
            break


def preorderTraversal3(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []
    
    stack, pre_ordered_list = [root], [root.val]
    visited = set([root])
    
    while stack:
        v = stack[-1]
        if v.left and v.left not in visited:
            stack.append(v.left)
            visited.add(v.left)
            pre_ordered_list.append(v.left.val)
        elif v.right and v.right not in visited:
            stack.append(v.right)
            visited.add(v.right)
            pre_ordered_list.append(v.right.val)
        else:
            stack.pop()
    return pre_ordered_list


###############################################################


# postOrder - print node when you backtrack from it
def postorderTraversal1(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []
    
    stack, post_ordered_list = [root], []
    visited = set([root])
    
    while stack:
        v = stack[-1]
        if v.left and v.left not in visited:
            stack.append(v.left)
            visited.add(v.left)
        elif v.right and v.right not in visited:
            stack.append(v.right)
            visited.add(v.right)
        else:
            post_ordered_list.append(stack.pop().val)
    return post_ordered_list


def postorderTraversal2(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []
    
    stack, post_ordered_list = [root], []
    visited = set()
    
    while stack:
        v = stack[-1]
        ad = True # flag to indicate if all children of this node are visited
        if v.right and v.right not in visited:
            stack.append(v.right)
            visited.add(v.right)
            ad = False
        if v.left and v.left not in visited:
            stack.append(v.left)
            visited.add(v.left)
            ad = False
        if ad:
            post_ordered_list.append(stack.pop().val)
    return post_ordered_list


# inOrder - print node when you backtrack
# also check if right child has been visited - if not
# add to stack
def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []
    
    stack, in_ordered_list = [root], []
    visited = set([root])
    
    while stack:
        v = stack[-1]
        if v.left and v.left not in visited:
            stack.append(v.left)
            visited.add(v.left)
        else:
            v = stack.pop()
            in_ordered_list.append(v.val)
            if v.right and v.right not in visited:
                stack.append(v.right)
                visited.add(v.right)
    return in_ordered_list

# another way to print inorder iteratively
def printInorderIterative(root):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if stack:
            root = stack.pop()
            print (root.val),
            root = root.right
        else:
            break


def levelOrderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    
    level_ordered_list = [[root.val]]
    cl = [root]
    
    while True:
        nl, vals = [], []
        for node in cl:
            if node.left:
                nl.append(node.left)
                vals.append(node.left.val)
            if node.right:
                nl.append(node.right)
                vals.append(node.right.val)
        if nl:
            level_ordered_list.append(vals)
            cl = nl
        else:
            break
