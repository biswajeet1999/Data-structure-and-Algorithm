# O(3^n) time | O(n) space
# def canAWin(n, x, y, turn):
#    if turn == 1 and n == 0:
#       return True
#    if n == 0:
#       return False
   
#    aCanWin = False
   
#    aCanWin = canAWin(n -1, x, y, 1-turn)
#    if (x > 0 and x <= n) and not aCanWin:
#       aCanWin = canAWin(n-x, x, y, 1-turn)
#    if (y > 0 and y <= n) and not aCanWin:
#       aCanWin = canAWin(n-y, x, y, 1-turn)
#    return aCanWin

# n = 5
# x = 3
# y = 4
# print(canAWin(n, x, y, 0))

# n = 2
# x = 3
# y = 4
# print(canAWin(n, x, y, 0))

def canAWin(n, x, y):
   dp = [False for _ in range(n+1)]
   dp[0] = False
   dp[1] = True

   for i in range(2, n+1):
      if i-1 >= 0 and dp[i-1] == False:
         dp[i] = True
      if i-x >= 0 and dp[i-x] == False:
         dp[i] = True
      if i-y >= 0 and dp[i-y] == False:
         dp[i] = True
   return dp[-1]

n = 5
x = 3
y = 4
print(canAWin(n, x, y))

n = 2
x = 3
y = 4
print(canAWin(n, x, y))