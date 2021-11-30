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

    def inOrder(self):
        if self.left is not None:
            self.left.inOrder()
        print(self.key, end=" ")
        if self.right is not None:
            self.right.inOrder()

    def validateBst(self):
        if self.left is None and self.right is None:
            return True
        elif self.left is None:
            return self.key <= self.right.key and self.right.validateBst()
        elif self.right is None:
            return self.key > self.left.key and self.left.validateBst()
        elif self.left.key < self.key and self.right.key >= self.key :
            return self.left.validateBst() and self.right.validateBst()
        return False

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        self.root.insert(key)
    def inOrder(self):
        if self.root is not None:
            self.root.inOrder()
            print()

    def validateBst(self):
        if self.root is not None:
            return self.root.validateBst()
        return True


tree = BinarySearchTree()

tree.insert(10)
# true case
tree.insert(5)
tree.insert(2)
tree.insert(1)
tree.insert(5)
tree.insert(15)
tree.insert(13)
tree.insert(22)
tree.insert(14)

# flase case
# tree.root.left = Node(12)

tree.inOrder()

print(tree.validateBst())