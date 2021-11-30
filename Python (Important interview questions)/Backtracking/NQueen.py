# One Solution :-

# def solution(n):
#    solution = [None for _ in range(n)]
#    solve(n, 0, solution)
#    return solution

# def solve(n, curRow, solution):
#    if curRow == n:
#       return True
#    for col in range(n):
#       canPlace = canQueenPlace(n, curRow, col, solution)
#       if canPlace:
#          solution[curRow] = col
#          solved = solve(n, curRow + 1, solution)
#          if solved:
#             return True
#    return False


# def canQueenPlace(n, curRow, col, solution):
#    # left diagonal
#    curCol = col - 1
#    for row in range(curRow-1, -1, -1):
#       if solution[row] == curCol:
#          return False
#       curCol -= 1
#    # right diagonal
#    for row in range(curRow - 1, -1, -1):
#       if solution[row] == n-1-row:
#          return False
#    # top column
#    for row in range(curRow-1, -1, -1):
#       if solution[row] == col:
#          return False
#    return True

# n = 4
# print(solution(4))


# All solution:-
# T(n) = n*T(n-1)
# O(n!) time | O(n^2) space
def solution(n):
   curSolution = [None for _ in range(n)]
   solution = []
   solve(n, 0, curSolution, solution)
   return solution

def solve(n, curRow, curSolution, solution):
   if curRow == n:
      solution.append(curSolution[:]) 
      return
   for col in range(n):
      canPlace = canQueenPlace(n, curRow, col, curSolution)
      if canPlace:
         curSolution[curRow] = col
         solve(n, curRow + 1, curSolution, solution)

def canQueenPlace(n, curRow, col, solution):
   # left diagonal
   curCol = col - 1
   for row in range(curRow-1, -1, -1):
      if solution[row] == curCol:
         return False
      curCol -= 1
   # right diagonal
   curCol = col + 1   
   for row in range(curRow - 1, -1, -1):
      if solution[row] == curCol:
         return False
      curCol += 1
   # top column
   for row in range(curRow-1, -1, -1):
      if solution[row] == col:
         return False
   return True

n = 4
print(solution(4))