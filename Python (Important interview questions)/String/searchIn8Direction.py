def countWord(matrix, p):
   count = 0
   for i in range(len(matrix)):
      for j in range(len(matrix[0])):
         if matrix[i][j] == p[0]:
            count += countWordHelper(matrix, i, j, p, 0)
   return count

def countWordHelper(matrix, i, j, p, pIdx):
   pass


matrix = [
            ["D","D","D","G","D","D"],
            ["B","B","D","E","B","S"],
            ["B","S","K","E","B","K"],
            ["D","D","D","D","D","E"],
            ["D","D","D","D","D","E"],
            ["D","D","D","D","D","G"]
]

print(countWord(matrix, "GEEKS"))