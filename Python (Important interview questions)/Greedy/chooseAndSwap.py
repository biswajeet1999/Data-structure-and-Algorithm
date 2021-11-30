def getSmallestString(string):
   uniqueChars = []
   cache = {}
   swapChars = {}
   for char in string:
      if char not in cache:
         uniqueChars.append(char)
         cache[char] = True
   sortedUniqueChars = sorted(uniqueChars)
   for idx in range(len(uniqueChars)):
      char1 = uniqueChars[idx]
      char2 = sortedUniqueChars[idx]
      if char1 != char2:
         swapChars[char1] = char2
         swapChars[char2] = char1
         break
   if len(swapChars) == 0:
      return string
   string = list(string)
   for idx, char in enumerate(string):
      if char in swapChars:
         string[idx] = swapChars[char]
   return "".join(string)

print(getSmallestString("ccab"))
print(getSmallestString("abba"))