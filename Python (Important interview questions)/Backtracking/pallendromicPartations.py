# O(n^2 * n^2) time | O(2^n) space
def pallendromicPartations(s):
   cache = {}
   pallendromicPartationsHelper(s, 0, cache)
   return cache[s]

def pallendromicPartationsHelper(s, curIdx, cache):
   if curIdx >= len(s):
      return
   if s[curIdx: ] in cache:
      return
   
   for i in range(curIdx+1, len(s)+1):
      prefix = s[curIdx: i]
      if isPallendrom(prefix):
         pallendromicPartationsHelper(s, i, cache)

         if prefix == s[curIdx: ]:
            if prefix not in cache:
               cache[prefix] = [[prefix]]
            else:
               cache[prefix].append([prefix])
         else:
            if s[curIdx: ] not in cache:
               cache[s[curIdx: ]] = []
            suffix = s[i: ]
            if suffix in cache:
               for suff in cache[suffix]:
                  cache[s[curIdx: ]].append([prefix] + suff)
      
          
def isPallendrom(s):
   return s == s[::-1]


print(pallendromicPartations('nitin'))