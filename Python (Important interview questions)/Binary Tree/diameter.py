class Node:
   def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None

# O(n) time | O(1) space
# def maxPath(root: Node):
#    if root is None:
#       return 0
#    return 1 + max(maxPath(root.left), maxPath(root.right))

# O(n^2) time | O(n) sp1ace
# def diameter(root: Node):
#    if root is None:
#       return 0
#    longestPathIncludingRoot = 1 + maxPath(root.left) + maxPath(root.right)
#    leftSubTreeDiameter = diameter(root.left)
#    rightSubTreeDiameter = diameter(root.right)
#    return max(longestPathIncludingRoot, leftSubTreeDiameter, rightSubTreeDiameter)


def diameter(root: Node):
   if root is None:
      # (height, diameter)
      return (0, 0)

   lh, ld = diameter(root.left)
   rh, rd = diameter(root.right)
   maxDiameter = max(ld, rd, 1 + lh + rh)
   curHeight = 1 + max(lh, rh)
   return (curHeight, maxDiameter)


def printTree(root, dist = 0):
   if root == None:
      return
   printTree(root.right, dist + 10)
   print(" "*dist, root.value)
   printTree(root.left, dist + 10)


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)

root.left.left.left.left = Node(12)
root.left.right.right.right = Node(13)


printTree(root)
print(diameter(root))