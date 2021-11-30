
class MaxHeap:
   def __init__(self, array):
      self.heap = array[:]
      self.buildHeap()

   def buildHeap(self):
      n = len(self.heap)
      for i in range((n//2) - 1, -1, -1):
         self.prelocateDown(i)
   
   def size(self):
      return len(self.heap)

   def insert(self, value):
      self.heap.append(value)
      self.prelocateUp(self.size() - 1)

   def remove(self):
      if len(self.heap) > 0:
         elementToRemove = self.heap[0]
         self.heap[0] = self.heap[-1]
         self.heap.pop()
         self.prelocateDown(0)
         return elementToRemove
      return None


   def prelocateDown(self, idx):
      n = len(self.heap)
      leftChildIdx = (idx * 2) + 1
      while leftChildIdx < n:
         rightChildIdx = (idx * 2) + 2
         if rightChildIdx < n and self.heap[rightChildIdx][1] > self.heap[leftChildIdx][1]:
            idxToSwap = rightChildIdx
         else:
            idxToSwap = leftChildIdx
         
         if self.heap[idxToSwap][1] > self.heap[idx][1]:
            self.swap(idxToSwap, idx)
            idx = idxToSwap
            leftChildIdx = (idx * 2) + 1
         else:
            return

   def prelocateUp(self, idx):
      while idx != 0:
         parentIdx = (idx - 1)//2
         if self.heap[parentIdx][1] < self.heap[idx][1]:
            self.swap(idx, parentIdx)
            idx = parentIdx
         else: return

   def swap(self, i, j):
      self.heap[i], self.heap[j] = self.heap[j], self.heap[i]



def reorganize(s):
   charFreq = {}
   for char in s:
      if char not in charFreq:
         charFreq[char] = 0
      charFreq[char] += 1
   freqList = [[char, charFreq[char]]  for char in charFreq]
   result = []
   heap = MaxHeap(freqList)
   prevChar = None
   while heap.size() > 0:
      curChar = heap.remove()
      result.append(curChar[0])
      curChar[1] -= 1
      if curChar[1] == 0:
         curChar = None
      if prevChar is not None:
         heap.insert(prevChar)
      prevChar = curChar
   return "".join(result)
   

print(reorganize("aaabc"))
      