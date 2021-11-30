# O(n^2) time | O(n^2) space
def getMaxPoint(points):
   n = len(points)
   dp = [[0 for col in range(n)] for row in range(n)]
   
   for gap in range(0, n):
      row = 0
      col = row + gap
      while row < n and col < n:
         if row == col:
            dp[row][col] = points[row]
         elif row+1 == col:
            dp[row][col] = max(points[row], points[col])
         else:
            choice1 = points[row] + min(dp[row+2][col], dp[row+1][col-1])
            choice2 = points[col] + min(dp[row][col-2], dp[row+1][col-1])
            dp[row][col] = max(choice1, choice2)
         row += 1
         col = row + gap
   return dp[0][-1]

print(getMaxPoint([20, 30, 2, 10]))