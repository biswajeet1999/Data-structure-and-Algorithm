def fourNumberSum(nums = [], targetSum = 0):
   result = []
   numberPair = {}
   for i in range(1, len(nums)):
      for j in range(i+1, len(nums)):
         requiredSum = targetSum - (nums[i]  + nums[j])
         if requiredSum in numberPair:
            for pair in numberPair[requiredSum]:
               result.append(pair + [nums[i], nums[j]])
      for k in range(0, i):
         curSum = nums[i] + nums[k]
         if curSum in numberPair:
            numberPair[curSum].append([nums[i], nums[k]])
         else:
            numberPair[curSum] = [[nums[i], nums[k]]]    
   return result

nums = [7, 6, 4, -1, 1, 2]
print(fourNumberSum(nums, 16))