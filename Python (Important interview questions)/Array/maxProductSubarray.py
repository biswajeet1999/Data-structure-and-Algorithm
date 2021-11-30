def maxProduct(nums):
      maxx = nums[0]
      minn = nums[0]
      largestProduct = maxx
      
      for i in range(1, len(nums)):
        maxx, minn = max(nums[i], nums[i] * maxx, nums[i] * minn), min(nums[i], nums[i] * maxx, nums[i] * minn)
        largestProduct = max(largestProduct, maxx)
      return largestProduct