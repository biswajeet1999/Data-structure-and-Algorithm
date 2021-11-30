# def lcs(s1, s2):
#    return lcsHelper(s1, 0, len(s1) - 1, s2, 0, len(s2) - 1)

# def lcsHelper(s1, startIdx1, endIdx1, s2, startIdx2, endIdx2):
#    if endIdx1 < startIdx1 or endIdx2 < startIdx2:
#       return 0
   
#    if s1[startIdx1] == s2[startIdx2]:
#       return 1 + lcsHelper(s1, startIdx1 + 1, endIdx1, s2, startIdx2 + 1, endIdx2)
#    return max(lcsHelper(s1, startIdx1 + 1, endIdx1, s2, startIdx2, endIdx2), lcsHelper(s1, startIdx1, endIdx1, s2, startIdx2 + 1, endIdx2))



def lcs(s1, s2):
   rows = len(s1) + 1
   cols = len(s2) + 1
   dp = [[0 for i in range(cols)] for j in range(rows)]

   for i in range(1, rows):
      for j in range(1, cols):
         if s1[i -1] == s2[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
         else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
   return dp[-1][-1]


s1 = "ABCDGH"
s2 = "AEDFHR"
print(lcs(s1, s2))