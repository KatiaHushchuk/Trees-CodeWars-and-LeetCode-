class Node:
    def __init__(self, value, left, right):
        self.data = value
        self.left = left
        self.right = right

def pre_order(node):
    if not node:
        return []
    res = []
    res.append(node.data)
    res += pre_order(node.left)
    res += pre_order(node.right)
    return res

def in_order(node):
    if not node:
        return []
    res = []
    res += in_order(node.left)
    res.append(node.data)
    res += in_order(node.right)
    return res

def post_order(node):
    if not node:
        return []
    res = []
    res += post_order(node.left)
    res += post_order(node.right)
    res.append(node.data)
    return res
