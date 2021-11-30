# O(n) time | O(n) space
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
   print(rightMinHeight)
   
   for idx in range(n):
      curArea = (rightMinHeight[idx] - leftMinHeight[idx] + 1) * bars[idx]
      maximumArea = max(curArea, maximumArea)
   return maximumArea

bars = [3, 2, 4, 3, 1, 6, 2]
print(maxArea(bars))
      