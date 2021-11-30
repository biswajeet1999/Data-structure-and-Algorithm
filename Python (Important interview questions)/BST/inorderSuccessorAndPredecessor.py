class Node:
   def __init__(self, key):
      self.key = key
      self.left = self.right = None


def inorderPredecessor(root: Node, target: Node):
   parent = [None]
   pred = [None]
   inorderPredecessorHelper(root, target, parent, pred)
   return pred[0].key if pred[0] else None


def inorderPredecessorHelper(root, target, parent, pred):
   if root is None:
      return
   
   if target > root.key:
      parent[0] = root
      inorderPredecessorHelper(root.right, target, parent, pred)
   elif target < root.key:
      inorderPredecessorHelper(root.left, target, parent, pred)
   else:
      temp = root.left
      while temp and temp.right:
         temp = temp.right
      if temp:
         pred[0] = temp
      else:
         pred[0] = parent[0]


def inorderSuccessor(root: Node, target: Node):
   parent = [None]
   pred = [None]
   inorderPredecessorHelper(root, target, parent, pred)
   return pred[0].key if pred[0] else None


def inorderSuccessorHelper(root, target, parent, pred):
   if root is None:
      return
   
   if target > root.key:
      inorderSuccessorHelper(root.right, target, parent, pred)
   elif target < root.key:
      parent[0] = root
      inorderSuccessorHelper(root.left, target, parent, pred)
   else:
      temp = root.right
      while temp and temp.left:
         temp = temp.left
      if temp:
         pred[0] = temp
      else:
         pred[0] = parent[0]


   
def insert(root, key):
   if root is None:
      return Node(key)
   if key < root.key:
      root.left = insert(root.left, key)
   else:
      root.right = insert(root.right, key)
   return root


root = None
root = insert(root, 50)
root = insert(root, 30);
root = insert(root, 20);
root = insert(root, 40);
root = insert(root, 70);
root = insert(root, 60);
root = insert(root, 80);

print(inorderPredecessor(root, 50))
print(inorderPredecessor(root, 30))
print(inorderPredecessor(root, 20))
print(inorderPredecessor(root, 40))
print(inorderPredecessor(root, 70))
print(inorderPredecessor(root, 60))
print(inorderPredecessor(root, 80))