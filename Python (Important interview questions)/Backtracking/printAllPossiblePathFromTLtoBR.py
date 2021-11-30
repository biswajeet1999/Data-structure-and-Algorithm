# O(2^(n*m)) time | O( 2^(m-1 * n-1) * (m+n-1))
# space complexity:- there are n rows and m cols. so from each cell we can either move top or bottom so 2 options we have
# but m-1th col and n-1th row we can only move in one direction. so total paths = 2(n-1 * m-1). 
# and length of each path is m+n-1

def getAllPaths(mat):
   allPaths = []
   curPath = []
   getAllPathsHelper(mat, 0, 0, allPaths, curPath)
   return allPaths

def getAllPathsHelper(mat, row, col, allPaths, curPath):
   rows = len(mat)
   cols = len(mat[0])
   if col >= cols or row >= rows:
      return
   if col == cols - 1 and row == rows - 1:
      allPaths.append(curPath[:] + [mat[row][col]])

   curPath.append(mat[row][col])
   getAllPathsHelper(mat, row, col+1, allPaths, curPath)
   getAllPathsHelper(mat, row+1, col, allPaths, curPath)
   curPath.pop()



mat = [[1, 2, 3],
       [4, 5, 6]]
 
print(getAllPaths(mat))