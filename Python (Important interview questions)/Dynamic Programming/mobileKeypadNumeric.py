def getCount(n):
   neighbours = {
      1: [1, 2, 4],
      2: [2, 1, 3, 5],
      3: [3, 2, 6],
      4: [4, 1, 5, 7],
      5: [5, 2, 4, 6, 8],
      6: [6, 3, 5, 9],
      7: [7, 4, 8],
      8: [8, 0, 5, 7, 9],
      9: [9, 8, 6],
      0: [0, 8]
   }
   dp = [[0 for num in range(10)] for t in range(n+1)]
   for num in range(10):
      dp[1][num] = 1
   
   for t in range(2, n+1):
      for num in range(0, 10):
         for neigh in neighbours[num]:
            dp[t][num] += dp[t-1][neigh]
   
   return sum(dp[-1])

print("Count for numbers of length 1:", getCount(1))
print("Count for numbers of length 2:", getCount(2))
print("Count for numbers of length 3:", getCount(3))
print("Count for numbers of length 4:", getCount(4))
print("Count for numbers of length 5:", getCount(5))
