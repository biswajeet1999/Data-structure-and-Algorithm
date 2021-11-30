# O(min(m, n)) time | O(min(n, m)) space
def getIntersctionPointIdx(path1, path2):
   idx1 = 0
   idx2 = 0
   intersectionPoints = []
   while idx1 < len(path1) and idx2 < len(path2):
      if path1[idx1] == path2[idx2]:
         intersectionPoints.append(path1[idx1])
         idx1 += 1
         idx2 += 1
      elif path1[idx1] < path2[idx2]:
         idx1 += 1
      else:
         idx2 += 1
   return intersectionPoints

# O(m + n) time | O(min(m, n))
def getMaxPath(path1, path2):
   intersectionPoints = getIntersctionPointIdx(path1, path2)
   # O(min(m, n)) time | O(min(n, m)) space
   intersectionDict = {num: {'leftSum1': 0, 'leftSum2': 0} for num in intersectionPoints}

   sumTillNow = 0
   for ele in path1:
      if ele in intersectionDict:
         intersectionDict[ele]['leftSum1'] = sumTillNow
         sumTillNow = 0
      else:
         sumTillNow += ele
   
   sumTillNow = 0
   for ele in path2:
      if ele in intersectionDict:
         intersectionDict[ele]['leftSum2'] = sumTillNow
         sumTillNow = 0
      else:
         sumTillNow += ele
   
   maxPathSum = 0

   for intersection in intersectionDict:
      maxPathSum += intersection + max(intersectionDict[intersection]['leftSum1'], intersectionDict[intersection]['leftSum2'])
   
   rightMostSum1 = 0
   rightMostSum2 = 0

   for ele in reversed(path1):
      if ele in intersectionDict:
         break
      rightMostSum1 += ele
   
   for ele in reversed(path2):
      if ele in intersectionDict:
         break
      rightMostSum2 += ele

   maxPathSum += max(rightMostSum1, rightMostSum2)
   return maxPathSum

print(getMaxPath([3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62], [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]))
print(getMaxPath([-5, 100, 1000, 1005], [-12, 1000, 1001]))