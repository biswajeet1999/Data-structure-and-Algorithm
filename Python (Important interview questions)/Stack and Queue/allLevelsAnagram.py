class Node:
   def __init__(self, val):
      self.data = val
      self.left = None
      self.right = None

# O(2n) time :- traverse tree 2 times
# O(2n) space
def checkAnagram(root1, root2):
   if root1 == None and root2 == None:
      return True
   if root1 == None or root2 == None:
      return False

   queue1 = []
   queue2 = []
   queue1.append(root1)
   queue1.append(None)
   queue2.append(root2)
   queue2.append(None)
   curLevel1 = []
   curLevel2 = []

   while len(queue1) > 0 or len(queue2) > 0:
      if len(queue1) == 0 or len(queue2) == 0:
         return False
      
      curNode1 = queue1.pop(0)
      curNode2 = queue2.pop(0)
      
      if curNode1 == None and curNode2 == None:
         if(checkAnagramUtil(curLevel1, curLevel2)) == False:
            return False
         curLevel1 = []
         curLevel2 = []
         if len(queue1) > 0: 
            queue1.append(None)
         if len(queue2) > 0:
            queue2.append(None)
         continue
      elif curNode1 == None or curNode2 == None:
         return False
      
      curLevel1.append(curNode1)
      curLevel2.append(curNode2)

      if curNode1.left:
         queue1.append(curNode1.left)
      if curNode1.right:
         queue1.append(curNode1.right)
      
      if curNode2.left:
         queue2.append(curNode2.left)
      if curNode2.right:
         queue2.append(curNode2.right)
   return True


def checkAnagramUtil(level1, level2):
   if len(level1) == 0 and len(level2) == 0:
      return True
   if len(level1) != len(level2):
      return False
   
   cache = {val.data: True for val in level2}
   for num in level1:
      if num.data not in cache:
         return False
   return True


root1 = Node(1) 
root1.left = Node(3) 
root1.right = Node(2) 
root1.right.left = Node(5) 
root1.right.right = Node(4) 
  
root2 = Node(1) 
root2.left = Node(2) 
root2.right = Node(3) 
root2.left.left = Node(4) 
root2.left.right = Node(5)

print(checkAnagram(root1, root2))