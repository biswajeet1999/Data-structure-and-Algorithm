class Node:
   def __init__(self, key):
      self.value = key
      self.left = self.right = None
      self.isVisited = False

def exploreDown(root: Node, k):
   if root == None:
      return
   if k < 0:
      return 
   if root.isVisited == True:
      return
   root.isVisited = True
   if k == 0:
      print(root.value)
      return
   exploreDown(root.left, k - 1)
   exploreDown(root.right, k - 1)


def findKDistanceNodes(root: Node, target: Node, k):
   if root == None:
      return -1
   
   if root == target:
      exploreDown(root, k)
      return k - 1

   k1 = findKDistanceNodes(root.left, target, k)
   if k1 >= 0:
      exploreDown(root, k1)
      return k1 - 1
   k2 = findKDistanceNodes(root.right, target, k)
   if k2 >= 0:
      exploreDown(root, k2)
      return k2 - 1
   return -1
   
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
target = root.left.right
findKDistanceNodes(root, target, 2)