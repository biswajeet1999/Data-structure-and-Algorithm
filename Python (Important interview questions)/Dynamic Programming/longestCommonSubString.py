class SuffixTrie:
   def __init__(self, s):
      self.root = {}
      self.end = '$'
      self.buildFrom(s)
   def buildFrom(self, s):
      for i in range(0, len(s)):
         self.insertSuffix(i, s)
   
   def insertSuffix(self, i, s):
      node = self.root
      for idx in range(i, len(s)):
         char = s[idx]
         if char not in node:
            node[char] = {}
         node = node[char]
      node[self.end] = True
   
   def getMatchingLength(self, s, i):
      node = self.root
      length = 0
      for idx in range(i, len(s)):
         char = s[idx]
         if char not in node:
            return length
         length += 1
         node = node[char]
      return length
      
# O(n^2) time | O(n^2) space
def getLongestCommonSubString(s1, s2):
   suffixTrie = SuffixTrie(s1)
   maxLength = 0
   for idx in range(0, len(s2)):
      maxLength = max(maxLength, suffixTrie.getMatchingLength(s2, idx))
   return maxLength


print(getLongestCommonSubString("ABCDGH", "ACDGHR"))
print(getLongestCommonSubString("ABC", "ACB"))
