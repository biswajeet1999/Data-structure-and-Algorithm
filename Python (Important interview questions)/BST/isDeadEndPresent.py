class Node:
   def __init__(self, key):
      self.key = key
      self.left = self.right = None



# find all leaf node the  for leaf node x check whether x -1 and x + 1 present in the tree or not if both are present then that node is dead end
def isDeadEndPresent(root: Node):
   leafNodes = {}
   allNodes = {}
   inorder(root, leafNodes, allNodes)
   for key in leafNodes.keys():
      prevVal = key - 1
      nextVal = key + 1
      if (prevVal == 0 or prevVal in allNodes) and (nextVal in allNodes):
         return True
   return False

def inorder(root: Node, leafNodes, allNodes):
   if root is None:
      return
   inorder(root.left, leafNodes, allNodes)
   allNodes[root.key] = root
   if root.left is None and root.right is None:
      leafNodes[root.key] = root
   inorder(root.right, leafNodes, allNodes)


def insert(root, key):
   if root is None:
      return Node(key)
   if key < root.key:
      root.left = insert(root.left, key)
   else:
      root.right = insert(root.right, key)
   return root

root = None
root = insert(root, 8)
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 7)
root = insert(root, 11)
root = insert(root, 4)
print(isDeadEndPresent(root))