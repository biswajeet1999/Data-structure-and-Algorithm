class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data == self.data:
            print('Duplicate key')
        elif data < self.data and self.left == None:
            self.left = Node(data)
        elif data > self.data and self.right == None:
            self.right = Node(data)
        elif data < self.data:
            self.left.insert(data)
        else:
            self.right.insert(data)
    
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data, end='  ')
        if self.right is not None:
            self.right.inorder()

    def printTree(self, gap = 0):
        if self.right is not None:
            self.right.printTree(gap + 5)
        print('{}{}'.format(' '*gap, self.data))
        if self.left is not None:
            self.left.printTree(gap + 5)
        
    def flip(self):
        temp = self.left
        self.left = self.right
        self.right = temp

        if self.left is not None:
            self.left.flip()
        if self.right is not None:
            self.right.flip()


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            newNode = Node(data)
            self.root = newNode
        else:
            self.root.insert(data)
    
    def inorder(self):
        if self.root is not None:
            self.root.inorder()
    
    def printTree(self, gap = 0):
        if self.root is not None:
            self.root.printTree(gap = 0)
    
    def flip(self):
        if self.root is not Node:
            self.root.flip()

if __name__ == '__main__':
    Tree = BST()
    Tree.insert(6)
    Tree.insert(3)
    Tree.insert(1)
    Tree.insert(5)
    Tree.insert(8)
    Tree.insert(7)
    Tree.insert(9)
    Tree.inorder()
    print()
    Tree.printTree()
    print('Tree after flip')
    Tree.flip()
    Tree.printTree()

