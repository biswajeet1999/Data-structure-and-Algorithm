def getMaxProduct(arr):
   negCount = 0
   posCount = 0
   zeroCount = 0
   prod = 1
   minNegativeNum = -9999999

   for num in arr:
      if num > 0:
         posCount += 1
         prod *= num
      elif num < 0:
         prod *= num
         negCount += 1
         minNegativeNum = max(minNegativeNum, num)
      else:
         zeroCount += 1
   if zeroCount == len(arr) or (zeroCount == len(arr) -1 and negCount == 1):
      return 0
   if negCount % 2 == 1:
      prod //= minNegativeNum
   return prod
