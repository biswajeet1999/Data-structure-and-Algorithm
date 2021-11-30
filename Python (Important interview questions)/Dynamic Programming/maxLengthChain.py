def getMaxLengthChain(nums):
   pairList = []
   for idx in range(1, len(nums), 2):
      pairList.append((nums[idx-1], nums[idx]))
   print(pairList)
   n = len(pairList)
   maxLengthChain = [1 for _ in range(n)]
   maxLength = 1
   for i in range(1, n):
      for j in range(0, i):
         if pairList[j][1] < pairList[i][0]:
            maxLengthChain[i] = max(maxLengthChain[i], maxLengthChain[j] + 1)
            maxLength = max(maxLength, maxLengthChain[i])
   print(maxLengthChain)
   return maxLength


print(getMaxLengthChain([5, 24 ,39, 60, 15, 28, 27, 40, 50, 90]))