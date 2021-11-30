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
def reverseInGroup(lst, blockSize):
   newHead = None
   blockStartNode = lst.head
   prevBlockEndNodeAfterSwapping = None
   while True:
      blockEndNode = getNextKthNode(blockStartNode, blockSize)
      if blockEndNode is None:
         if prevBlockEndNodeAfterSwapping is not None: # except first block this will be true
            prevBlockEndNodeAfterSwapping.next =  blockStartNode
         break
      nextBlockStartNode = blockEndNode.next
      reverse(blockStartNode, blockEndNode)
      if newHead is None:
         newHead = blockEndNode
      if prevBlockEndNodeAfterSwapping is not None: # except first block this will be true
         prevBlockEndNodeAfterSwapping.next =  blockEndNode
      prevBlockEndNodeAfterSwapping = blockStartNode
      blockStartNode = nextBlockStartNode
   if newHead:
      lst.head = newHead

def getNextKthNode(blockStartNode, blockSize):
   curNode = blockStartNode
   for _ in range(blockSize - 1):
      curNode = curNode.next
      if curNode is None:
         return None
   return curNode

def reverse(blockStartNode, blockEndNode):
   prevNode = None
   curNode = blockStartNode
   while prevNode != blockEndNode:
      nextNode = curNode.next
      curNode.next = prevNode
      prevNode = curNode
      curNode = nextNode


linkedList = LinkedList()
linkedList.addRange(7)
linkedList.display()
reverseInGroup(linkedList, 3)
linkedList.display()