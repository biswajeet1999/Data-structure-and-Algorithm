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

# O(n) time | O(1) space
def isPallendrom(lst):
   if lst.head is None:
      return True
   
   slow = fast = lst.head
   while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
   
   if fast is None:
     head2 =  reverse(slow)
   else:
     head2 = reverse(slow.next)

   curNode1 = lst.head
   curNode2 = head2

   while curNode2:
      if curNode1.data != curNode2.data:
         return False
      curNode1 = curNode1.next
      curNode2 = curNode2.next
   reverse(head2)
   return True

def reverse(head):
   cur = head
   prev = None

   while cur:
      nxt = cur.next 
      cur.next = prev
      prev = cur
      cur = nxt
   return prev


ll1 = LinkedList()
ll1.addRange(4)
print(isPallendrom(ll1))
ll1.display()
print()

ll2 = LinkedList()
ll2.addRange(5)
print(isPallendrom(ll2))
ll2.display()
print()

ll3 = LinkedList()
ll3.add(1)
ll3.add(2)
ll3.add(3)
ll3.add(2)
ll3.add(1)
print(isPallendrom(ll3))
ll3.display()
print()

ll4 = LinkedList()
ll4.add(1)
ll4.add(2)
ll4.add(2)
ll4.add(1)
print(isPallendrom(ll4))
ll4.display()
print()
