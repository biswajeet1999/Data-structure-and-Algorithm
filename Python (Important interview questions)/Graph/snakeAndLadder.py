# O(n*2) time | O(n^2) space
def getMinMove(board):
   moves = [None for _ in range(len(board))]
   visited = [False for _ in board]
   queue = []
   queue.append(0)
   moves[0] = 0

   while len(queue) > 0:
      curCell = queue.pop(0)
      if curCell == len(board) - 1:
         break
      for move in range(1, 7):
         if curCell + move < len(board) and not visited[curCell + move]:
            if board[curCell + move] != -1:
               if not visited[board[curCell + move]]:
                  queue.append(board[curCell + move])
                  visited[board[curCell + move]]
                  moves[board[curCell + move]] = moves[curCell] + 1
            else:
               queue.append(curCell + move)
               moves[curCell + move] = moves[curCell] + 1
            visited[curCell + move] = True
   return moves[-1]


N = 30
board = [-1] * N
  
# Ladders
board[2] = 21
board[4] = 7
board[10] = 25
board[19] = 28
  
# Snakes
board[26] = 0
board[20] = 8
board[16] = 3
board[18] = 6

print(getMinMove(board))