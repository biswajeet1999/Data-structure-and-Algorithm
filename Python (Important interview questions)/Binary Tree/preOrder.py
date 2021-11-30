class Node:
   def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None

# def preorder(root: Node):
#    if root is None:
#       return
#    print(root.value, end=" ")
#    preorder(root.left)
#    preorder(root.right)

def preorder(root: Node):
   stack = []
   curNode = root
   stack.append(root)
   while len(stack) > 0:
      curNode = stack.pop()
      print(curNode.value, end=" ")
      if curNode.right:
         stack.append(curNode.right)
      if curNode.left:
         stack.append(curNode.left)
      
      
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


preorder(root)