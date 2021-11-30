class Node:
   def __init__(self, key):
      self.key = key
      self.left = self.right = None


def binaryTreeToBST(root: Node):
   if root is None:
      return
   inorderLst = []
   inorder(root, inorderLst)
   inorderLst.sort()
   populateTree(root, inorderLst, [0])

def populateTree(root, inorderLst, curPtr):
   if root is None:
      return
   populateTree(root.left)
   root.key = inorderLst[curPtr[0]]
   curPtr[0] += 1
   populateTree(root.right)


def inorder(root, inorderLst):
   if root is None:
      return None
   inorderLst.append(root.key)
   inorder(root.left, inorderLst)
   inorder(root.right, inorderLst)
   


