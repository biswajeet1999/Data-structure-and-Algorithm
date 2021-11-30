class Heap:
   def __init__(self):
      self.arr = []
      self.capacity = 0

   def prelocateDown(self, idx):
      leftIdx = idx * 2 + 1
      while leftIdx < self.capacity:
         rightIdx = idx * 2 + 2
         if rightIdx >= self.capacity or self.arr[rightIdx] > self.arr[leftIdx]:
            idxToSwap = leftIdx
         else:
            idxToSwap = rightIdx
         if self.arr[idx] <= self.arr[idxToSwap]:
            return
         swap(self.arr, idx, idxToSwap)
         idx = idxToSwap
         leftIdx = idx*2+1

   def prelocateUp(self, idx):
      while idx > 0:
         parentIdx = (idx-1)//2
         if self.arr[parentIdx] <= self.arr[idx]:
            return
         swap(self.arr, parentIdx, idx)
         idx = parentIdx
         
   def insert(self, data):
      self.arr.append(data)
      self.capacity += 1
      self.prelocateUp(self.capacity - 1)

   def remove(self):
      data = self.arr[0]
      swap(self.arr, 0, self.capacity - 1)
      self.arr.pop()
      self.capacity -= 1
      self.prelocateDown(0)
      return data

def swap(arr, i, j):
   arr[i], arr[j] = arr[j], arr[i]

# O(n^2log(k)) time | O(k) space
def getKthLargestSum(arr, k):
   minHeap = Heap()
   for i in range(0, len(arr)):
      subSum = 0
      for j in range(i, len(arr)):
         subSum += arr[j]
         print(subSum)   
         minHeap.insert(subSum)
         if minHeap.capacity > k:
            minHeap.remove()
   return minHeap.remove()



print(getKthLargestSum([20, -5, -1], 3))