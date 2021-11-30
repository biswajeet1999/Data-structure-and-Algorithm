class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList: 
   def __init__(self):
      self.head = None

   def add(self, value):
      if self.head is None:
         self.head = Node(value)
      else:
         newNode = Node(value)
         newNode.next = self.head
         self.head = newNode
   
   def addRange(self, n):
      for i in range(n, 0, -1):
         self.add(i)

   def length(self):
      count = 0
      node = self.head
      while node:
         count += 1
         node = node.next
      return count

   def display(self):
      curNode = self.head
      while curNode is not None:
         print(curNode.data, end="  ")
         curNode = curNode.next
      print()

# O(n+m) time | o(1) space
def findIntersectionPoint(lst1, lst2):
   len1 = lst1.length()
   len2 = lst2.length()
   if len1 == 0 or len2 == 0:
      return None
   if len1 > len2:
      longestLst = lst1.head
      smallestLst = lst2.head
   else:
      longestLst = lst2.head
      smallestLst = lst1.head
   diff = abs(len1 - len2)
   for _ in range(diff):
      longestLst = longestLst.next
   
   while longestLst and smallestLst:
      if longestLst is smallestLst:
         return longestLst
      longestLst = longestLst.next
      smallestLst = smallestLst.next
   return None


lst1 = LinkedList()
lst1.add(5)
lst1.add(4)
lst1.add(3)
lst1.add(2)
lst1.add(1)

lst2 = LinkedList()
lst2.add(6)
lst2.add(10)
lst2.add(3)

lst2.head.next.next.next = lst1.head.next

intersectionPoint = findIntersectionPoint(lst1, lst2)
if intersectionPoint is None:
   print("not found")
lst1.display()
lst2.display()
print(intersectionPoint.data)