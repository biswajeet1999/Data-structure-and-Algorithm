# O(n*n) time | O(n*n) space
def traverseDown(matrix, curRow, curCol, result):
   while curCol >= 0 and curRow < len(matrix):
      result.append(matrix[curRow][curCol])
      curCol -= 1
      curRow += 1
   if curRow >= len(matrix) and curCol < 0:
      curCol += 2
      curRow -= 1
   elif curRow >= len(matrix):
      curRow = len(matrix) - 1
      curCol += 2
   elif curCol < 0:
      curCol = 0
   return curRow, curCol

def traverseUp(matrix, curRow, curCol, result):
   while curCol < len(matrix[0]) and curRow >= 0:
      result.append(matrix[curRow][curCol])
      curCol += 1
      curRow -= 1
   if curRow < 0 and curCol >= len(matrix[0]):
      curRow += 2
      curCol = len(matrix[0]) - 1 
   elif curRow < 0:
      curRow = 0
   elif curCol >= len(matrix[0]):
      curCol = len(matrix[0]) - 1
      curRow += 2
   return curRow, curCol

def zigzagTraverse(matrix):
   curRow = 0
   curCol = 0
   result = []
   isDown = True
   while 0 <= curRow < len(matrix) and 0 <= curCol < len(matrix[0]):
      if isDown:
         curRow, curCol = traverseDown(matrix, curRow, curCol, result)
         isDown = False
      else:
         curRow, curCol = traverseUp(matrix, curRow, curCol, result)
         isDown = True
      if curRow == len(matrix) - 1 and curCol == len(matrix[0]) - 1:
         result.append(matrix[len(matrix) - 1][len(matrix[0]) - 1])
         break
   return result

# even x even matrix
# matrix = [
#    [1, 3, 4, 10],
#    [2, 5, 9, 11],
#    [6, 8, 12, 15],
#    [7, 13, 14, 16]
# ]

# odd x odd matrix
matrix = [
   [1, 3, 4, 10, 11],
   [2, 5, 9, 12, 19],
   [6, 8, 13, 18, 20],
   [7, 14, 17, 21, 24],
   [15, 16, 22, 23, 25]
]
print(zigzagTraverse(matrix))