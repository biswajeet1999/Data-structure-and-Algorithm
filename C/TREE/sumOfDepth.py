class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if(data == self.data):
            print('Duplicate key not allowed')
            return
        elif(data < self.data and self.left is None):
            self.left = Node(data)
        elif(data > self.data and self.right is None):
            self.right = Node(data)
        elif(data > self.data):
            self.right.insert(data)
        else:
            self.left.insert(data)

    def sumOfDepthOfTree(self, currentDepth=0):
        if(self.left is None and self.right is None):
            return currentDepth
        if self.left is not None:
            leftSubTreeDepth = self.left.sumOfDepthOfTree(currentDepth + 1)
        if self.right is not None:
            rightSubTreeDepth = self.right.sumOfDepthOfTree(currentDepth + 1)
        return currentDepth + leftSubTreeDepth + rightSubTreeDepth

    def sumOfDepthOfTreeRootedEachNode(self, currentDepth=0):
        if(self.left is None and self.right is None):
            return currentDepth

        if self.left is not None:
            leftSubTreeDepth = self.left.sumOfDepthOfTreeRootedEachNode(currentDepth + 1)
            leftRootedTreeDepth = self.left.sumOfDepthOfTreeRootedEachNode(0)
            print("(%d  %d)" %(self.left.data, leftRootedTreeDepth))

        if self.right is not None:
            rightSubTreeDepth = self.right.sumOfDepthOfTreeRootedEachNode(currentDepth + 1)
            rightRootedTreeDepth = self.right.sumOfDepthOfTreeRootedEachNode(0)
            print("(%d  %d)" %(self.right.data, rightRootedTreeDepth))

        return currentDepth + leftSubTreeDepth + rightSubTreeDepth + leftRootedTreeDepth + rightRootedTreeDepth

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if(self.root == None):
            self.root = Node(data)
        else:
            self.root.insert(data)

    def sumOfDepthOfTree(self):
        if self.root == None:
            return 0
        return self.root.sumOfDepthOfTree()

    def sumOfDepthOfTreeRootedEachNode(self):
        if self.root == None:
            return 0
        return self.root.sumOfDepthOfTreeRootedEachNode()


t = Tree()
t.insert(10)
t.insert(5)
t.insert(15)
t.insert(2)
t.insert(7)
t.insert(12)
t.insert(16)
t.insert(1)
t.insert(3)
print(t.sumOfDepthOfTree())
print(t.sumOfDepthOfTreeRootedEachNode())
