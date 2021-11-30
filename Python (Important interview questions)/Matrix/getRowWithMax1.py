# O(r+c) time | O(1) space
def getMax1Row(matrix):
   if matrix == []:
      return -1
   max1Row = 0
   startIdx = len(matrix[0])

   for idx in range(0, len(matrix[0])):
      if matrix[0][idx] == 1:
         startIdx = idx
         break

   for row in range(1, len(matrix)):
      while startIdx != 0 and matrix[row][startIdx - 1] == 1:
         startIdx -= 1
         max1Row = row
      if startIdx == 0:
         return row
   
   if startIdx == len(matrix[0]):
      return -1
   return max1Row
   
# test-1
matrix = [[0, 1, 1, 1],
           [0, 0, 1, 1],
           [1, 1, 1, 1],
           [0, 0, 0, 0]]
# test-2
# matrix = [[0, 0, 0, 0],
#            [0, 0, 0, 0],
#            [0, 0, 0, 0],
#            [0, 0, 0, 0]]

print(getMax1Row(matrix))