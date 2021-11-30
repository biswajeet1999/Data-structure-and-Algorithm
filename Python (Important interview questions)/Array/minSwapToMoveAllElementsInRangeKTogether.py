
# O(n) time | O(1) space
def minSwaps(array, k):
   curLength = 0
   maxLength = 0
   prevIdx = -1
   TotalElementsInRangeK = 0
   for idx, num in enumerate(array):
      if num > k:
         curLength = 0
         continue
      TotalElementsInRangeK += 1
      curLength += 1
      prevIdx = idx
      maxLength = max(maxLength, curLength)
   return TotalElementsInRangeK  - maxLength

print(minSwaps([2, 1, 5, 6, 3], 3))
print(minSwaps([2, 7, 9, 5, 8, 7, 4], 6))
print(minSwaps([1, 2, 10, 11, 12, 8, 9, 8, 13, 2], 9))