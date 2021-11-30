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

# O(n) time | O(n) space
# def populateTreeFromString(s):
#    global ptr

#    if ptr >= len(s):
#       return
#    if s[ptr] == "(":
#       ptr += 1
#    curNode = Node(s[ptr])
#    ptr += 1
#    if ptr < len(s) and s[ptr] == ")":
#       ptr += 1
#       return curNode
#    curNode.left = populateTreeFromString(s)
#    if ptr < len(s) and s[ptr] == ")":
#       ptr += 1
#       return curNode
#    curNode.right = populateTreeFromString(s)
#    if ptr < len(s) and s[ptr] == ")":
#       ptr += 1
#    return curNode
      
# ptr = 0
# root = populateTreeFromString("1(2)(3)")
# printTree(root)

# ptr = 0
# root = populateTreeFromString("4(2(3)(1))(6(5))")
# printTree(root)

# method-2
# O(n) time | O(n) space
def populateTreeFromString(s):
   # build tree using staack
   pass