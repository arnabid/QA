class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def serializeBFS(root):
    """
    returns dictionary with key = index in the tree; value = node value
    """
    if root is None: return {}

    treedic = {}
    clevel = [(1,root)]
    while clevel:
        nlevel = []
        for index, node in clevel:
            treedic[index] = node.val
            if node.left:
                nlevel.append((index*2, node.left))
            if node.right:
                nlevel.append((index*2 + 1, node.right))
        clevel = nlevel
    return treedic

def deserialize(treedic):
    if not treedic: return None
    root = Node(treedic[1])
    clevel = [(1, root)]
    while clevel:
        nlevel = []
        for index, node in clevel:
            if index*2 in treedic:
                node.left = Node(treedic[index*2])
                nlevel.append((index*2, node.left))
            if index*2 + 1 in treedic:
                node.right = Node(treedic[index*2+1])
                nlevel.append((index*2+1, node.right))
        clevel = nlevel
    return root


def check2TreesIdentical(r1, r2):
    if r1 is None and r2 is None:
        return True
    if r1 is None or r2 is None:
        return False
    return r1.val == r2.val and \
    check2TreesIdentical(r1.left, r2.left) and \
    check2TreesIdentical(r1.right, r2.right)

# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(5)
    root.right.right.left = Node(6)
    root.right.left.right = Node(8)

    droot = deserialize(serializeBFS(root))
    print (check2TreesIdentical(root, droot))