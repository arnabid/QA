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
# Inorder LC, root, RC
def traverseInOrder(root):

    if root:
        traverseInOrder(root.left)
        print(root.val),
        traverseInOrder(root.right)

# Preorder root, LC, RC
def traversePreOrder(root):

    if root:
        print(root.val),
        traversePreOrder(root.left)
        traversePreOrder(root.right)

# Postorder LC, RC, root
def traversePostOrder(root):

    if root:
        traversePostOrder(root.left)
        traversePostOrder(root.right)
        print(root.val),



"""
Iterative solutions using DFS
"""

# preOrder - print node when you visit it
def preorderTraversal(root):
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

# another way to print pre-order iteratively
def printPreorderIterative(root):
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


# postOrder - print node when you backtrack from it
def postorderTraversal(root):
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
