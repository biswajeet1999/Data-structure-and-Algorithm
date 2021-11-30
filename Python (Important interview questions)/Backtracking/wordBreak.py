# backtracking: O(2^n) time | O(n) space
# DP: O(N^2*s) time | O(N^2*s) space
# N: length of string, s: lenght of word list
# here we are bulding cache. so htere are at most N^2 substring in the cache present as key and values can be created in s time.
# value can contain at most s list i.e [ [w1], [w1, w2], ..., [w1, w2, ..., Ws] ]. so time is O(N^2*s)

def breakWord(s, words):
   wordDict = {word: True for word in words}      
   cache = {}
   breakWordHelper(s, wordDict, 0, cache)
   print(cache)
   return cache[s]

def breakWordHelper(s, words, start, cache):
   if start >= len(s):
      return
   
   if s[start: len(s)] in cache:
      return

   for idx in range(start+1, len(s)+1):
      prefix = s[start: idx]
      
      if prefix in words:
         breakWordHelper(s, words, idx, cache)

         if prefix == s[start: len(s)]:
            cache[prefix] = [[prefix]]
         else:
            if s[start: len(s)] not in cache:
               cache[s[start: len(s)]] = []
            suffix = s[idx: ]
            if suffix in cache:
               for suff in cache[suffix]:
                  cache[s[start: len(s)]].append([prefix] + suff)
   

s = "catsanddog"
words = ['cat', 'cats', 'and', 'sand', 'dog']
print(breakWord(s, words))


