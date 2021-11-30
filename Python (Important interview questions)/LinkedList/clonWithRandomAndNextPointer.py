class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.random = None


def clone(head: Node):
   cloneHead = cloneTail = None
   curNode = head
   # clone original list with next field
   while curNode:
      curCloneNode = Node(curNode.data)
      if cloneHead is None:
         cloneHead = cloneTail = curCloneNode
      else:
         cloneTail.next = curCloneNode
         cloneTail = curCloneNode
      curNode = curNode.next
   # alter next fields
   cur = head
   curClone = cloneHead
   while cur:
      temp = cur
      tempClone = curClone
      cur = cur.next
      curClone = curClone.next
      tempClone.next = temp.next
      temp.next = tempClone
   # populate random field
   cur = head
   while cur:
      curClone = cur.next
      curCloneRandomNode = cur.random.next
      curClone.random = curCloneRandomNode
      cur = cur.next.next
   # repopulate next field of both the list with correct node 
   cur = head
   while cur:
      curClone = cur.next
      cur.next = curClone.next
      curClone.next = cur.next.next
      cur = cur.next
   return cloneHead