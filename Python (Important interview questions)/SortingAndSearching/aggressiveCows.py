def canWePlaceCows(stalls, noCows, gap):
   previousCowPosition = stalls[0]
   noCows -= 1

   for stallPosition in stalls:
      if stallPosition - previousCowPosition >= gap:
         noCows -= 1
         previousCowPosition = stallPosition
         if(noCows == 0): break
   return noCows == 0


def getMinDistance(stalls, noCows):
   stalls.sort()
   minGap = 1
   maxGap = stalls[-1] - stalls[0]
   finalGap = 1

   while minGap <= maxGap:
      midGap = (minGap + maxGap)//2
      isPlaced = canWePlaceCows(stalls, noCows, midGap)
      if(isPlaced):
         finalGap = midGap
         minGap = midGap + 1
      else:
         maxGap = midGap - 1
   return finalGap


print(getMinDistance([1, 2, 8, 4, 9], 3))