def getRepeatingNumber(n, arr):
   for idx in range(n):
      curNum = abs(arr[idx])
      targetIdx = curNum - 1
      if arr[targetIdx] < 0:
         return curNum
      arr[targetIdx] = -arr[targetIdx]



def findRepeatingMissing(n, arr):
   repeatingNum = getRepeatingNumber(n, arr)
   # reset arr
   arr = list(map(lambda x: abs(x), arr))

   arrSum = sum(arr)
   arrSumAfterRemovingRepeatingNum = arrSum - repeatingNum
   realSum = (n*(n+1))//2
   missingNumber = realSum - arrSumAfterRemovingRepeatingNum
   return [repeatingNum, missingNumber]


arr = [1, 3, 2, 3]
print(findRepeatingMissing(len(arr), arr))