class Node:
   def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None

# def postorder(root: Node):
#    if root is None:
#       return
#    postorder(root.left)
#    postorder(root.right)
#    print(root.value, end=" ")

def postorder(root: Node):
   stack1 = []
   stack2 = []
   curNode = root
   stack1.append(root)
   while len(stack1) > 0:
      curNode = stack1.pop()
      stack2.append(curNode.value)
      if curNode.left:
         stack1.append(curNode.left)
      if curNode.right:
         stack1.append(curNode.right)
   print(stack2[::-1])
      
      
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


postorder(root)