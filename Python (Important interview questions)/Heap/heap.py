class Heap:
   def __init__(self, arr):
      self.arr = arr[:]
      self.capacity = len(arr)
      self.buildHeap()
   
   def buildHeap(self):
      for idx in range((self.capacity // 2) - 1, -1, -1):
         self.prelocateDown(idx)

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
      self.capacity -= 1
      self.prelocateDown(0)
      return data

   def heapSort(self):
      while self.capacity > 1:
         self.remove()
      self.arr = self.arr[::-1]

def swap(arr, i, j):
   arr[i], arr[j] = arr[j], arr[i]



h = Heap([5, 4, 3, 2, 1])
h.insert(6)
print(h.arr)
h.heapSort()
print(h.arr)
print(h.capacity)