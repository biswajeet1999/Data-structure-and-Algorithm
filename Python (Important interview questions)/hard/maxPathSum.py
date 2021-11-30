class Node:
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None


# O(n) time | O(d) space
# def getBranchSum(root):
#    return 0 if root is None else root.value + max(getBranchSum(root.left), getBranchSum(root.right))
# # O(n^2) time | O(d) space
# def maxPathSum(root):
#    if root == None:
#       return 0
#    leftBranchSum = getBranchSum(root.left)
#    rightBranchSum = getBranchSum(root.right)
#    leftPathSum = maxPathSum(root.left)
#    rightPathSum = maxPathSum(root.right)
   
#    childMaxPathSum = max(leftPathSum, rightPathSum)
#    currentPathSum = max(root.value, root.value + leftBranchSum + rightBranchSum)
#    return max(childMaxPathSum, max(currentPathSum, root.value + max(leftBranchSum, rightBranchSum)))

# O(n) time | O(d) space
def maxPathSum(root):
   if root == None:
      return (0, 0)
   leftBranchSum, leftPathSum = maxPathSum(root.left)
   rightBranchSum, rightPathSum = maxPathSum(root.right)

   childMaxBranchSum = max(leftBranchSum, rightBranchSum)
   maxBranchSum = max(root.value, root.value + childMaxBranchSum)
   childMaxPathSum = max(leftPathSum, rightPathSum)
   pathSum = max(childMaxPathSum, maxBranchSum, leftBranchSum + root.value + rightBranchSum)
   return (maxBranchSum, pathSum)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(maxPathSum(root))