def findPair(arr, diff):
   n = len(arr)
   arr.sort()
   i = 0
   j = n - 1

   while i < j:
      curDiff = arr[j] - arr[i]
      if curDiff - diff == 0:
         return (arr[i], arr[j])
      if curDiff - diff < 0:
         return (-1, -1)
      rightDiff = arr[j] - arr[i+1]
      leftDiff = arr[j-1] - arr[i]
      if rightDiff - diff > leftDiff - diff and (leftDiff - diff) >= 0:
         j -= 1
      else:
         i += 1

arr = [1, 8, 30, 40, 100]  
n = 60
print(findPair(arr, n) )

arr = [5, 20, 3, 2, 50, 80]  
n = 78
print(findPair(arr, n) )

arr = [90, 70, 20, 80, 50]  
n = 45
print(findPair(arr, n) )