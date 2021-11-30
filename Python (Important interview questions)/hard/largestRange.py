def expandRange(numbers, idx, cache):
   curRange = [numbers[idx], numbers[idx]]
   # expand left range
   while curRange[0] - 1 in cache:
      curRange[0] = curRange[0] - 1
      cache[curRange[0]] = True # visited
   # expand right range
   while curRange[1] + 1 in cache:
      curRange[1] = curRange[1] + 1
      cache[curRange[1]] = True # visited
   return curRange

# O(1) tieme | O(1) space
def distance(rangeVal):
   if type(rangeVal)  not in[list, tuple] or len(rangeVal) < 2:
      return 0
   return rangeVal[1] - rangeVal[0] + 1

# O(n) tieme | O(n) space
def largestRange(numbers):
   if numbers == []:
      return [-1, -1]
   largestRange = [numbers[0], numbers[0]]
   cache = {num:False for num in numbers}

   for idx in range(0, len(numbers)):
      if cache[numbers[idx]] is not True:
         currentRange = expandRange(numbers, idx, cache)
         if distance(currentRange) > distance(largestRange):
            largestRange = currentRange
   return largestRange


nums = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(nums))