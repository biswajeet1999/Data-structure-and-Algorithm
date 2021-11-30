class Node:
   def __init__(self, key):
      self.data = key
      self.left = None
      self.right = None

# O(n) time | O(h) space
def isSumTree(root: Node):
   if(root is None):
      #      (sum of the subtree, isBalanced or not)  
      return (0, True)
   if (root.left is None or root.right is None):
      return (root.data, True)
   (leftTreeSum, leftTreeIsBalanced) = isSumTree(root.left)
   (rightTreeSum, rightTreeIsBalanced) = isSumTree(root.right)
   if leftTreeIsBalanced and rightTreeIsBalanced and leftTreeSum + rightTreeSum == root.data:
      return (leftTreeSum + rightTreeSum + root.data, True)
   else:
      return (None, False)

root = Node(3)
root.left = Node(1)
root.right = Node(2)
print(isSumTree(root))

root = Node(10)
root.left = Node(20)
root.left.left = Node(10)
root.left.right = Node(10)
root.right = Node(30)
print(isSumTree(root))