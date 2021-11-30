class Node:
   def __init__(self, data, idx, arrayNo):
      self.data = data
      self.idx = idx
      self.arrayNo = arrayNo

class Heap:
   def __init__(self):
      self.arr = []
      self.capacity = 0

   def prelocateDown(self, idx):
      leftIdx = idx * 2 + 1
      while leftIdx < self.capacity:
         rightIdx = idx * 2 + 2
         if rightIdx >= self.capacity or self.arr[rightIdx].data > self.arr[leftIdx].data:
            idxToSwap = leftIdx
         else:
            idxToSwap = rightIdx
         if self.arr[idx].data <= self.arr[idxToSwap].data:
            return
         swap(self.arr, idx, idxToSwap)
         idx = idxToSwap
         leftIdx = idx*2+1

   def prelocateUp(self, idx):
      while idx > 0:
         parentIdx = (idx-1)//2
         if self.arr[parentIdx].data <= self.arr[idx].data:
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


def mergeArrays(arrayLst):
   k = len(arrayLst)
   n = len(arrayLst[0])
   result = []
   minHeap = Heap()
   for arrayIdx in range(k):
      node = Node(arrayLst[arrayIdx][0], 0, arrayIdx)
      minHeap.insert(node)
   
   while minHeap.capacity > 0:
      node = minHeap.remove()
      result.append(node.data)
      targetArrayIdx = node.arrayNo
      nextIdx = node.idx + 1
      if nextIdx < n:
         newNode = Node(arrayLst[targetArrayIdx][nextIdx], nextIdx, targetArrayIdx)
         minHeap.insert(newNode)
   return result

print(mergeArrays([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))