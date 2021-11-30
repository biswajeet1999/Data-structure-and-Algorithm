class Node:
   def __init__(self, key):
      self.data = key
      self.prev = None
      self.next = None

class DLL:
   def __init__(self):
      self.head = None
      self.tail = None
   
   def insert(self, key):
      if self.head is None:
         self.head = self.tail = Node(key)
         return
      newNode = Node(key)
      self.tail.next = newNode
      newNode.prev = self.tail
      self.tail = newNode
   
   def remove(self):
      if self.head is None:
         return None
      nodeToDelete = self.head
      self.head = nodeToDelete.next
      if self.head is None:
         self.tail = None
         return nodeToDelete
      self.head.prev = None
      nodeToDelete.next = None
      return nodeToDelete
      
   def display(self):
      curNode = self.head
      while curNode:
         print(curNode.data, end="  ")
         curNode = curNode.next
      print()

# O(k) time | O(1) space
def rotate(dll: DLL, k):
   head = dll.head
   tail = dll.tail
   curNode = head
   for _ in range(k-1):
      curNode = curNode.next
   newHead = curNode.next
   curNode.next = None
   newHead.prev = None
   
   tail.next = head
   head.prev = tail
   tail = curNode
   dll.head = newHead
   dll.tail = tail


dll = DLL()
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert(4)
dll.insert(5)
dll.insert(6)
dll.insert(7)
dll.insert(8)
dll.display()
rotate(dll, 3)
dll.display()

