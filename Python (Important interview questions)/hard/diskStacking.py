# O(1) time | O(1) space
def canBePlaced(dim1, dim2):
   return dim1[0] < dim2[0] and dim1[1] < dim2[1] and dim1[2] < dim2[2]

# O(n^2) time | O(n) space 
def diskStacking(dimensions = []):
   dimensions.sort(key = lambda dimension: dimension[2])
   maxHeights = [dim[2] for dim in dimensions]
   maxHeight = -float("inf")
   for i in range(1, len(dimensions)):
      for j in range(i):
         if canBePlaced(dimensions[j], dimensions[i]):
            maxHeights[i] = max(maxHeights[i], maxHeights[j] + dimensions[i][2])
      maxHeight = max(maxHeight, maxHeights[i])
   print(maxHeights)
   return maxHeight

dimensions = [[2, 2, 1], [2, 1, 2], [3, 2, 3], [2, 3, 4], [4, 4, 5], [2, 2, 8]]
print(diskStacking(dimensions))