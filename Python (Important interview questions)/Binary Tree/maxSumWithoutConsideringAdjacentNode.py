class Node:
   def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None

def maxSum(root: Node):
   return max(maxSumUtil(root))

def maxSumUtil(root: Node):
   if root == None:
      return (0, 0)
   
   considerLeftChild, withoutConsiderLeftChild = maxSumUtil(root.left)
   considerRightChild, withoutConsiderRightChild = maxSumUtil(root.right)

   totalSumByConsideringBothChild = considerLeftChild + considerRightChild
   totalSumConsideringRootNode = root.value + withoutConsiderLeftChild + withoutConsiderRightChild

   return (totalSumConsideringRootNode, totalSumByConsideringBothChild)

root = Node(1);
root.left = Node(2);
root.right = Node(3);
root.right.left = Node(4);
root.right.right = Node(5);
root.left.left = Node(1);
print(maxSum(root))