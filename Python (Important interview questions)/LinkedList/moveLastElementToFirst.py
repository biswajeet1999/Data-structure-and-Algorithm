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
def rotateRight(lst):
   if lst.head is None or lst.head.next is None:
      return
   prevNode = lst.head
   curNode = prevNode.next
   while curNode.next:
      prevNode = curNode
      curNode = curNode.next
   
   prevNode.next = None
   curNode.next = lst.head
   lst.head = curNode

linkedList = LinkedList()
linkedList.addRange(7)
linkedList.display()
rotateRight(linkedList)
linkedList.display()