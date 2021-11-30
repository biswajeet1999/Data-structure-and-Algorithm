class Node:
   def __init__(self, key):
      self.key = key
      self.left = self.right = None


def buildTreeFromPreorder(preorder):
   return buildTreeHelper(preorder, [0], -float("inf"), float("inf"))

def buildTreeHelper(preorder,curPtr, minRange, maxRange):
   if curPtr[0] >= len(preorder):
      return None
   if preorder[curPtr[0]] < minRange or preorder[curPtr[0]] > maxRange:
      return None

   curNode = Node(preorder[curPtr[0]])
   curPtr[0] += 1
   curNode.left = buildTreeHelper(preorder, curPtr, minRange, curNode.key - 1)
   curNode.right = buildTreeHelper(preorder, curPtr, curNode.key + 1, maxRange)
   return curNode


def inorder(root):
   if root is None:
      return
   inorder(root.left)
   print(root.key)
   inorder(root.right)

root = buildTreeFromPreorder([10, 5, 1, 7, 40, 50])
inorder(root)
