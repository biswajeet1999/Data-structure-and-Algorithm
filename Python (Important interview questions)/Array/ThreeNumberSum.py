# O(n^2) time | O(n) space
def ThreeNumSum(array, k):
   array.sort()
   result = []
   for i in range(0, len(array) - 2):
      curNum = array[i]
      targetSum = k - curNum
      left = i + 1
      right = len(array) - 1
      while left < right:
         curSum = array[left] + array[right]
         if curSum == targetSum:
            result.append([curNum, array[left], array[right]])
            left += 1
            right -= 1
         elif curSum < targetSum:
            left += 1
         else:
            right -= 1
   return result


array = [-8, -6, 1, 2, 3, 5, 6, 12]
print(ThreeNumSum(array, 0))