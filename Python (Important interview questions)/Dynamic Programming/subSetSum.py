def subSetSum(arr):
   totalSum = sum(arr)
   if totalSum %2 == 1:
      return False
   targetSum = totalSum // 2

   dp = [[False for summ in range(targetSum +1)] for _ in range(len(arr) +1)]
   for row in range(len(arr) +1):
      dp[row][0] = True
   
   for row in range(1, len(arr) + 1):
      for col in range(1, targetSum + 1):
         curNum = arr[row - 1]
         if curNum > col:
            dp[row][col] = dp[row - 1][col]
         else:
            dp[row][col] = dp[row - 1][col] or dp[row - 1][col - curNum]
   return dp[-1][-1]

print(subSetSum([1, 5, 11, 5]))