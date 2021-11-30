# O(nlog(n)) time | O(1) space
def getDiff(chocolates, noOfStud):
   if len(chocolates) == 0 or noOfStud == 0:
      return 0
   chocolates.sort()
   startIdx = 0
   endIdx = noOfStud - 1
   diff = chocolates[endIdx] - chocolates[startIdx]

   while endIdx < len(chocolates) - 1:
      startIdx += 1
      endIdx += 1
      diff = min(diff, chocolates[endIdx] - chocolates[startIdx])
   return diff



chocolates = [2, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7
print(getDiff(chocolates, m))