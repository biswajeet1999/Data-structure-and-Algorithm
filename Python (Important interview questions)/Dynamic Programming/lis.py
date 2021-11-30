# O(2^n) time | O(n) space
# def lis(nums):
#    maxLength = 1
#    for idx in range(1, len(nums)):
#       maxLength = max(maxLength, lisHelper(nums, idx))
#    return maxLength

# def lisHelper(nums, idx):
#    if idx >= len(nums):
#       return 0
#    length = 0
#    for i in range(idx+1, len(nums)):
#       if nums[i] > nums[idx]:
#          length = max(length, lisHelper(nums, i))
#    length += 1
#    return length



# O(n^2) time | O(n) space 
# def lis(nums):
#    n = len(nums)
#    lisDp = [1 for _ in range(n)]
#    for idx in range(1, len(nums)):
#       for j in range(idx - 1, -1, -1):
#          if nums[idx] > nums[j]:
#             lisDp[idx] = max(lisDp[idx], 1 + lisDp[j])
#    return max(lisDp)



def getMinLengthIdx(length, num):
   idx = -1
   start = 0
   end = len(length)
   while start <= end:
      mid = (start + end) // 2
      if length[mid] > num:
         idx = mid
         end = mid - 1
      else:
         start = mid + 1
   return idx

# O(nlogn) time | O(n) space
def lis(nums):
   length = [nums[0]]

   for idx in range(1, len(nums)):
      if nums[idx] > length[-1]:
         length.append(nums[idx])
      else:
         targetIdx = getMinLengthIdx(length, nums[idx])
         length[targetIdx] = nums[idx]
   print(length)
   return len(length)


print(lis([5, 8, 3, 7, 9, 1]))
