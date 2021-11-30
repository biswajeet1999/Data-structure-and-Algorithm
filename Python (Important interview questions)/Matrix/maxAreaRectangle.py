def maxArea(bars = []):
   n = len(bars)
   maximumArea = -float('inf')
   leftMinHeight = [-1 for _ in bars]
   rightMinHeight = [n for _ in bars]
   
   # find (idx of left most bar which is smaller than current bar) + 1
   stack = []
   for idx, bar in enumerate(bars):
      while len(stack) > 0 and bars[stack[-1]] >= bar:
         stack.pop()
      if len(stack) == 0:
         leftMinHeight[idx] = 0
      else:
         leftMinHeight[idx] = stack[-1] + 1
      stack.append(idx)
   # find (idx of right most bar which is smaller than current bar) - 1
   stack = []
   for idx in range(n-1, -1, -1):
      bar = bars[idx]
      while len(stack) > 0 and bars[stack[-1]] >= bar:
         stack.pop()
      if len(stack) == 0:
         rightMinHeight[idx] = n - 1
      else:
         rightMinHeight[idx] = stack[-1] - 1
      stack.append(idx)
   
   for idx in range(n):
      curArea = (rightMinHeight[idx] - leftMinHeight[idx] + 1) * bars[idx]
      maximumArea = max(curArea, maximumArea)
   return maximumArea


def maxAreaRectangle(matrix):
   maximumArea = -float('inf')
   histogramWithThisRow = [0 for _ in range(len(matrix[0]))]
   for row in matrix:
      for idx, col in enumerate(row):
         if col == 0:
            histogramWithThisRow[idx] = 0
         else:
            histogramWithThisRow[idx] += 1
      curArea = maxArea(histogramWithThisRow)
      maximumArea = max(curArea, maximumArea)
   return maximumArea

matrix = [[0, 1, 1, 0, 0], 
          [1, 1, 1, 1, 0],
          [0, 0, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 0, 1, 1, 0],
          [1, 0, 0, 1, 1]]
print(maxAreaRectangle(matrix))
