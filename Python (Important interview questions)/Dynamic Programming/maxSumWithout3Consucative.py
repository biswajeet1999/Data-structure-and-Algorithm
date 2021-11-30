def mss(nums):
   n = len(nums)
   sums = [0 for _ in range(n)]
   largestSum = -float('inf')
   if n >= 1:
      sums[0] = nums[0]
   if n >= 2:
      sums[1] = nums[0] + nums[1]
   if n >= 3:
      sums[2] = nums[2] + max(nums[0], nums[1])
   for idx in range(3, n):
      sums[idx] = nums[idx] + max(sums[idx-3]+nums[idx-1], sums[idx-2])
   return max(sums)

print(mss([100, 1000, 100, 1000, 1]))