class Node:
   def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None
      self.isVisited = False

# def inorder(root: Node):
#    if root is None:
#       return
#    inorder(root.left)
#    print(root.value, end=" ")
#    inorder(root.right)

def inorder(root: Node):
   stack = []
   curNode = root
   while True:
      while curNode:
         stack.append(curNode)
         curNode = curNode.left
      if len(stack) == 0:
         return
      curNode = stack.pop()
      print(curNode.value, end=" ")
      curNode = curNode.right
      
      
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


inorder(root)