def getOptimalBSTCost(freq):
   n = len(freq)
   dp = [[0 for col in range(n)] for row in range(n)]

   for gap in range(0, n):
      i = 0
      j = i + gap
      while i < n and j < n:
         if gap == 0:
            dp[i][j] = freq[i]
         elif gap == 1:
            dp[i][j] = min(freq[i]+2*freq[j], 2*freq[i]+freq[j]) 
         else:
            freqSum = 0
            minCost = float('inf')
            for f in range(i, j+1):
               freqSum += freq[f]
            for k in range(i, j+1):
               leftTreeCost = 0 if k-1 < 0 else dp[i][k-1]
               rightTreeCost = 0 if k+1 > j else dp[k+1][j]
               totalCost = leftTreeCost + rightTreeCost + freqSum
               minCost = min(minCost, totalCost)
            dp[i][j] = minCost
         i+=1
         j=i+gap
   return dp[0][-1]

print(getOptimalBSTCost([3, 1, 2, 1]))


