# O(n*m) time | O(n*m) space
def lcs(str1, str2):
   n = len(str1)
   m = len(str2)

   lcsTable = [[0 for col in range(n+1)] for row in range(m+1)]

   for row in range(1, m+1):
      for col in range(1, n+1):
         lcsTable[row][col] = 1+lcsTable[row-1][col-1] if str1[col-1] ==  str2[row-1] else max(lcsTable[row-1][col], lcsTable[row][col-1])
   return lcsTable[-1][-1]


print(lcs("ABCDGH", "AEDFHR"))