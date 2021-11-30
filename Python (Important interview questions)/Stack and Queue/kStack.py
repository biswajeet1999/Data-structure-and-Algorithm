class Stack:
   def __init__(self, capacity, k):
      self.capacity = capacity
      self.k = k
      self.arr = [None for _ in range(capacity)]
      self.top = [-1 for _ in range(k)]
      self.next = [i+1 for i in range(capacity)]
      self.free = 0

   def isFull(self):
      if self.free == self.capacity:
         return True
      return False

   def isEmpty(self, stackNo):
      return self.top[stackNo] == -1
   
   def push(self, stackNo, data):
      if self.isFull():
         print("Stack overflow")
         return
      freeIdx = self.free
      self.arr[freeIdx] = data
      self.free = self.next[freeIdx]
      self.next[freeIdx] = self.top[stackNo]
      self.top[stackNo] = freeIdx

   def pop(self, stackNo):
      if self.isEmpty(stackNo):
         print("Stack underflow")
         return
      topIdx = self.top[stackNo]
      data = self.arr[topIdx]
      self.top[stackNo] = self.next[topIdx]
      self.next[topIdx] = self.free
      self.free = topIdx
      return data
