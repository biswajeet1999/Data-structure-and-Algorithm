class Node:
   def __init__(self, data):
      self.value = data
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
         print(curNode.value, end="  ")
         curNode = curNode.next
      print()


def removeNthNodeFromEnd(lst, k):
   if k <= 0: return None
   head = lst.head
   prevNode = None
   followPrt = head
   advancedPtr = head
   for _ in range(k):
      if advancedPtr == None: return None
      advancedPtr = advancedPtr.next
   while advancedPtr:
      advancedPtr = advancedPtr.next
      prevNode = followPrt
      followPrt = followPrt.next
   if followPrt is lst.head:
      lst.head = followPrt.next
   else:
      prevNode.next = followPrt.next
   return followPrt


ll = LinkedList()
ll.addRange(6)
ll.display()
removeNthNodeFromEnd(ll, 3)
ll.display()
