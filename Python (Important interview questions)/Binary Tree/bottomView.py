class Node:
   def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None

# O(n) time | O(n) space
def bottomView(root: Node):
   horizontalHeights = {}
   populateHorizontalHeight(root, horizontalHeights)
   return horizontalHeights

def populateHorizontalHeight(root: Node, horizontalHeights, currHeight = 0):
   if root is None:
      return 
   horizontalHeights[currHeight] = root.value
   populateHorizontalHeight(root.left, horizontalHeights, currHeight-1)
   populateHorizontalHeight(root.right, horizontalHeights, currHeight+1)

# another approach
# find horizontal height of each and every node. now do level order traversal and maintain dictionary{height: node} and update height with
# the node which come late bcz the node which come late means that node pesent at bottom in that (horizontal height or vertical axis).

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
print(bottomView(root))