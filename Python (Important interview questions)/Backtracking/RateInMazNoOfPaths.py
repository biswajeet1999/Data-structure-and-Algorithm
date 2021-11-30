def countPath(mat):
   visitedMat = [[False for col in row] for row in mat]
   count = [0]
   allPaths = []
   curPath = []
   countPathHelper(mat, visitedMat, 0, 0, count, allPaths, curPath)
   return count[0], allPaths

# matrix is always n*n
def countPathHelper(mat, visitedMat, curRow, curCol, count, allPaths, curPath):
   n = len(mat)
   if curRow < 0 or curRow >= n or curCol < 0 or curCol >= n:
      return
   if mat[curRow][curCol] == 0 or visitedMat[curRow][curCol]:
      return
   if curRow == n-1 and curCol == n - 1:
      count[0] += 1
      allPaths.append(''.join(curPath))
      return
   visitedMat[curRow][curCol] = True

   curPath.append('U')
   countPathHelper(mat, visitedMat, curRow - 1, curCol, count, allPaths, curPath)
   curPath.pop()

   curPath.append('D')
   countPathHelper(mat, visitedMat, curRow + 1, curCol, count, allPaths, curPath)
   curPath.pop()

   curPath.append('R')
   countPathHelper(mat, visitedMat, curRow, curCol + 1, count, allPaths, curPath)
   curPath.pop()

   curPath.append('L')
   countPathHelper(mat, visitedMat, curRow, curCol - 1, count, allPaths, curPath)
   curPath.pop()

   visitedMat[curRow][curCol] = False

mat = [
   [ 1, 0, 0, 0, 0 ],
   [ 1, 1, 1, 1, 1 ],
   [ 1, 1, 1, 0, 1 ],
   [ 0, 0, 0, 0, 1 ],
   [ 0, 0, 0, 0, 1 ]
]

print(countPath(mat))