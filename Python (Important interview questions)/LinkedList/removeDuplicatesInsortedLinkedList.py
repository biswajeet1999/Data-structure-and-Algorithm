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

   def display(self):
      curNode = self.head
      while curNode is not None:
         print(curNode.data, end="\t")
         curNode = curNode.next
      print()

# O(n) time | O(1) space
def removeDuplicates(lst):
   curNode = lst.head
   while curNode.next is not None:
      if curNode.data == curNode.next.data:
         curNode.next = curNode.next.next
      else:
         curNode = curNode.next

lst = LinkedList()
lst.add(5)
lst.add(5)
lst.add(4)
lst.add(2)
lst.add(2)
lst.add(2)
lst.display()
removeDuplicates(lst)
lst.display()