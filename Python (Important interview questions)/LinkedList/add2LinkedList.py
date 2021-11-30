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
         print(curNode.data, end="")
         curNode = curNode.next
      print()

def reverse(lst):
   prev = None
   cur = lst.head
   while cur is not None:
      nxt = cur.next
      cur.next = prev
      prev = cur
      cur = nxt
   lst.head = prev

# O(n+m) time | O(max(n, m)) space
def addLinkedList(lst1, lst2):
   sumList = LinkedList()
   carry = 0
   if lst1.head is None and lst2.head is None:
      return sumList

   reverse(lst1)
   reverse(lst2)
   curNode1 = lst1.head
   curNode2 = lst2.head
   while curNode1 is not None and curNode2 is not None:
      summ = carry + curNode1.data + curNode2.data
      sumList.add(summ % 10)
      carry = summ // 10
      curNode1 = curNode1.next
      curNode2 = curNode2.next
   
   while curNode1 is not None:
      summ = carry + curNode1.data
      sumList.add(summ % 10)
      carry = summ // 10
      curNode1 = curNode1.next
   while curNode2 is not None:
      summ = carry + curNode2.data
      sumList.add(summ % 10)
      carry = summ // 10
      curNode2 = curNode2.next
   reverse(lst1)
   reverse(lst2)

   return sumList

lst1 = LinkedList()
lst1.add(3)
lst1.add(2)
lst1.add(1)

lst2 = LinkedList()
lst2.add(3)
lst2.add(2)
lst2.add(1)

summ = addLinkedList(lst1, lst2)
lst1.display()
lst2.display()
summ.display()