
class Heap:
   def __init__(self, heapFunction, array = []):
      self.array = array
      self.heapFunction = heapFunction
      self.buildHeap()
      
   def buildHeap(self):
      for i in reversed(range(len(self.array) // 2)):
         self.prelocateDown(i)

   def prelocateDown(self, idx):
      leftChildIdx = 2 * idx + 1
      while leftChildIdx < len(self.array):
         rightChildIdx = 2 * idx + 2
         if rightChildIdx < len(self.array) and self.heapFunction(self.array[leftChildIdx], self.array[rightChildIdx]):
            idxToSwap = rightChildIdx
         else:
            idxToSwap = leftChildIdx
         if self.heapFunction(self.array[idx], self.array[idxToSwap]):
            self.array[idx], self.array[idxToSwap] = self.array[idxToSwap], self.array[idx]
            idx = idxToSwap
            leftChildIdx = 2 * idx + 1
         else:
            break
   
   def prelocateUp(self, idx):
      while idx > 0:
         parent = (idx - 1) // 2
         if self.heapFunction(self.array[parent], self.array[idx]):
            self.array[idx], self.array[parent] = self.array[parent], self.array[idx]
            idx = parent
         else:
            break

   def insert(self, value):
      self.array.append(value)
      self.prelocateUp(len(self.array) - 1)

   def remove(self):
      if len(self.array) == 0:
         return None
      self.array[0], self.array[-1] = self.array[-1], self.array[0]
      elementToRemove = self.array.pop()
      self.prelocateDown(0)
      return elementToRemove

def minHeapFunc(val1, val2):
   return val1 > val2

def maxHeapFunc(val1, val2):
   return val1 < val2



class ContinousMedian:
   def __init__(self):
      self.minHeap = Heap(minHeapFunc)
      self.maxHeap = Heap(maxHeapFunc)
      self.medians = []

   def insert(self, value):
      if len(self.maxHeap.array) == 0 or value < self.maxHeap.array[0]:
        self.maxHeap.insert(value)
      else:
         self.minHeap.insert(value)
      self.balanceHeaps()
      self.calculateMedians()
      return self.meidans


   def balanceHeaps(self):
      diff = len(self.maxHeap.array) - len(self.minHeap.array)
      if diff == 0 or diff == 1:
         return
      if diff > 1:
         self.minHeap.insert(self.maxHeap.remove())
      else:
         self.maxHeap.insert(self.minHeap.remove())

   def calculateMedians(self):
      if len(self.maxHeap.array) == len(self.minHeap.array):
         self.medians.append((self.maxHeap.array[0] + self.minHeap.array[0]) // 2)
      else:
         self.medians.append(self.maxHeap.array[0])


