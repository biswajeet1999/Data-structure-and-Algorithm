def getMaxGold(mat):
   cost = [[0 for col in mat[0]] for row in mat]

   for row in range(len(mat)):
      cost[row][-1] = mat[row][-1]
   
   for col in range(len(mat[0]) - 2, -1, -1):
      for row in range(0, len(mat)):
         right = cost[row][col+1]
         rightTop = cost[row-1][col+1] if row > 0 else 0
         rightBottom = cost[row+1][col+1] if row < len(mat) - 1 else 0
         cost[row][col] = mat[row][col] + max(right, rightTop, rightBottom)
         
   result = -float('inf')
   for row in cost:
      result = max(row[0], result)
   return result

gold = [[1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]]

 
print(getMaxGold(gold))