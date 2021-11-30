class Node:
   def __init__(self, key):
      self.data = key
      self.left = None
      self.right = None


def maxPathSum(root: Node):
   if root is None:
      #      sum, noOfNodes
      return (0, 0)
   
   (leftTreeMaxPathSum, noOfNodesInLeftTree) = maxPathSum(root.left)
   (rightTreeMaxPathSum, noOfNodesInRightTree) = maxPathSum(root.right)


   if noOfNodesInLeftTree > noOfNodesInRightTree:
      totalSum = root.data + leftTreeMaxPathSum
      totalNodes = noOfNodesInLeftTree + 1
   elif noOfNodesInLeftTree < noOfNodesInRightTree:
      totalSum = root.data + rightTreeMaxPathSum
      totalNodes = noOfNodesInRightTree + 1
   else:
      totalSum = root.data + max(rightTreeMaxPathSum, leftTreeMaxPathSum)
      totalNodes = noOfNodesInRightTree + 1

   return (totalSum, totalNodes)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(7)
root.left.right = Node(1)
root.right.left = Node(2)
root.right.right = Node(3)
root.left.right.left = Node(6)

print(maxPathSum(root))