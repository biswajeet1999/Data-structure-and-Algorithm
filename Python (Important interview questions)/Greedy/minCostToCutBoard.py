# O(m + n + mlogm + nlogn) time | O(1) space
def minCost(horCosts, verCosts):
   totalHorizontalPieces = 1
   totalVerticalPieces = 1

   horCosts.sort(reverse=True)
   verCosts.sort(reverse=True)
   totalCost = 0

   i = 0
   j = 0
   while i < len(horCosts) and j < len(verCosts):
      minHorCut = horCosts[i]
      minVerCut = verCosts[j]
      if minHorCut > minVerCut:
         totalCost += totalVerticalPieces * minHorCut
         totalHorizontalPieces += 1
         i += 1
      else:
         totalCost += totalHorizontalPieces * minVerCut
         totalVerticalPieces += 1
         j += 1
   
   while i < len(horCosts):
      totalCost += totalVerticalPieces * horCosts[i]
      i += 1
   while j < len(verCosts):
      totalCost += totalHorizontalPieces * verCosts[i]
      totalVerticalPieces += 1
      j += 1
   return totalCost

print(minCost([4, 1, 2], [2, 1, 3, 1, 4]))