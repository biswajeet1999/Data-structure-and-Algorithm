class HeapNode:
   def __init__(self, rowNum, colNum):
      self.rowNum = rowNum
      self.colNum = colNum

def createHeap(totalRows):
   return [HeapNode(row, 0) for row in range(totalRows)]

def swap(heap, i, j):
   heap[i], heap[j] = heap[j], heap[i]

def prelocateDown(heap, idx, mat):
   leftChildIdx = idx*2 + 1
   while leftChildIdx < len(heap):
      rightChildIdx = idx*2 + 2
      leftChild = heap[leftChildIdx]
      rightChild = heap[rightChildIdx] if rightChildIdx < len(heap) else None
      if rightChildIdx >= len(heap) or (mat[leftChild.rowNum][leftChild.colNum] < mat[rightChild.rowNum][rightChild.colNum]):
         elementToSwap = leftChildIdx
      else:
         elementToSwap = rightChildIdx
      swapNumber = mat[heap[elementToSwap].rowNum][heap[elementToSwap].colNum]
      curNumber = mat[heap[idx].rowNum][heap[idx].colNum]
      if curNumber > swapNumber:
         swap(heap, idx, elementToSwap)
         idx = elementToSwap
         leftChildIdx = idx*2 + 1
      else:
         return

def deleteTop(heap, mat):
   eleToDelete = heap[0]
   deletedElementRow = eleToDelete.rowNum
   deletedElementCol = eleToDelete.colNum

   isLast = deletedElementCol == len(mat[deletedElementRow]) - 1
   # BUG: fix this
   if isLast:
      elementToMoveTop = heap.pop()
   else:
      elementToMoveTop = HeapNode(deletedElementRow, deletedElementCol + 1)

   if len(heap) == 0:
      heap.append(elementToMoveTop)
   else:
      heap[0] = elementToMoveTop
   prelocateDown(heap, 0, mat) 
   return mat[deletedElementRow][deletedElementCol]


def buildHeap(mat):
   heapArray = createHeap(len(mat))
   idxToStart = (len(mat) - 1) // 2
   for idx in range(idxToStart, -1, -1):
      prelocateDown(heapArray, idx, mat)
   return heapArray

def sortMatrix(mat):
   heap = buildHeap(mat)
   result = []
   while len(heap) > 0:
      element = deleteTop(heap, mat)
      result.append(element)
   return result


mat = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
print(sortMatrix(mat))