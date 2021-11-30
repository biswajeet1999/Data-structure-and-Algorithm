# def lrs(s):
#    return lrsUtil(s, 0, 0)

# def lrsUtil(s, i, j):
#    if i == len(s) or j == len(s):
#       return 0
#    if s[i] == s[j] and i != j:
#       return 1 + lrsUtil(s, i+1, j+1)
#    return max(lrsUtil(s, i+1, j), lrsUtil(s, i, j+1))

def lrs(s):
   n = len(s)
   m = len(s)

   lcsTable = [[0 for col in range(n+1)] for row in range(m+1)]

   for row in range(1, m+1):
      for col in range(1, n+1):
         lcsTable[row][col] = 1+lcsTable[row-1][col-1] if s[col-1] ==  s[row-1] and row != col else max(lcsTable[row-1][col], lcsTable[row][col-1])
   return lcsTable[-1][-1]


print(lrs('AABEBCDD'))