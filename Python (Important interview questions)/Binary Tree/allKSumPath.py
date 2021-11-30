class Node:
   def __init__(self, key):
      self.value = key
      self.left = None
      self.right = None


def KSumPath(root: Node, k):
   return KSumPathUtil(root, k, path=[], result = [])

def KSumPathUtil(root, k, path, result):
   if root == None:
      return
   
   if (root.left == None and root.right == None):
      path.append(root.value)
      printAllKSumPath(path, k, result)
      path.pop()
      return 
   
   path.append(root.value)
   KSumPathUtil(root.left, k, path, result)
   KSumPathUtil(root.right, k, path, result)
   path.pop()
   return result

def printAllKSumPath(path, k, result):
   if len(path) == 0:
      return
   
   for i in range(len(path)):
      curSum = 0
      for j in range(i, len(path)):
         curSum += path[j]
         if curSum == k:
            result.append(path[i : j+1])

   return result


root = Node(1) 
root.left = Node(3) 
root.left.left = Node(2) 
root.left.right = Node(1) 
root.left.right.left = Node(1) 
root.right = Node(-1) 
root.right.left = Node(4) 
root.right.left.left = Node(1) 
root.right.left.right = Node(2) 
root.right.right = Node(5) 
root.right.right.right = Node(2)
k = 5
print(KSumPath(root, k))