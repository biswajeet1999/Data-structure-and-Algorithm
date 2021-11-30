# O(n) time | O(n) space
# def waterArea(heights = []):
#    leftMax = [height for height in heights]
#    rightMax = [height for height in heights]
#    result = 0
#    for i in range(1, len(heights)):
#       leftMax[i] = max(leftMax[i - 1], heights[i])

#    for i in range(len(heights) - 2, -1, -1):
#       rightMax[i] = max(rightMax[i+1], heights[i])

#    for i in range(1, len(heights) - 1):
#       result += max(0, min(leftMax[i], rightMax[i]) - heights[i])
#    return result

# two pointer method bcz left max is a monotonically non decreasing function and right max is a monotonically non increasing function
# refer youtube- ForAllEpsilon channel
# O(n) time | O(1) space
def waterArea(heights = []):
   leftMax = heights[0]
   rightMax = heights[-1]
   result = 0
   leftPtr = 0
   rightPtr = len(heights) - 1
   while leftPtr <= rightPtr:
      leftMax = max(leftMax, heights[leftPtr])
      rightMax = max(rightMax, heights[rightPtr])
      if leftMax < rightMax:
         result += max(0, leftMax - heights[leftPtr])
         leftPtr += 1
      else:
         result += max(0, rightMax - heights[rightPtr])
         rightPtr -= 1
   return result

heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
print(waterArea(heights))