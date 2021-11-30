# O(n*m) time | O(m*n) space
# here in cache we are storing combination of idx1, idx2 so total m*n combination.
# so time complexity is m*n because we are exploring each combination if idx1, idx2 only once.
def isValidShuffle(str1, str2, targetStr):
   if len(str1) + len(str2) != len(targetStr):
      return False
   cache = {}
   return isValid(str1, str2, targetStr, 0, 0, 0, cache)


def isValid(str1, str2, targetStr, idx1, idx2, idx3, cache):
   if (idx1, idx2) in cache:
      return cache[(idx1, idx2)]
   if idx1 == len(str1) and idx2 == len(str2) and idx3 == len(targetStr):
      cache[(idx1, idx2)] = True
      return True
   if idx1 < len(str1) and str1[idx1] == targetStr[idx3]:
      res = isValid(str1, str2, targetStr, idx1 + 1, idx2, idx3 + 1, cache)
      cache[(idx1, idx2)] = res
      if res == True:
         return True
   if idx2 < len(str2) and str2[idx2] == targetStr[idx3]:
      res = isValid(str1, str2, targetStr, idx1, idx2 + 1, idx3 + 1, cache)
      cache[(idx1, idx2)] = res
      return res
   cache[(idx1, idx2)] = False
   return False


str1 = 'aaa'
str2 = 'aaaf'
targetStr = 'aaafaaa'
print(isValidShuffle(str1, str2, targetStr))