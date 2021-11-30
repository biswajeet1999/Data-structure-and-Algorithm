# worst O(n^2) time | O(n) space
# avg O(n) time | O(n) space
def findAllZeroSumSubarray(arr):
   sumCache = {}
   summ = 0
   result = []
   for i in range(len(arr)):
      summ += arr[i]
      if summ == 0:
         result.append((0, i))

      if summ in sumCache:
         sumIdxs = sumCache[summ]
         for idx in sumIdxs:
            result.append((idx+1 , i))
      if summ not in sumCache:
         sumCache[summ] = []
      sumCache[summ].append(i)
   return result
         

print(findAllZeroSumSubarray([6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]))