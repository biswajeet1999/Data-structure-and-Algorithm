def maxProfit(w, p, maxWeight):
   dp = [[0 for col in range(maxWeight+1)] for row in range(len(w) + 1)]

   for row in range(1, len(w) + 1):
      for col in range(1, maxWeight+1):
         dp[row][col] = dp[row-1][col]
         if w[row-1] <= col:
            dp[row][col] = max(dp[row][col], p[row-1]+dp[row][col-w[row-1]])
   # printDp(dp)
   return dp[-1][-1]

def printDp(dp):
   for row in dp:
      print(row)

print(maxProfit([5, 10, 15], [10, 30, 20], 100))
print(maxProfit([2, 1], [1, 1], 3))
print(maxProfit([1, 3, 4, 5], [1, 4, 5, 7], 8))