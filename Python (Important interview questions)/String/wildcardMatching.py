# 2^n time | O(n) space
# def wildcardMatching(s, sIdx, p, pIdx):
#    if sIdx == len(s) and pIdx == len(p):
#       return True
   
#    if sIdx == len(s) or pIdx == len(p):
#       return False 
   
   
#    if p[pIdx] == "*":
#       return wildcardMatching(s, sIdx + 1, p, pIdx) or wildcardMatching(s, sIdx, p, pIdx + 1) or wildcardMatching(s, sIdx + 1, p, pIdx + 1)
   
#    if p[pIdx] == "?" or p[pIdx] == s[sIdx]:
#       return wildcardMatching(s, sIdx + 1, p, pIdx + 1)
#    return False

# o(n^2) time | o(n^2) space
def wildcardMatching(s, sIdx, p, pIdx, cache = {}):
   if (sIdx, pIdx) in cache:
      return cache[(sIdx, pIdx)]

   if sIdx == len(s) and pIdx == len(p):
      cache[(sIdx, pIdx)] = True
      return True
   
   if sIdx == len(s) or pIdx == len(p):
      cache[(sIdx, pIdx)] = False
      return False 
   
   
   if p[pIdx] == "*":
      cache[(sIdx, pIdx)] =  wildcardMatching(s, sIdx + 1, p, pIdx, cache) or wildcardMatching(s, sIdx, p, pIdx + 1, cache) or wildcardMatching(s, sIdx + 1, p, pIdx + 1, cache)
      return cache[(sIdx, pIdx)]

   if p[pIdx] == "?" or p[pIdx] == s[sIdx]:
      cache[(sIdx, pIdx)] = wildcardMatching(s, sIdx + 1, p, pIdx + 1, cache)
      return cache[(sIdx, pIdx)]
   
   cache[(sIdx, pIdx)] = False
   return False




s = "baaabab"
# p = "*****ba*****ab"
# p = "ba*****ab"
# p = "ba*ab"
# p = "a*ab"
# p = "a*****ab"
# p = "*a*****ab"
# p = "ba*ab****"
# p = "****"
# p = "*"
# p = "aa?ab"
# p = "b*b"
# p = "a*a"
# p = "baaabab"
# p = "?baaabab"
p = "*baaaba*"
print(wildcardMatching(s, 0, p, 0))