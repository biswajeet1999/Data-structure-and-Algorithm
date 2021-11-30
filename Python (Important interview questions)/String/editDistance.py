def minEdits(str1, str2):
   n = len(str1)
   m = len(str2)

   prevRow = [i for i in range(m + 1)]
   curRow = []
   for row in range(1, n+1):
      for col in range(0, m+1):
         if col == 0:
            curRow.append(col)
         elif str1[row - 1] == str2[col - 1]:
            curRow.append(prevRow[col - 1])
         else:
            curRow.append(1 + min( curRow[col - 1], prevRow[col], prevRow[col - 1]))
      prevRow = curRow
      curRow = []
   return prevRow[-1]

str1 = "cat"
str2 = "cut"
print(minEdits(str1, str2))