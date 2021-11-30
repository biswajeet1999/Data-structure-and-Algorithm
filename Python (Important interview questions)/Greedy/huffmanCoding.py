class Node:
   def __init__(self, char, freq):
      self.char = char
      self.freq = freq
      self.left = self.right = None

class MinHeap:
   def __init__(self, charWithFreq):
      self.arr = []
      self.size = 0
      self.buildHeap(charWithFreq)
   
   def buildHeap(self, charWithFreq):
      self.arr = list(map(lambda x: Node(x[0], x[1]), charWithFreq))
      self.size = len(self.arr)
      for idx in range((self.size//2)-1, -1, -1):
         self.prelocateDown(idx)
      
   def prelocateDown(self, idx):
      leftIdx = idx*2 + 1
      while leftIdx < self.size:
         rightIdx = idx*2 + 2
         if rightIdx >= self.size or self.arr[rightIdx].freq > self.arr[leftIdx].freq:
            idxToSwap = leftIdx
         else:
            idxToSwap = rightIdx
         if self.arr[idx].freq <= self.arr[idxToSwap].freq:
            return
         swap(self.arr, idx, idxToSwap)
         idx = idxToSwap
         leftIdx = idx*2 + 1

   def prelocateUp(self, idx):
      while idx > 0:
         parent = (idx - 1) //2
         if self.arr[idx].freq < self.arr[parent].freq:
            swap(self.arr, parent, idx)
            idx = parent
         else:
            return
   
   def pop(self):
      swap(self.arr, 0, self.size - 1)
      nodeToRemove = self.arr.pop()
      self.size -= 1
      self.prelocateDown(0)
      return nodeToRemove

   def insert(self, node):
      self.arr.append(node)
      self.size += 1
      self.prelocateUp(self.size-1)
   
   def getLength(self):
      return self.size


def swap(arr, i, j):
   arr[i], arr[j] = arr[j], arr[i]

def huffmanCoding(s, freq):
   charWithFreq = [(s[i], freq[i]) for i in range(len(s))]
   minHeap = MinHeap(charWithFreq)
   while minHeap.getLength() > 1:
      node1 = minHeap.pop()
      node2 = minHeap.pop()
      newNode = Node("*", node1.freq + node2.freq)
      newNode.left = node1
      newNode.right = node2
      minHeap.insert(newNode)
   root = minHeap.pop()
   path = []
   result = {}
   preorder(root, result, path)
   return result

def preorder(root, result, path):
   if root is None:
      return
   if root.left is None and root.right is None:
      result[root.char] = "".join(path)
      return
   path.append('0')
   preorder(root.left, result, path)
   path.pop()
   path.append('1')
   preorder(root.right, result, path)
   path.pop()


print(huffmanCoding("abcdef", [5, 9, 12, 13, 16, 45]))