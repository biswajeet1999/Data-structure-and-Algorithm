class Node:
   def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None

# O(n) time | O(2^(maxLevel)) space
# level order traversal
def areLeafsInSameLevel(root):
   if root is None:
      return True
   queue = []
   queue.append(root)
   queue.append(None)
   maxLevelOfLeafNode = None
   currentLevel = 0

   while len(queue) > 0:
      curNode = queue.pop(0)

      if curNode is None:
         currentLevel += 1
         if len(queue) > 0:
            queue.append(None)
         continue

      if curNode.left is None and curNode.right is None:
         if maxLevelOfLeafNode == None:
            maxLevelOfLeafNode = currentLevel
         if maxLevelOfLeafNode != currentLevel:
            return False

      if(curNode.left):
         queue.append(curNode.left)
      if(curNode.right):
         queue.append(curNode.right)

   return True

root = Node(3)
root.left = Node(1)
root.right = Node(2)
print(areLeafsInSameLevel(root))

root = Node(10)
root.left = Node(20)
root.left.left = Node(10)
root.left.right = Node(10)
root.right = Node(30)
print(areLeafsInSameLevel(root))