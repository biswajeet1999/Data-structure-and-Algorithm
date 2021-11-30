# O(kn^2) time | O(nk) space
# def maxProfit(price, k):
#    dp = [[0 for col in range(len(price))] for _ in range(k+1)]

#    for trans in range(1, k+1):
#       for day in range(1, len(price)):
#          for prevDay in range(0, day):
#             dp[trans][day] = max(dp[trans][day], price[day] - price[prevDay] + dp[trans - 1][prevDay])
#          dp[trans][day] = max(dp[trans][day - 1], dp[trans][day])
#    return dp[-1][-1]

# O(kn) time | O(nk) space
def maxProfit(price, k):
   dp = [[0 for col in range(len(price))] for _ in range(k+1)]
   maxProfitSoFar = -float("inf")
   for trans in range(1, k+1):
      for day in range(1, len(price)):
         maxProfitSoFar = max(maxProfitSoFar, -price[day-1] + dp[trans-1][day-1])
         dp[trans][day] = max(dp[trans][day-1], maxProfitSoFar + price[day])
   return dp[-1][-1]

price = [2, 30, 15, 10, 8, 25, 80]
k = 2
print(maxProfit(price, k))