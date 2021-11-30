# O(capacity * m) time | O(capacity * m) space
def knapSack(capacity, weights, profits):
   dp = [[0 for i in range(capacity + 1)] for _ in range(len(weights) + 1)]
   
   for col in range(1, capacity + 1):
      for row in range(1, len(weights)+1):
         curWeight = weights[row - 1]
         curProfit = profits[row - 1]
         if curWeight <= col:
            dp[row][col] = max( curProfit + dp[row-1][col-curWeight], dp[row-1][col])
         else:
            dp[row][col] = dp[row-1][col]
   return getItems(dp, dp[-1][-1], profits, weights)

def getItems(dp, maxProfit, profits, weights):
   rowIdx = len(dp) - 1
   colIdx = len(dp[0]) - 1
   items = []
   while maxProfit > 0:
      if dp[rowIdx][colIdx] == maxProfit and dp[rowIdx - 1][colIdx] != dp[rowIdx][colIdx]:
         items.append(weights[rowIdx-1])
         maxProfit -= profits[rowIdx-1]
         rowIdx -= 1
      elif dp[rowIdx][colIdx] == maxProfit and dp[rowIdx - 1][colIdx] == dp[rowIdx][colIdx]:
         rowIdx -= 1
      else:
         colIdx -= 1
   return items


# Driver code
val = [120, 60, 100]
wt = [30, 10, 20]
W = 50
print(knapSack(W, wt, val))