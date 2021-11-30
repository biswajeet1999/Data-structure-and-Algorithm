class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)

# O(N) Time | O(h) space
def inOrder(tree, array = []):
    if tree is not None:
        inOrder(tree.left, array)
        array.append(tree.key)
        inOrder(tree.right, array)
    return array


# O(N) Time | O(h) space
def preOrder(tree, array = []):
    if tree is not None:
        array.append(tree.key)
        inOrder(tree.left, array)
        inOrder(tree.right, array)
    return array

# O(N) Time | O(h) space
def postOrder(tree, array = []):
    if tree is not None:
        inOrder(tree.left, array)
        inOrder(tree.right, array)
        array.append(tree.key)
    return array



class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        self.root.insert(key)





tree = BinarySearchTree()

tree.insert(10)
tree.insert(5)
tree.insert(2)
tree.insert(1)
tree.insert(5)
tree.insert(15)
tree.insert(13)
tree.insert(22)
tree.insert(14)


print(inOrder(tree.root))