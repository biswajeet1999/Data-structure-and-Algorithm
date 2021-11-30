def longestConsecutive(nums):
      cache = {}
      for num in nums:
        cache[num] = False
      maxSeq = 0
      for num in nums:
        nxtNum = num + 1
        prvNum = num - 1
        if cache[num] == False and prvNum not in cache:
          curSeq = 1
          while nxtNum in cache:
            curSeq += 1
            nxtNum += 1
          maxSeq = max(maxSeq, curSeq)
      return maxSeq