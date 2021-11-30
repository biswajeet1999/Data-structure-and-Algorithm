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

   def display(self):
      if self.head is None:
         return
      curNode = head = self.head
      print(curNode.data, end="  ")
      curNode = curNode.next
      while curNode is not head:
         print(curNode.data, end="  ")
         curNode = curNode.next
      print()

def breakCycle(lst):
   if lst.head is None:
      return
   if lst.head.next == lst.head:
      lst.head.next = None
      return
   head = lst.head
   curNode = head.next

   while curNode.next is not head:
      curNode = curNode.next
   curNode.next = None


def split(lst: CircularLinkedList):
   if lst.head.next == lst.head:
      return lst, lst

   breakCycle(lst)

   head = lst.head
   slow = fast = head
   prevSlow = prevFast = None
   while fast and fast.next:
      prevSlow = slow
      slow = slow.next
      prevFast = fast.next
      fast = fast.next.next
   
   if fast is None: # even length
      mid = prevSlow
      tail = prevFast
   else:
      mid = slow
      tail = fast
   
   head1 = head
   tail1 = mid
   head2 = mid.next
   tail2 = tail

   tail1.next = head1
   lst2 = CircularLinkedList()
   lst2.head = head2
   tail2.next = lst2.head

   return lst, lst2
    

   


ll = CircularLinkedList()
ll.addRange(2)
ll.display()
ll1, ll2 = split(ll)
ll1.display()
ll2.display()