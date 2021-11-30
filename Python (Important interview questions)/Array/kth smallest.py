# AVG:- O(n) time | O(1) space
def kthSmallest(array, k):
   return quickSelect(array, 0, len(array) - 1, k)

def quickSelect(array, start, end, k):
   while start <= end:
      pivotIdx = partation(array, start, end)
      if pivotIdx == k:
         return array[pivotIdx]
      elif k > pivotIdx:
         start = pivotIdx + 1
      else:
         end = pivotIdx - 1

def partation(array, start, end):
   pivotIdx = start
   for idx in range(start+1, end+1):
      if array[idx] < array[pivotIdx]:
         if idx - pivotIdx > 1:
            swap(array, idx, pivotIdx+1)
         swap(array, pivotIdx, pivotIdx + 1)
         pivotIdx += 1
   return pivotIdx

def swap(array, i, j):
   array[i], array[j] = array[j], array[i]


array = [4, 8, 1, 2, 5, 0]
print(kthSmallest(array, 0))