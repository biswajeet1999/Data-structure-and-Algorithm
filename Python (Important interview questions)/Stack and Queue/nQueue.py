# O(1) time | O(n) space
class Queue:
   def __init__(self, capacity, nQueue):
      self.capacity = capacity
      self.nQueue = nQueue
      self.arr = [None for _ in range(capacity)]
      self.front = [-1 for _ in range(nQueue)]
      self.rear = [-1 for _ in range(nQueue)]
      self.next = [None for _ in range(capacity)]
      self.free = 0

   def enqueue(self, data, nQueue):
      if self.free == self.capacity:
         print("Queue overflow")
         return
      currRear = self.rear[nQueue]
      curFront = self.front[nQueue]
      free = self.free
      self.arr[free] = data
      self.free = self.next[free]
      self.next[free] = -1
      if curFront == -1:
         self.front[nQueue] = self.rear[nQueue] = free
         return
      self.next[currRear] = free
      self.rear[nQueue] = free

   def dequeue(self, nQueue):
      if self.front[nQueue] == -1:
         print("Queue underflow")
         return
      data = self.arr[self.front[nQueue]]
      prevFront = self.front[nQueue]
      
      if self.front[nQueue] == self.rear[nQueue]:
         self.front[nQueue] = self.rear[nQueue] = -1
      else:
         self.front[nQueue] = self.next[self.front[nQueue]]
      
      self.next[prevFront] = self.free
      self.free = prevFront
      return data

   def peek(self, nQueue):
      if self.front[nQueue] == -1:
         print("Queue underflow")
         return
      return self.arr[self.front[nQueue]]

