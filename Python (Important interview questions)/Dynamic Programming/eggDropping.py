def getMInAttempt(f, e):
   dp = [[0 for col in range(1+f)] for row in range(1+e)]
   for floor in range(1, f+1):
      dp[1][floor] = floor
   for egg in range(1, 1+e):
      dp[egg][1] = 1
   
   for egg in range(2, e+1):
      for floor in range(2, f+1):
         minAttempt = float('inf')
         for curFloor in range(1, floor+1):
            maxAttempt = max(dp[egg-1][curFloor-1], dp[egg][floor-curFloor])
            minAttempt = min(minAttempt, maxAttempt)
         dp[egg][floor] = minAttempt + 1
   printDp(dp)
   return dp[-1][-1]

def printDp(dp):
   for row in dp:
      print(row)

print(getMInAttempt(10, 2))