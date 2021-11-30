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
      for i in range(1, n+1):
         self.add(i)

   def display(self):
      curNode = self.head
      while curNode is not None:
         print(curNode.data, end="\t")
         curNode = curNode.next
      print()

# O(n) time | O(1) space
def reverseLinkedList(lst):
   prev = None
   cur = lst.head
   while cur is not None:
      nxt = cur.next
      cur.next = prev
      prev = cur
      cur = nxt
   lst.head = prev

# O(n) time | O(n) space
# def reverseLinkedList(lst):
#    reverseLinkedListUtil(lst, lst.head, None)

# def reverseLinkedListUtil(lst, curNode, prevNode):
#    if curNode.next is None:
#       lst.head = curNode
#       curNode.next = prevNode
#       return
#    reverseLinkedListUtil(lst, curNode.next, curNode)
#    curNode.next = prevNode

linkedList = LinkedList()
linkedList.addRange(5)
linkedList.display()
reverseLinkedList(linkedList)
linkedList.display()