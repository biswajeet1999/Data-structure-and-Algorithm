# mplement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.

def swap(nums, i, j):
   nums[i], nums[j] = nums[j], nums[i]
      
def reverse(nums, startIdx):
   i = startIdx
   j = len(nums) - 1
   while i < j:
      swap(nums, i, j)
      i += 1
      j -= 1
# O(n) time | O(1) space  
def nextPermutation(nums):
   for i in range(len(nums)-2, -1, -1):
      if nums[i] < nums[i+1]:
         for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
               swap(nums, i, j)
               reverse(nums, i + 1)
               return
   reverse(nums, 0)