class Stack:
   def __init__(self, n):
      self.capacity = n
      self.arr = [None for _ in range(n)]
      self.top1 = -1
      self.top2 = n

   def isFull(self):
      if self.top1+1 == self.capacity or self.top2 == 0 or self.top1+1 == self.top2:
         return True
      return False
   
   def push1(self, data):
      if self.isFull():
         print("Stack1 overflow")
         return
      self.top1+=1
      self.arr[self.top1] = data

   def push2(self, data):
      if self.isFull():
         print("Stack2 overflow")
         return
      self.top2 -= 1
      self.arr[self.top2] = data

   def pop1(self):
      if self.top1 == -1:
         print("Stack1 underflow")
         return
      data = self.arr[self.top1]
      self.top1 -= 1
      return data

   def pop2(self):
      if self.top2 == self.capacity:
         print("Stack2 underflow")
         return
      data = self.arr[self.top2]
      self.top2 += 1
      return data
