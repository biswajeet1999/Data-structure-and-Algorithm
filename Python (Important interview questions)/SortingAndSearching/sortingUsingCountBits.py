# O(1) time | O(1) space
def getBits(num):
   counter = 0
   while(num):
      if(num & 1):
         counter += 1
      num >>= 1
   return counter

# modified counting sort
# O(n) time | O(n) space
def sortUsingCountBits(nums):
   bitCaching = {i: [] for i in range(0, 33)} # assuing integer takes 32 bit most
   result = []
   for num in nums:
      noOfBits = getBits(num)
      bitCaching[noOfBits].append(num)
   for bit in range(32, -1, -1):
      curList = bitCaching[bit]
      result.extend(curList)
   return result

print(sortUsingCountBits([1, 2, 3, 4, 5, 6]))