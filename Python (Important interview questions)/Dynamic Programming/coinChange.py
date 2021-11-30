# (2^m) time | O(n) space
# m = len(coins)
# def coinChange(n, coins):
#    return coinChangeHelper(n, coins, len(coins) - 1)

# def coinChangeHelper(money, coins, idx):
#    if money < 0:
#       return 0
#    if money == 0:
#       return 1
#    if idx < 0:
#       return 0
#                               # without using given coin   +   using given coin
#    return coinChangeHelper(money - coins[idx], coins, idx) + coinChangeHelper(money, coins, idx - 1)


# O(m*n) time | O(n) space
def coinChange(n, coins):
   noOfWays = [0 for _ in range(n+1)]
   noOfWays[0] = 1 # base case: no of ways we can make 0 using any coin set

   for coin in coins:
      for amount in range(1, n+1):
         if coin <= amount:
            #        without using given coin   +   using given coin            
            noOfWays[amount] = noOfWays[amount] + noOfWays[amount - coin]
   return noOfWays[-1]

print(coinChange(4, [1, 2, 3]))