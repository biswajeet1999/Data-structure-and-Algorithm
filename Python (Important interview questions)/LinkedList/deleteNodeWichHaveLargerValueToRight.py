# O(n) time | O(1) space
def remove(lst):
   head = lst.head
   if head is None: return
   head = reverse(head)
   maxSoFar = head.value
   curNode = head.next
   prevNode = head
   while curNode is not None:
      if curNode.value < maxSoFar:
         curNode = curNode.next
         prevNode.next = curNode
      maxSoFar = max(maxSoFar, curNode.value)
   lst.head =  reverse(head)

def reverse(head):
   prevNode = None
   curNode = head
   while curNode is not None:
      nextNode = curNode.next
      curNode.next = prevNode
      prevNode = curNode
      curNode = nextNode
   return prevNode

