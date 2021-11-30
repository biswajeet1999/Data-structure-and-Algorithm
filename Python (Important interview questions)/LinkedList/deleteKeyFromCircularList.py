class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

class CircularLinkedList: 
   def __init__(self):
      self.head = None

   def add(self, value):
      if self.head is None:
         self.head = Node(value)
         self.head.next = self.head
      else:
         newNode = Node(value)
         newNode.next = self.head.next
         self.head.next = newNode
   
   def addRange(self, n):
      for i in range(1, n+1):
         self.add(i)

   def delete(self, key):
      if self.head == None:
         return False
      if self.head.next == self.head and self.head.data == key:
         self.head = None
         return 
      head = curNode = self.head

      while True:
         if curNode.next.data == key:
            if curNode.next == head:
               self.head = curNode.next.next
            curNode.next = curNode.next.next
            return True
         curNode = curNode.next
         if curNode == head:
            return False

   def display(self):
      if self.head is None:
         return
      head = curNode = self.head
      while True:
         print(curNode.data)
         curNode = curNode.next
         if curNode == head:
            return
      
      print()

