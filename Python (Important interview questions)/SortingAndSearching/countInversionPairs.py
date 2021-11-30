# O(nlogn) time | O(n) space
def countInversionPair(arr):
   return mergeSortModified(arr, 0, len(arr) - 1)

def mergeSortModified(arr, start, end):
   if start >= end:
      return 0
   
   midIdx = (start + end)//2

   leftSubarrayCount = mergeSortModified(arr, start, midIdx)
   rightSubarrayCount = mergeSortModified(arr, midIdx + 1, end)
   countAfterMerging = merge(arr, start, end, midIdx)
   
   return leftSubarrayCount + rightSubarrayCount + countAfterMerging

def merge(arr, start, end, mid):
   count = 0
   temp = []

   i = start
   j = mid + 1

   while i <= mid and j <= end:
      if arr[i] < arr[j]:
         temp.append(arr[i])
         i += 1
      elif arr[i] > arr[j]:
         count += mid - i + 1
         temp.append(arr[j])
         j += 1

   while i <= mid:
      temp.append(arr[i])
      i += 1
   while j <= end:
      temp.append(arr[j])
      j += 1

   i = start
   for element in temp:
      arr[i] = element
      i += 1
   return count


print(countInversionPair([2, 4, 1, 3, 5]))
print(countInversionPair([2, 3, 4, 5, 6]))
