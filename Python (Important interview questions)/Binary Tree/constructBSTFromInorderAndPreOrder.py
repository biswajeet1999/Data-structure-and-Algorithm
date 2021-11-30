class Node:
   def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None

def printTree(root, dist = 0):
   if root == None:
      return
   printTree(root.right, dist + 10)
   print(" "*dist, root.value)
   printTree(root.left, dist + 10)

def buildTree(inorder, preorder):
   return buildTreeHelper(inorder, 0, len(inorder)-1, preorder, 0, len(preorder)-1)

def buildTreeHelper(inorder, inorderStart, inorderEnd, preorder, preorderStart, preorderEnd):
   if preorderStart > preorderEnd or inorderStart > inorderEnd:
      return None
   rootVal = preorder[preorderStart]
   rootNode = Node(rootVal)
   rootValIdxInInorder = getRootIdxInInorder(rootVal, inorder, inorderStart, inorderEnd)
   rootNode.left = buildTreeHelper(inorder, inorderStart, rootValIdxInInorder - 1, preorder, preorderStart+1, preorderEnd)
   rootNode.right = buildTreeHelper(inorder, rootValIdxInInorder + 1, inorderEnd, preorder, preorderStart+1, preorderEnd) 
   return rootNode

def getRootIdxInInorder(rootVal, inorder, start, end):
   for i in range(start, end+1):
      if inorder[i] == rootVal:
         return i
   return -1

inorder = [1, 6, 8, 7]
preorder = [1, 6, 7, 8]

inorder = ['D', 'B', 'E', 'A', 'F', 'C']
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
root = buildTree(inorder, preorder)
printTree(root)

# this is wrong code