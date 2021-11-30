class Node:
   def __init__(self, key):
      self.data = key
      self.prev = self.next = None

class DLL:
   def __init__(self):
      self.length = 0
      self.head = self.tail = self.mid = None

   def push(self, data):
      self.length += 1
      if self.head == None:
         self.head = self.tail = self.mid = Node(data)
         return
      temp = Node(data)
      self.tail.next = temp
      temp.prev = self.tail
      self.tail = temp
      #  update mid
      if self.length % 2 == 0: # even length after add
         self.mid = self.mid.next
      else:
         # dont move mid pointer
         pass

   def pop(self):
      data = self.tail
      if self.head == None:
         return None
      if self.head == self.tail:
         self.head = self.tail = self.mid = None
         self.length -= 1
         return data
      if self.length % 2 == 0:
         self.mid = self.mid.prev
      else:
         # do nothing
         pass
      self.length -= 1
      self.tail = self.tail.prev
      self.tail.next = None
      return data

   def deleteMid(self):
      data = self.mid
      if self.head == None:
         return None
      if self.head == self.tail:
         self.head = self.mid = self.tail = None
         self.length -= 1
         return data
      if self.mid ==  self.tail:
         self.tail = self.tail.prev
         self.mid = self.tail
         self.tail.next = None
         self.length -= 1
         return data
      if self.length % 2 == 0:
         self.mid = self.mid.prev
         self.mid.next = self.mid.next.next
         self.mid.next.prev = self.mid
      else:
         self.mid = self.mid.next
         self.mid.prev = self.mid.prev.prev
         self.mid.prev.next = self.mid
      self.length -= 1
      return data


   def getMid(self):
      return self.mid



stack = DLL()

stack.push(11)
stack.push(22)
stack.push(33)
stack.push(44)
stack.push(55)
stack.push(66)
stack.push(77)
print(stack.getMid().data)
stack.pop()
print(stack.getMid().data)
stack.pop()
print(stack.getMid().data)
