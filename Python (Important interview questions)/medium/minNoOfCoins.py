# O(n * amount) time | O(amount) space
def minCoins(coins=[], amount=0):
    noOfCoins = [float('inf') for _ in range(amount + 1)]
    noOfCoins[0] = 0
    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                noOfCoins[current_amount] = min(
                    noOfCoins[current_amount], 1 + noOfCoins[current_amount - coin])
    print(noOfCoins)
    return noOfCoins[-1] if noOfCoins[-1] != float('inf') else -1


coins = [1, 2, 4, 5]
amount = 10

print(minCoins(coins, amount))
   