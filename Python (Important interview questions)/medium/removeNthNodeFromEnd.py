class Node:
  def __init__(self, value):
    self.value = value


def removeNthNodeFromEnd(head, n):
  first = head
  second = head
  i = 1

  while i <= n+1:
    if second is None and i == n: # remove head case
      head = head.next
      return head  
    if second is None: # if n > len(linked list) 
      return head
    i += 1
    second = second.next

  while second is not None:
    second = second.next
    first = first.next

  first.next = first.next.next