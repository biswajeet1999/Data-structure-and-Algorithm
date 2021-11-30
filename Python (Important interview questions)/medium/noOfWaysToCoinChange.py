# O(n*amount) time | O(amount) space
# assuming coins are given in assending order
def noOfWaysToChangeCoin(coins = [], amount = 0):
    make_change = [0 for _ in range(amount+1)]
    make_change[0] = 1
    
    for coin in coins:
        for current_amount in range(1, amount+1):
            if coin <= current_amount:
                make_change[current_amount] += make_change[current_amount - coin]

    
    print(make_change)
    return make_change[-1]




coins = [1, 5, 10, 25]
amount = 10

# coins = [2, 4]
# amount = 7
print(noOfWaysToChangeCoin(coins, amount))