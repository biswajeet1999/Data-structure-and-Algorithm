def getMaxProfit(prices, k):
   if k == 0 or len(prices) == 0:
      return 0
   profits = [[0 for p in prices] for t in range(k+1)]
   for t in range(1, k+1):
      maxThusFar = -float('inf')
      for p in range(1, len(prices)):
         maxThusFar = max(maxThusFar, profits[t - 1][p - 1] - prices[p - 1])
         profits[t][p] = max(maxThusFar + prices[p], profits[t][p-1])
   return profits[-1][-1]
