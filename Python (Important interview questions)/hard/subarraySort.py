#  O(n) time | O(1) space
def getMinMax(array, leftUnsortedIdx, rightUnsortedIdx):
   minn = array[leftUnsortedIdx]
   maxx = array[leftUnsortedIdx]
   i = leftUnsortedIdx + 1
   while i <= rightUnsortedIdx:
      if array[i] < minn:
         minn = array[i]
      elif array[i] > maxx:
         maxx = array[i] 
      i += 1
   return minn, maxx

#  O(n) time | O(1) space
def subarraySort(array = []):
   length = len(array)
   leftSortedIdx = 0
   rightSortedIdx = length - 1

   while leftSortedIdx < length - 1 and array[leftSortedIdx] <= array[leftSortedIdx + 1]:
      leftSortedIdx += 1
   if leftSortedIdx == length - 1:
      return [-1, -1]

   while rightSortedIdx > 0 and array[rightSortedIdx] >= array[rightSortedIdx - 1]:
      rightSortedIdx -= 1

   minInUnsortedSubarray, maxInUnsortedSubarray = getMinMax(array, leftSortedIdx + 1, rightSortedIdx - 1)

   while rightSortedIdx < length and minInUnsortedSubarray >= array[rightSortedIdx]:
      minInUnsortedSubarray = array[rightSortedIdx]
      rightSortedIdx += 1
   
   while leftSortedIdx >= 0 and maxInUnsortedSubarray <= array[leftSortedIdx]:
      maxInUnsortedSubarray = array[leftSortedIdx]
      leftSortedIdx -= 1

   while leftSortedIdx >= 0 and array[leftSortedIdx] > minInUnsortedSubarray:
      leftSortedIdx -= 1
   
   while rightSortedIdx < length and array[rightSortedIdx] < maxInUnsortedSubarray:
      rightSortedIdx += 1

   return [leftSortedIdx + 1, rightSortedIdx - 1]   

array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(subarraySort(array))