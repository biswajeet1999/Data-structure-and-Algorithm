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

#  recursive
# O(n) time | O(n) space
def add1(lst):
   if lst.head is None:
      return
   carry = add1Util(lst.head)
   if carry != 0:
      newNode = Node(carry)
      newNode.next = lst.head
      lst.head = newNode

def add1Util(curNode):
   if curNode.next is None:
      summ = 1 + curNode.data
      curNode.data = summ % 10
      return summ // 10
   carry = add1Util(curNode.next)
   if carry == 0:
      return 0
   summ = carry + curNode.data
   curNode.data = summ % 10
   return summ // 10
   

# iterative
# reverse num
# add 1
# reverse num
# O(n) time | O(1) space

num = LinkedList()
num.add(9)
num.add(9)
num.add(9)
num.add(9)
num.display()
add1(num)
num.display()

num1 = LinkedList()
num1.add(4)
num1.add(8)
num1.add(7)
num1.display()
add1(num1)
num1.display()
