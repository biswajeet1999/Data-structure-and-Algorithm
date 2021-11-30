def countWord(matrix, p):
   count = 0
   for i in range(len(matrix)):
      for j in range(len(matrix[0])):
         if matrix[i][j] == p[0]:
            count += countWordHelper(matrix, i, j, p, 0)
   return count

def countWordHelper(matrix, i, j, p, pIdx):
   rows = len(matrix)
   cols = len(matrix[0])
   patternLength = len(p)
   
   if i < 0 or i >= rows:
      return 0
   if j < 0 or j >= cols:
      return 0
   if pIdx == patternLength - 1 and matrix[i][j] == p[pIdx]:
      return 1
   if p[pIdx] != matrix[i][j]:
      return 0
   
   return (countWordHelper(matrix, i - 1, j, p, pIdx + 1) 
         + countWordHelper(matrix, i + 1, j, p, pIdx + 1) 
         + countWordHelper(matrix, i, j - 1, p, pIdx + 1) 
         + countWordHelper(matrix, i, j + 1, p, pIdx + 1))


matrix = [
            ["D","D","D","G","D","D"],
            ["B","B","D","E","B","S"],
            ["B","S","K","E","B","K"],
            ["D","D","D","D","D","E"],
            ["D","D","D","D","D","E"],
            ["D","D","D","D","D","G"]
]

print(countWord(matrix, "GEEKS"))