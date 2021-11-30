def maxMin(prices, k):
   prices.sort()
   noOfCandies = len(prices)
   noOfCandiesToBuy = 0
   while noOfCandies > 0:
      noOfCandiesToBuy += 1
      noOfCandies -= (k + 1)
   minPrice = sum(prices[0: noOfCandiesToBuy])
   maxPrice = sum(prices[len(prices) - noOfCandiesToBuy: len(prices)])
   return (minPrice, maxPrice)

print(maxMin([3, 2, 1, 4], 2))

