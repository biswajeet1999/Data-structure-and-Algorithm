# O(9^(n^2)) time | O(n*n) space
def getNextEmptyCell(board):
   for row in range(9):
      for col in range(9):
         if board[row][col] == 0:
            return (row, col)
   return None

def isValid(board, row, col, num):
   for i in range(9):
      if board[row][i] == num:
         return False
      if board[i][col] == num:
         return False
   baseRow = 3 * (row // 3)
   baseCol = 3 * (col // 3)
   for i in range(baseRow, baseRow + 3):
      for j in range(baseCol, baseCol + 3):
         if board[i][j] == num:
            return False
   return True

def solve(board):
   pos = getNextEmptyCell(board)
   if pos == None:
      return True
   row, col = pos
   for i in range(1, 10):
      if(isValid(board, row, col, i)):
         board[row][col] = i
         result = solve(board)
         if result ==  True:
            return True
   board[row][col] = 0
   return False

board = [
   [3, 0, 6, 5, 0, 8, 4, 0, 0],
   [5, 2, 0, 0, 0, 0, 0, 0, 0],
   [0, 8, 7, 0, 0, 0, 0, 3, 1],
   [0, 0, 3, 0, 1, 0, 0, 8, 0],
   [9, 0, 0, 8, 6, 3, 0, 0, 5],
   [0, 5, 0, 0, 9, 0, 6, 0, 0],
   [1, 3, 0, 0, 0, 0, 2, 5, 0],
   [0, 0, 0, 0, 0, 0, 0, 7, 4],
   [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

solve(board)
print(board)