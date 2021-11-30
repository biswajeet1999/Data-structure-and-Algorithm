class Node:
   def __init__(self, data):
      self.value = data
      self.next = None

class LinkedList: 
   def __init__(self):
      self.head = None
      self.tail = None

   def addLast(self, value):
      newNode = Node(value)
      if self.head is None:
         self.head = self.tail = newNode
      else:
         self.tail.next = newNode
         self.tail = newNode
      return newNode
      
   def remove(self, targetNode: Node):
      if self.head is targetNode:
         self.head = self.head.next
         if self.head == None:
            self.tail = None
         return
      curNode = self.head
      while curNode.next is not targetNode:
         curNode = curNode.next
      curNode.next = targetNode.next
      if self.tail == targetNode:
         self.tail = curNode

   def getHead(self):
      return self.head

   def display(self):
      curNode = self.head
      while curNode is not None:
         print(curNode.value, end="  ")
         curNode = curNode.next
      print()

# O(26*n) time | O(26) space
def findStream(string: str):
   uniqueCharCache = {}
   repeatedCharCache = {}
   orderedCharLst = LinkedList()
   result = []
   for char in string:
      if char not in repeatedCharCache and  char not in uniqueCharCache:
         node = orderedCharLst.addLast(char)
         uniqueCharCache[char] = node
      elif char not in repeatedCharCache:
         nodeToRemove = uniqueCharCache[char]
         orderedCharLst.remove(nodeToRemove)
         uniqueCharCache.pop(char)
         repeatedCharCache[char] = True
      ans = orderedCharLst.getHead()
      if ans is None:
         result.append('#')
      else:
         result.append(ans.value)
   return result

print(findStream('aabc'))
