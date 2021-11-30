# Ref:- GeeksForGeeks
# O(n^2) time | O(n^2) space
def getMaxDiff(matrix):
   n = len(matrix)
   maxMat = [[0 for j in range(n)] for _ in range(n)]
   maxMat[-1][-1] = matrix[-1][-1]

   maxVal = maxMat[n-1][n-1]
   for col in range(n-2, -1, -1):
      if matrix[n-1][col] > maxVal:
         maxVal = matrix[n-1][col]
      maxMat[n-1][col] = maxVal

   maxVal = maxMat[n-1][n-1]
   for row in range(n-2, -1, -1):
      if matrix[row][n-1] > maxVal:
         maxVal = matrix[row][n-1]
      maxMat[row][n-1] = maxVal

   diff = -float('inf')
   for i in range(n-2, -1, -1):
      for j in range(n-2, -1, -1):
         if diff < maxMat[i+1][j+1] - matrix[i][j]:
            diff = maxMat[i+1][j+1] - matrix[i][j]
         
         maxMat[i][j] = max(matrix[i][j], maxMat[i][j+1], maxMat[i+1][j])

   return diff



mat = [[ 1, 2, -1, -4, -20 ],
       [ -8, -3, 4, 2, 1 ], 
       [ 3, 8, 6, 1, 3 ],
       [ -4, -1, 1, 7, -6 ],
       [ 0, -4, 10, -5, 1 ]]

print(getMaxDiff(mat))