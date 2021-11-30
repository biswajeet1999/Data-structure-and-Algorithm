# O(n) time | O(1) space
def findDuplicate(nums):
   for i in range(len(nums)):
      curNum = abs(nums[i])
      if nums[curNum] < 0:
            return curNum
      nums[curNum] = -nums[curNum]
   return -1
