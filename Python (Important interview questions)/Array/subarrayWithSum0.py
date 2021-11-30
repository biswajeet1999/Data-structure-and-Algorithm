# O(n) time | O(1) space
def getSubArray(array):
   summ = sum(array)
   i = 0
   j = len(array) - 1
   while i <= j:
      if summ == 0:
         return True
      leftMostSum = summ - array[j]
      rightMostSum =  summ - array[i]
      if abs(leftMostSum) > abs(rightMostSum):
         i += 1
         summ = rightMostSum
      else:
         j -= 1
         summ = leftMostSum
   return False

array = [4, 2, -3, 1, 6]
print(getSubArray(array))
array = [4, 2, 0, 1, 6]
print(getSubArray(array))
array = [-1, -2, 0, -3, -2, -1]
print(getSubArray(array))
array = [-1, -2, -3, -2, -1]
print(getSubArray(array))
array = [1, 2, 3, 4]
print(getSubArray(array))
