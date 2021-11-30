class Node:
   def __init__(self, key):
      self.value = key
      self.left = None
      self.right = None

def LCA(root: Node, node1, node2):
   parents1 = {}
   populateParent(root, node1, parents1)
   parents2 = {}
   populateParent(root, node2, parents2)
   
   diff = abs(len(parents1) - len(parents2))
   if len(parents1) > len(parents2):
      for i in range(diff):
         node1 = parents1[node1]
   elif len(parents2) > len(parents1):
      for i in range(diff):
         node2 = parents2[node2]
   count = diff
   while node1 is not node2:
      node1 = parents1[node1]
      node2 = parents2[node2]
      count+=2 # 2 added bcz node1 moveup 1 distance and node2 cover 1 distance
   return count

def populateParent(root, targetNode, parents):
   if root is None:
      return None

   if root == targetNode:
      return root
   child = populateParent(root.left, targetNode, parents)
   if child != None:
      parents[child] = root
      return root  
   child = populateParent(root.right, targetNode, parents)
   if child != None:
      parents[child] = root
      return root
   return None 


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
print(LCA(root, root.left.right.left, root.right.left))
print(LCA(root, root.left.right.left, root.left.right))
