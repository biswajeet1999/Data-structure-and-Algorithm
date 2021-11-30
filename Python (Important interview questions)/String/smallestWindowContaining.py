def getSmallestWindowContaining(string):
   uniqueChars = {char: True for char in string}
   totalUniqueChars = len(uniqueChars)
   curFreq = {}
   currentUniqueChars = 0
   windowLength = len(string)
   l = 0
   r = 0

   while r < len(string):
      currChar = string[r]
      if currChar not in curFreq or curFreq[currChar] == 0:
         curFreq[currChar] = 0
         currentUniqueChars += 1
      curFreq[currChar] += 1
      while currentUniqueChars == totalUniqueChars and l <= r:
         windowLength = min(windowLength, r - l + 1)
         leftMostCharInWindow = string[l]
         curFreq[leftMostCharInWindow] -= 1
         l += 1
         if curFreq[leftMostCharInWindow] == 0:
            currentUniqueChars -= 1
      r += 1
   return windowLength







string = "AABBBCBBAC"
print(getSmallestWindowContaining(string))