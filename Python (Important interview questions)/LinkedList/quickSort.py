class Node:
   def __init__(self, key):
      self.data = key
      self.next = None


def partition(head):
   piovetKey = head.data
   smallerList = None
   equalList = None
   greaterList = None
   while head:
      temp = head
      if temp.data < piovetKey:
         temp.next = smallerList
         smallerList = temp
      elif temp.data == piovetKey:
         temp.next = equalList
         equalList = temp
      else:
         temp.next = greaterList
         greaterList = temp
      head = head.next
   return [smallerList, equalList, greaterList]

def quickSort(head: Node):
   if head is None or head.next is None:
      return head
   [leftList, pivotNode, rightList] = partition(head)
   leftSortedList = quickSort(leftList)
   rightSortedList = quickSort(rightList)
   cur = rightSortedList
   while cur.next:
      cur = cur.next
   cur.next = pivotNode
   cur = pivotNode
   while cur.next:
      cur = cur.next
   cur.next = rightSortedList
   return leftSortedList