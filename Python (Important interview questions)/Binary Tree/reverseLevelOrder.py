class Node:
   def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None

def levelOrder(root: Node):
   queue = []
   curLevel = []
   resultStack = []
   queue.append(root)
   queue.append(None) # act as a level delimeter
   while len(queue) > 0:
      curNode = queue.pop(0)
      if curNode is None:
         print()
         resultStack.append(curLevel)
         curLevel = []
         if len(queue) > 0: queue.append(None)
         continue
      curLevel.append(curNode.value)
      if curNode.left:
         queue.append(curNode.left)
      if curNode.right:
         queue.append(curNode.right)
   return resultStack[::-1]



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

target = root.right.left
printTree(root)
print(levelOrder(root))