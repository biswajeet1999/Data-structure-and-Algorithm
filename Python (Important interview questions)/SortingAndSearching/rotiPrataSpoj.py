def canPrataMadeInGivenTime(noOfPrata, cookRanks, targetTime):
   timeTillNow = 0
   counter = 1
   cookIdx = 0
   for i in range(1, noOfPrata + 1):
      if timeTillNow + (counter*cookRanks[cookIdx]) <= targetTime:
         timeTillNow += (counter*cookRanks[cookIdx])
         counter += 1
      else:
         cookIdx += 1
         if cookIdx == len(cookRanks):
            return False
         counter = 1
         timeTillNow = counter * cookRanks[cookIdx]
         if timeTillNow > targetTime:
            return False
         counter += 1
   return True


def getMinTime(noOfPrata, cookRanks):
   cookRanks.sort()
   finalTime = float("inf")
   minTime = 0
   maxTime = cookRanks[-1] * ((noOfPrata * (noOfPrata + 1))//2)

   while minTime <= maxTime:
      midTime = (minTime + maxTime) // 2
      result = canPrataMadeInGivenTime(noOfPrata, cookRanks, midTime)
      if result == True:
         finalTime = midTime
         maxTime = midTime - 1
      else:
         minTime = midTime + 1
   return finalTime


print(getMinTime(10, [1, 2, 3, 4]))
print(getMinTime(8, [1]))
print(getMinTime(8, [1, 1, 1, 1, 1, 1, 1, 1]))
