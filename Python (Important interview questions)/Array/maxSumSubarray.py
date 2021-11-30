def maxSumSubarray(array):
   maxSum = array[0]
   currentSum = array[0]

   for i in range(1, len(array)):
      currentSum = max(currentSum + array[i], array[i])
      maxSum = max(maxSum, currentSum)
   return maxSum


array = [1,2,3,-2,5]
print(maxSumSubarray(array))

array = [-1,-2,-3,-4]
print(maxSumSubarray(array))