def startOfLoop(lst):
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
   while slow != fast:
      slow = slow.next
      fast = fast.next
   return slow