# O(n) time | O(n) space
# def getMinCostAssambly(a, t, s, e):
   # dp = [[0 for cost in range(len(a[0]))] for _ in range(2)]

   # dp[0][0] = s[0] + a[0][0]
   # dp[1][0] = s[1] + a[1][0]

   # for i in range(1, len(a[0])):
   #    dp[0][i] = a[0][i] + min(dp[0][i-1], dp[1][i-1] + t[1][i])
   #    dp[1][i] = a[1][i] + min(dp[1][i-1], dp[0][i-1] + t[0][i])
   # return min(e[0] + dp[0][-1], e[1] + dp[1][-1])

# with path
def getMinCostAssambly(a, t, s, e):
   dp = [[0 for cost in range(len(a[0]))] for _ in range(2)]
   path = [[None for parent in range(len(a[0]))] for _ in range(2)]

   dp[0][0] = s[0] + a[0][0]
   dp[1][0] = s[1] + a[1][0]

   for i in range(1, len(a[0])):
      if dp[0][i-1] < dp[1][i-1] + t[1][i]:
         dp[0][i] = a[0][i] + dp[0][i-1]
         path[0][i] = 0
      else:
         dp[0][i] = a[0][i] + dp[1][i-1] + t[1][i]
         path[0][i] = 1

      if dp[1][i-1] < dp[0][i-1] + t[0][i]:
         dp[1][i] = a[1][i] + dp[1][i-1]
         path[1][i] = 1
      else:
         dp[1][i] = a[1][i] + dp[0][i-1] + t[0][i]
         path[1][i] = 0

   if e[0] + dp[0][-1] < e[1] + dp[1][-1]:
      printPath(path, 0)
   else:
      printPath(path, 1)

   return min(e[0] + dp[0][-1], e[1] + dp[1][-1])
 
def printPath(path, end):
   n = len(path[0])
   result = [end]
   assamblyLine = end
   for idx in range(n-1, 0, -1):
      result.append(path[assamblyLine][idx])
      assamblyLine = path[assamblyLine][idx]
   print(result[::-1])


a = [[4, 5, 3, 2],
     [2, 10, 1, 4]]
t = [[0, 7, 4, 5],
     [0, 9, 2, 8]]
s = [10, 12]
e = [18, 7]
 
print(getMinCostAssambly(a, t, s, e))