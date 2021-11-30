class Node:
   def __init__(self, key):
      self.value = key
      self.left = None
      self.right = None

cache = {}

def isDuplicatePresent(root: Node):
   if root is None:
      return '$' # delemeter
   s = ""
   leftStr = isDuplicatePresent(root.left)
   rightStr = isDuplicatePresent(root.right)

   s = str(root.value) + leftStr + rightStr

   if len(s) > 3: # > 3 bcs of 2 delimiter for leaf node
      if s not in cache:
         cache[s] = 0
      cache[s] += 1
   return s


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.right = Node(2)
root.right.right.left = Node(4)
root.right.right.right = Node(5)
print(isDuplicatePresent(root))
for _, val in cache.items():
   if val > 1:
      print("yes")
print(cache)



