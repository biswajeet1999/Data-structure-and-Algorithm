

def maxProfit(weights, profits, capacity):
   density = [profits[i]/weights[i] for i in range(len(weights))]
   items = [(weights[idx], profits[idx], density[idx]) for idx in range(len(weights))]
   items.sort(key=lambda x: x[2], reverse=True)
   totalProfit = 0
   for item in items:
      if capacity == 0:
         break
      weight = item[0]
      profit = item[1]
      profitPerWeight = item[2]
      if capacity >= weight:
         totalProfit += profit
         capacity -= weight
      else:
         totalProfit += profitPerWeight * capacity
         capacity = 0
   return totalProfit


print(maxProfit([10, 40, 20, 30], [60, 40, 100, 120], 50))