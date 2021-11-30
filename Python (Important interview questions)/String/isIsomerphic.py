def isIsomorphic(s1, s2):
   if len(s1) != len(s2):
      return False
   
   charMapping = {}
   for idx in range(len(s1)):
      char1 = s1[idx]
      char2 = s2[idx]
      if char1 not in charMapping:
         charMapping[char1] = char2
      if charMapping[char1] != char2:
         return False
   
   charMapping = {}
   for idx in range(len(s2)):
      char1 = s2[idx]
      char2 = s1[idx]
      if char1 not in charMapping:
         charMapping[char1] = char2
      if charMapping[char1] != char2:
         return False
   return True

str1 = "aab"
str2 = "xxy"
print(isIsomorphic(str1, str2))

str1 = "aab"
str2 = "xyz"
print(isIsomorphic(str1, str2))