def spiral(mat):
   startRowIdx = 0
   endRowIdx = len(mat) - 1
   startColIdx = 0
   endColIdx = len(mat[0]) - 1
   result = []
   while startRowIdx <= endRowIdx and startColIdx <= endColIdx:
      for idx in range(startColIdx, endColIdx + 1): result.append(mat[startRowIdx][idx])
      for idx in range(startRowIdx+1, endRowIdx + 1): result.append(mat[idx][endColIdx])
      for idx in range(endColIdx - 1, startColIdx - 1, -1): result.append(mat[endRowIdx][idx])
      for idx in range(endRowIdx - 1, startRowIdx, -1): result.append(mat[idx][startColIdx])
      startRowIdx += 1
      endRowIdx -= 1
      startColIdx += 1
      endColIdx -= 1
   return result

mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15,16]]
print(spiral(mat))