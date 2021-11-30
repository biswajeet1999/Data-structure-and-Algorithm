# O(m*n) time | O(m*n) space
def longestSubsequence(string):
   cache = {}
   return longestSubsequenceHelper(string, string, len(string) - 1, len(string) - 1, cache)

def longestSubsequenceHelper(str1, str2, n, m, cache):
   if (n, m) in cache:
      return cache[(n, m)]
   if n == -1 or m == -1:
      cache[(n, m)] = 0
      return 0
   
   if str1[n] == str2[m] and n != m:
      cache[(n, m)] = 1 + longestSubsequenceHelper(str1, str2, n-1, m-1, cache)
      return cache[(n, m)]
   cache[(n, m)] = max(longestSubsequenceHelper(str1, str2, n, m-1, cache), longestSubsequenceHelper(str1, str2, n-1, m, cache))
   return cache[(n, m)]

print(longestSubsequence("aabb"))
print(longestSubsequence("axxxb"))