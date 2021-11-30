def removeLoop(lst):
   slow = lst.head
   fast = lst.head

   while slow and fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
         break
   
   if slow != fast:
      return None
   
   slow = lst.head
   prev = None
   while slow != fast:
      prev = fast
      slow = slow.next
      fast = fast.next
   prev.next = None