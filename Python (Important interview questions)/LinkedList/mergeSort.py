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

# O(nlogn) time | O(1) space
def mergesort(lst):
   lst.head = mergesortHelper(lst.head)

def mergesortHelper(head):
   if head is None or head.next is None:
      return head

   midNode = middleNode(head)
   secondHalf = midNode.next
   midNode.next = None
   firstHalf = head

   firstHalf = mergesortHelper(firstHalf)
   secondHalf = mergesortHelper(secondHalf)
   return merge(firstHalf, secondHalf)
   
def merge(firstHalf, secondHalf):
   newHead = newTail = None
   while firstHalf and secondHalf:
      if firstHalf.value > secondHalf.value:
         nodeToInsert = secondHalf
         secondHalf = secondHalf.next
         nodeToInsert.next = None
      else:
         nodeToInsert = firstHalf
         firstHalf = firstHalf.next
         nodeToInsert.next = None
      if newHead == None:
         newHead = newTail = nodeToInsert
      else:
         newTail.next = nodeToInsert
         newTail = nodeToInsert

   while firstHalf:
      nodeToInsert = firstHalf
      firstHalf = firstHalf.next
      nodeToInsert.next = None
      if newHead == None:
         newHead = newTail = nodeToInsert
      else:
         newTail.next = nodeToInsert
         newTail = nodeToInsert

   while secondHalf:
      nodeToInsert = secondHalf
      secondHalf = secondHalf.next
      nodeToInsert.next = None
      if newHead == None:
         newHead = newTail = nodeToInsert
      else:
         newTail.next = nodeToInsert
         newTail = nodeToInsert
   return newHead

def middleNode(head: Node) -> Node:
   slow = fast = head
   prev = None
   while fast and fast.next:
      prev = slow
      slow = slow.next
      fast = fast.next.next
   if fast is None: # even length
      return prev # return previous to avoid infinite loop 
   return slow


lst = LinkedList()
lst.add(5)
lst.add(15)
lst.add(1)
lst.add(6)
# lst.add(1)
lst.add(2)
lst.add(3)
lst.add(4)
lst.display()
mergesort(lst)
lst.display()