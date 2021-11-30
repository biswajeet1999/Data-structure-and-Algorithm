class Node:
   def __init__(self, key):
      self.key = key
      self.left = self.right = None


# O(n) time | O(h) space
def getLargestBst(root: Node):
   if root is None:
      # (size of bst, bst or not) 
      return (0, True)

   leftBSTSize, isLeftBst = getLargestBst(root.left)
   rightBSTSize, isRightBst = getLargestBst(root.right)
   if isLeftBst and isRightBst:
      isRootedBst = True
      if root.left and root.left.key > root.key:
         isRootedBst = False
      if root.right and root.right.key > root.key:
         isRootedBst = False
      if isRootedBst is False:
         return (max(leftBSTSize, rightBSTSize), False)
      return (leftBSTSize + 1 + rightBSTSize, True)

   return (max(leftBSTSize, rightBSTSize), False)
      

root = Node(60)
root.left = Node(65)
root.right = Node(70)
root.left.left = Node(50)
print(getLargestBst(root)[0])