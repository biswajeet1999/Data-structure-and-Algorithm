class Node:
   def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None
      self.isVisited = False

def exploreSubTree(root, k):
   if root and not root.isVisited:
      root.isVisited = True
      if k == 0:
         print(root.value)
         return
      exploreSubTree(root.left, k - 1)
      exploreSubTree(root.right, k - 1)


def kthDistanceNodes(root, target, k):
   if root:
      if root.value == target.value:
         root.isVisited = True
         exploreSubTree(root.left, k - 1)
         exploreSubTree(root.right, k - 1)
         return k-1
      else:
         k1 = kthDistanceNodes(root.left, target, k)
         k2 = kthDistanceNodes(root.right, target, k)
         if (k1 == None or k1 < 0) and (k2 == None or k2 < 0):
            return None

         currentK = k1 if k2 is None else k2
         print('test', root.value, currentK, root.isVisited)
         exploreSubTree(root, currentK)
         return currentK - 1
         
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
# printTree(root)
# print(root.value, target.value)
kthDistanceNodes(root, target, 1)