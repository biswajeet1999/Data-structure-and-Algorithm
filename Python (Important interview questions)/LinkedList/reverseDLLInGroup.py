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

def reverseInGroup(dll: DLL, groupSize):
   newHead = None
   newTail = None
   blockStart = dll.head
   blockEnd = None
   nextBlockStart = None
   prevBlockEndAfterReverse = None
   while blockStart is not None:
      blockEnd = getNextKthNode(blockStart, groupSize)
      if blockEnd is not None:
          nextBlockStart = blockEnd.next
      if(blockEnd is None):
         if nextBlockStart is None:
            break
         prevBlockEndAfterReverse.next = nextBlockStart
         nextBlockStart.prev = prevBlockEndAfterReverse
         newTail = None
         break
      reverse(blockStart, blockEnd)
      blockStart.next = None
      blockEnd.prev = None
      if not newHead:
         newHead = blockEnd
         newHead.prev = None
      if prevBlockEndAfterReverse:
         prevBlockEndAfterReverse.next = blockEnd
         blockEnd.prev = prevBlockEndAfterReverse      
      newTail = blockStart
      prevBlockEndAfterReverse = blockStart
      blockStart = nextBlockStart
   dll.head = newHead
   if newTail:
      dll.tail = newTail



def getNextKthNode(blockStart: Node, groupSize: int):
   curNode = blockStart
   for _ in range(groupSize - 1):
      if curNode is None:
         return None
      curNode = curNode.next
   return curNode

def reverse(blockStart, blockEnd):
   curNode = blockStart
   while curNode:
      tempRef = curNode.prev
      curNode.prev = curNode.next
      curNode.next = tempRef
      if curNode is blockEnd:
         return
      curNode = curNode.prev
   
dll = DLL()
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert(4)
dll.insert(5)
dll.insert(6)
dll.display()
reverseInGroup(dll, 4)
dll.display()