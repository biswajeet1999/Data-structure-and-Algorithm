class Node:
   def  __init__(self, val):
      self.val = val
      self.left = None
      self.right = None

def largestSumSubtree(root: Node):
   maxSum = [-99999999]
   largestSumSubtreeUtil(root, maxSum)
   return maxSum[0]

def largestSumSubtreeUtil(root, maxSum):
   if root == None:
      return 0
   
   leftSubTreeSum = largestSumSubtreeUtil(root.left, maxSum)
   rightSubTreeSum = largestSumSubtreeUtil(root.right, maxSum)

   curSubTreeSum = leftSubTreeSum + root.val + rightSubTreeSum
   maxSum[0] = max(curSubTreeSum, maxSum[0])

   return curSubTreeSum


root = Node(1) 
root.left = Node(-2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(-6) 
root.right.right = Node(2) 
print(largestSumSubtree(root))
