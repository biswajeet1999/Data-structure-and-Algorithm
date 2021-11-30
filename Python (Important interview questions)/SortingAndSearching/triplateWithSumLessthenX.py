def getTriplate(arr, targetSum):
   arr.sort()
   count = 0
   for i in range(len(arr)):
      j = i + 1
      k = len(arr) - 1
      while j < k:
         if arr[i] + arr[j] + arr[k] >= targetSum:
            k -= 1
         else:
            count += (k-j)
            j += 1
   return count

print(getTriplate([1, 2, 3, 4], 100))