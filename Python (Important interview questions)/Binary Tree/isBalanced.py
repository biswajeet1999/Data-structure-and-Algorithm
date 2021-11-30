class Node:
   def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None

# O(n) time | O(n) space
def isBalanced(root: Node):
   if root is None:
      return (True, -1)
   isLeftSubtreeBalanced, leftSubTreeHeight = isBalanced(root.left)
   isRightSubtreeBalanced, rightSubTreeHeight = isBalanced(root.right)
   return (isLeftSubtreeBalanced and isRightSubtreeBalanced and abs(leftSubTreeHeight - rightSubTreeHeight) <= 1, 
            1 + max(leftSubTreeHeight, rightSubTreeHeight))


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)

root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)
print(isBalanced(root))