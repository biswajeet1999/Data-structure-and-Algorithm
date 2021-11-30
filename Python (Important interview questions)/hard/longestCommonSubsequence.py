# O(nm*min(m,n)) time | O(nm*min(n, m)) space
# def LCS(str1, str2):
#    n = len(str1)
#    m = len(str2)
#    lcs = [[[] for j in range(m + 1)] for i in range(n + 1)]
#    for i in range(1, n+1):
#       for j in range(1, m+1):
#          if str1[i-1] == str2[j-1]:
#             lcs[i][j] = lcs[i-1][j-1] + [str1[i-1]]
#          else:
#             lcs[i][j] = lcs[i-1][j] if len(lcs[i-1][j]) > len(lcs[i][j-1]) else lcs[i][j-1]
#    return "".join(lcs[n][m])

# O(m+n) time | O(min(m,n)) space
def buildSequence(lcs, string):
   curRow = len(lcs) - 1
   curCol = len(lcs[0]) - 1
   commonStr = ""
   while curRow > 0 and curRow > 0:
      if lcs[curRow][curCol] == lcs[curRow - 1][curCol]:
         curRow -= 1
      elif lcs[curRow][curCol] == lcs[curRow][curCol -1]:
         curCol -= 1
      else:
         commonStr = string[curRow - 1] + commonStr
         curRow -= 1
         curCol -= 1
   return commonStr

# O(nm) time | O(nm) space
def LCS(str1, str2):
   n = len(str1)
   m = len(str2)
   lcs = [[0 for j in range(m + 1)] for i in range(n + 1)]
   for i in range(1, n+1):
      for j in range(1, m+1):
         if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
         else:
            lcs[i][j] = lcs[i-1][j] if lcs[i-1][j] > lcs[i][j-1] else lcs[i][j-1]
   return buildSequence(lcs, str1)




str1 = "zxvvyzw"
str2 = "xkykzpw"
print(LCS(str1, str2))