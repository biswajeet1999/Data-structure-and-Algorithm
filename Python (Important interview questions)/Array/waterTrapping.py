def getArea(heights):
   leftMax = [heights[0]]
   rightMax = [heights[-1] for _ in heights]
   area = 0

   for height in heights:
      leftMax.append(max(leftMax[-1], height))
   
   for idx in range(len(heights)-2, -1, -1):
      height = heights[idx]
      rightMax[idx] = max(height, rightMax[idx + 1])
   
   for idx in range(1, len(heights) - 1):
      minHight = min(leftMax[idx], rightMax[idx])
      if heights[idx] < minHight:
         area += minHight - heights[idx]
   return area


heights = [3, 0, 0, 2, 0, 4]
print(getArea(heights))
