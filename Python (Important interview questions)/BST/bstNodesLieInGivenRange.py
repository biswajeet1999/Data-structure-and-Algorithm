class Node:
   def __init__(self, key):
      self.key = key
      self.left = self.right = None

# O(n) time  | O(n) space
def getBstNodesInARange(root: Node, minLimit, maxLimit):
   result = []
   getBstNodesHelper(root, result, minLimit, maxLimit)
   return result

def getBstNodesHelper(root, result, minLimit, maxLimit):
   if root is None:
      return
   
   if root.key >= minLimit and root.key <= maxLimit:
      result.append(root.key)
      getBstNodesHelper(root.left, result, minLimit, maxLimit)
      getBstNodesHelper(root.right, result, minLimit, maxLimit)
      return
   
   if root.key < minLimit:
      getBstNodesHelper(root.right, result, minLimit, maxLimit)
   else:
      getBstNodesHelper(root.left, result, minLimit, maxLimit)

root = Node(10)
root.left = Node(5)
root.right = Node(50)
root.left.left = Node(1)
root.right.left = Node(40)
root.right.right = Node(100)

print(getBstNodesInARange(root, 5, 45))