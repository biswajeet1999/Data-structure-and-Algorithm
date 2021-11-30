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
         print(curNode.data, end="  ")
         curNode = curNode.next
      print()

def intersectionPoints(lst1, lst2):
   curNode1 = lst1.head
   curNode2 = lst2.head
   resultLst = LinkedList()

   while curNode1 and curNode2:
      if curNode1.data < curNode2.data:
         curNode1 = curNode1.next
      elif curNode1.data > curNode2.data:
         curNode2 = curNode2.next
      else:
         resultLst.add(curNode1.data)
         curNode1 = curNode1.next
         curNode2 = curNode2.next
   return resultLst

ll1 = LinkedList()
ll1.add(7)
ll1.add(6)
ll1.add(5)
ll1.add(4)
ll1.add(3)
ll1.add(2)
ll1.add(1)

ll2 = LinkedList()
ll2.add(10)
ll2.add(9)
ll2.add(8)
ll2.add(6)
ll2.add(3)
ll2.add(2)
ll2.add(1)
ll2.add(-1)

resultLst = intersectionPoints(ll1, ll2)
ll1.display()
ll2.display()
resultLst.display()
