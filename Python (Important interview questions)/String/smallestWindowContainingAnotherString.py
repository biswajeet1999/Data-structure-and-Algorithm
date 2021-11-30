def getSmallestWindow(s1, s2):
   freq = {}
   for char in s2:
      if char not in freq:
         freq[char] = 0
      freq[char] += 1

   targetSubstrLength = len(s2)
   curSubstringLength = 0
   windowRange = [-float("inf"), float("inf")]
   curSubStrFreq = {}
   l = 0
   r = 0

   while r < len(s1):
      curChar = s1[r]
      if curChar not in curSubStrFreq:
         curSubStrFreq[curChar] = 0
      curSubStrFreq[curChar] += 1
   
      if curChar in freq and curSubStrFreq[curChar] <= freq[curChar]:
         curSubstringLength += 1
      while curSubstringLength == targetSubstrLength and l <= r:
         leftMostCharInWindow = s1[l]
         if r - l < windowRange[1] - windowRange[0]:
            windowRange = [l, r]
         l += 1
         curSubStrFreq[leftMostCharInWindow] -= 1
         if leftMostCharInWindow in freq and curSubStrFreq[leftMostCharInWindow] < freq[leftMostCharInWindow]:
            curSubstringLength -= 1
      r += 1
   return s1[windowRange[0]: windowRange[1] + 1]




   


s1 = "timetopractice"
s2 = "toc"
print(getSmallestWindow(s1, s2))

s1 = "zoomlazapzo"
s2 = "oza"
print(getSmallestWindow(s1, s2))
