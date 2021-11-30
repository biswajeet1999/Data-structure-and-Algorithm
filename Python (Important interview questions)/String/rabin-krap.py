def rabinKrap(str1, pattern):
   n = len(str1)
   m = len(pattern)
   base = 256
   patternHashValue = 0
   subStringHashValue = 0
   result = []
   for i in range(0, m):
      patternHashValue = patternHashValue * base + ord(pattern[i])
      subStringHashValue = subStringHashValue * base + ord(str1[i])
   i = m
   while True:
      if subStringHashValue == patternHashValue:
         if(areBothSame(str1, i-1, pattern, m)):
            result.append(i - m)
         pass
      if i < n:
         subStringHashValue = (subStringHashValue - (ord(str1[i - m])*(base**(m-1)))) * base + ord(str1[i])
         i += 1
      else:
         break 
   return result   

def areBothSame(str1, endIdx, pattern, m):
   i = m - 1
   while i >= 0:
      if str1[endIdx] != pattern[i]:
         return False
      i -= 1
      endIdx -= 1
   return True


s = "AABAACAADAABAABA"
p = "AABA"
print(rabinKrap(s, p))