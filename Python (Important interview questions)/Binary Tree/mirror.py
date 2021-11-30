class Node:
   def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None
      self.isVisited = False

# O(n) time | O(n) space
# dfs| preorder traversal method
def mirror(root: Node):
   if root is None:
      return None
   newNode = Node(root.value)
   newNode.right = mirror(root.left)
   newNode.left = mirror(root.right)
   return newNode
         
def printTree(root, dist = 0):
   if root == None:
      return
   printTree(root.right, dist + 10)
   print(" "*dist, root.value)
   printTree(root.left, dist + 10)

# Note:- we can do this using level order traversal method also by mentaining 2 queue i.e. one for original tree and 2nd for newly created tree
# we pop node from both the queue in each iteration and create new left and right node and insert into new node in reverse order

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
printTree(root)
printTree(mirror(root))

