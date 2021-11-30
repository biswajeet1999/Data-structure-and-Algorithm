def maxProfit(prices):
   if len(prices) == 0:
      return 0
   localMin = prices[0]
   profit = 0
   for idx in range(1, len(prices)):
      price = prices[idx]
      if price < localMin:
         localMin = price
      else:
         profit = max(profit, price - localMin)
   return profit