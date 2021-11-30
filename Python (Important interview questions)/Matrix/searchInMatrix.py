# O(m+n) time | O(1) space
def searchMatrix(matrix, target):
   if matrix == []:
      return False
   rowIdx = 0
   colIdx = len(matrix[0]) - 1
      
   while rowIdx < len(matrix) and colIdx >= 0:
      curNum = matrix[rowIdx][colIdx]
      if curNum == target:
         return True
      if curNum < target:
         rowIdx += 1
      else:
         colIdx -= 1
   return False