class Node:
   def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None

# O(n) time | O(n) space
def topView(root: Node):
   horizontalHeights = {}
   populateHorizontalHeight(root, horizontalHeights)
   # level order traversal
   queue = []
   result = []
   maxHorizontalHeightTillNow = -float("inf")
   minHorizontalHeightTillNow =  float("inf")
   queue.append(root)

   while len(queue) > 0:
      curNode = queue.pop(0)
      if horizontalHeights[curNode] < minHorizontalHeightTillNow:
         result.append(curNode.value)
         minHorizontalHeightTillNow = horizontalHeights[curNode]
      elif horizontalHeights[curNode] > maxHorizontalHeightTillNow:
         result.append(curNode.value)
         maxHorizontalHeightTillNow = horizontalHeights[curNode]
      if curNode.left:
         queue.append(curNode.left)
      if curNode.right:
         queue.append(curNode.right)
   return result

def populateHorizontalHeight(root: Node, horizontalHeights, currHeight = 0):
   if root is None:
      return 
   horizontalHeights[root] = currHeight
   populateHorizontalHeight(root.left, horizontalHeights, currHeight-1)
   populateHorizontalHeight(root.right, horizontalHeights, currHeight+1)



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
print(topView(root))