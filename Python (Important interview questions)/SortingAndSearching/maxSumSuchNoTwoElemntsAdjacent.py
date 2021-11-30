# O(n) time | O(n) space
# def getMaxSum(arr):
#    return getMaxSumHelper(arr, 0)

# def getMaxSumHelper(arr, idx, cache={}):
#    if idx in cache:
#       return cache[idx]
#    if idx >= len(arr):
#       cache[idx] = 0
#       return 0
#    cache[idx] = max(arr[idx] + getMaxSumHelper(arr, idx + 2), getMaxSumHelper(arr, idx+1))
#    return cache[idx] 

def getMaxSum(arr):
   if len(arr) == 1:
      return arr[0]
   sumTillNow = [0 for _ in arr]
   sumTillNow[0] = arr[0]
   sumTillNow[1] = (max(arr[0], arr[1]))
   for idx in range(2, len(arr)):
      sumTillNow[idx] = max(arr[idx]+sumTillNow[idx-2], sumTillNow[idx-1])
   return sumTillNow[-1]

print(getMaxSum([5, 5, 10, 100, 10, 5]))