def getWoodLength(heights, cutterLength):
   cutWoodLength = 0
   for height in heights:
      cutWoodLength += max(0, (height - cutterLength))
   return cutWoodLength


def getMinHeight(heights, woodLength):
   heights.sort()
   minHeight = 0
   maxHeight = heights[-1]
   cutterHeight = -1
   
   while minHeight <= maxHeight:
      midHeight = (minHeight + maxHeight) // 2
      curCuttedWoodLength = getWoodLength(heights, midHeight)
      if curCuttedWoodLength == woodLength:
         return midHeight
      elif curCuttedWoodLength < woodLength:
         maxHeight = midHeight - 1
      else:
         cutterHeight = midHeight
         minHeight = midHeight + 1
   return cutterHeight

print(getMinHeight([20, 15, 10, 17], 7))
print(getMinHeight([4, 42, 40, 26, 46], 20))
      