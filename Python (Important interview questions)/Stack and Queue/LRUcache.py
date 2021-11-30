class Node:
   def __init__(self, key, value):
      self.key = key
      self.value = value
      self.prev = self.next = None

class LinkedList:
   def __init__(self):
      self.head = self.tail = None
   
   def insertAtFront(self, node):
      if self.head == None:
         self.head = self.tail = node
         return
      node.next = self.head
      self.head.prev = node
      self.head = node

   def remove(self, node):
      if self.head is None:
         return None
      if self.tail is node:
         self.removeFromTail()
         return
      prevNode = node.prev
      nextNode = node.next
      node.prev = node.next = None
      nextNode.prev = prevNode
      if prevNode:
         prevNode.next = nextNode

   def removeFromTail(self):
      if self.head is None:
         return None
      node = self.tail
      if self.head == self.tail:
         self.head = self.tail = None
         return node
      self.tail = node.prev
      self.tail.next = None
      node.prev = node.next = None
      return node

      
class LRU:
   def __init__(self, capacity):
      self.capacity = capacity
      self.size = 0
      self.linkedList = LinkedList()
      self.cache = {}

   def get(self, key):
      if key not in self.cache:
         return None
      node = self.cache[key]
      self.linkedList.remove(node)
      self.linkedList.insertAtFront(node)
      return node.value

   def set(self, key, value):
      if key in self.cache:
         node = self.cahce[key]
         node.value = value
         self.linkedList.remove(node)
         self.linkedList.insertAtFront(node)
         return
      if self.size == self.capacity:
         node = self.linkedList.removeFromTail()
         self.cache.pop(node.key)
      else:
         self.size += 1
      node = Node(key, value)
      self.cache[key] = node
      self.linkedList.insertAtFront(node)
