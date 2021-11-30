# this algorithm doesn't work
# def getSmallestSubarrayLength(arr, targetNum):
#    curSum = 0
#    for num in arr:
#       curSum += num
#    if curSum <= targetNum:
#       return -1

#    left = 0
#    right = len(arr) - 1

#    while left <= right:
#       if curSum > targetNum and (curSum - arr[left] <= targetNum and curSum - arr[right] <= targetNum):
#          return right - left + 1
#       if arr[left] < arr[right]:
#          curSum -= arr[left]
#          left += 1
#       else:
#          curSum -= arr[right]
#          right -= 1
#    return -1
# O(n) time | O(1) space
def getSmallestSubarrayLength(arr, targetNum):
   startIdx = 0
   endIdx = 1
   summ = arr[startIdx]
   length = float("inf")

   while endIdx < len(arr):
      summ += arr[endIdx]
      while summ > targetNum:
         length = min(length, endIdx - startIdx + 1)
         summ -= arr[startIdx]
         startIdx += 1

      endIdx += 1
   return length


arr = [1, 4, 45, 6, 0, 19]
targetNum = 51
print(getSmallestSubarrayLength(arr, targetNum))
