# Avg:- O(nlogn) time | O(n) space
# worst:- O(n^2) time | O(n) space
# we can use avl tree to get worstcase O(nlogn) time

class Node:
   def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.count = 0

def insert(root, value):
   if root == None:
      return Node(value)
   if root.value > value:
      root.count += 1
      root.left = insert(root.left, value)
   else:
      root.right = insert(root.right, value)
   return root

def buildTree(arr):
   root = None
   for ele in arr:
      root = insert(root, ele)
   return root

def getCount(root):
   if root == None:
      return 0
   return root.count + getCount(root.left) + getCount(root.right)

def inversionCount(arr):
   bst = buildTree(arr)
   return getCount(bst)


arr = [1, 20, 6, 4, 5]
print(inversionCount(arr))