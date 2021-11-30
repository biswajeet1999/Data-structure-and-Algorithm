# O(n^2) time | O(n^2) space
def getMinCut(s):
   n = len(s)
   cuts = [float('inf') for _ in range(n)]
   palindromicDp = [[False for col in range(n)] for row in range(n)]

   # fill pallendromic dp
   for gap in range(0, n):
      i = 0
      j = i + gap
      while i < n and j < n:
         if gap == 0:
            palindromicDp[i][j] = True
         elif gap == 1:
            if s[i] == s[j]:
               palindromicDp[i][j] = True
         else:
            if s[i] == s[j] and palindromicDp[i+1][j-1]:
               palindromicDp[i][j] = True
         i+=1
         j=i+gap
   
   # find min cut
   cuts[0] = 1
   for i in range(1, n):
      for j in range(i, -1, -1):
         isPalendrom = palindromicDp[j][i]
         if isPalendrom == False:
            continue
         prefixCuts = 0 if j == 0 else cuts[j-1]
         cuts[i] = min(cuts[i], 1+prefixCuts)
   return cuts[-1]-1

print(getMinCut("geek"))
print(getMinCut("aaaa"))
print(getMinCut("abcde"))
      