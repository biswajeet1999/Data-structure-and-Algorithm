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


# O(N) time | O(h) space
def invertBstRecursive(root):
    if root is None:
        return
    (root.left, root.right) = (root.right, root.left)
    invertBstRecursive(root.left)
    invertBstRecursive(root.right)

# O(N) time | O(h) space
def invertBstIterative(root):
    if root is None:
        return
    queue = [root]
    while(len(queue) > 0):
        currNode = queue.pop(0)
        (currNode.left, currNode.right) = (currNode.right, currNode.left)
        if currNode.left: queue.append(currNode.left)
        if currNode.right: queue.append(currNode.right)


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

invertBstRecursive(tree.root)
tree.inOrder()

invertBstIterative(tree.root)
tree.inOrder()
