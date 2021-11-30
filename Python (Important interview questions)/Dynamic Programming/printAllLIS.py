# O(n^2 + s*n^2) time | O() space
def lis(nums):
   if len(nums) == 0:
      return 

   dp = [1 for _ in nums]
   for idx in range(1, len(nums)):
      for j in range(0, idx):
         if nums[idx] > nums[j]:
            dp[idx] = max(dp[idx], dp[j]+1)
   
   generateAllLis(nums, dp)

# O(s*n^2) time | O(n) space
# here max s solutions possible. each solution is of length max n. at each step of generating solution we have to do n comparisons
def generateAllLis(nums, dp):
   maxLength = max(dp)
   lis = []
   for idx in range(len(dp)):
      if dp[idx] == maxLength:
         generateAllLisUtil(nums, dp, idx, maxLength, lis)

def generateAllLisUtil(nums, dp, idx, curLength, lis):
   lis.insert(0, nums[idx])
   if curLength == 1:
      print(lis)
      lis.pop(0)
      return
   for i in range(0, idx):
      if dp[i] == curLength - 1 and nums[i] < nums[idx]:
         generateAllLisUtil(nums, dp, i, curLength-1, lis)
   lis.pop(0)



lis([10, 22, 42, 33, 21, 50, 41, 60, 80, 3])