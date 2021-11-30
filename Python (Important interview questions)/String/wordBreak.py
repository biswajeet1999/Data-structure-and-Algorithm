def wordBreak(s, words):
   dic = {word: True for word in words}
   return wordBreakHelper(list(s), 0, dic, cache = {})

def wordBreakHelper(s, curIdx, dic, cache = {}):
   if curIdx in cache:
      return cache[curIdx]
   if curIdx == len(s):
      cache[curIdx] = True
      return True
   for i in range(curIdx, len(s)):
      prefix = "".join(s[curIdx:i+1])
      if prefix in dic:
         result = wordBreakHelper(s, i + 1, dic, cache)
         if result == True:
            cache[curIdx] = True
            return True
   cache[curIdx] = False
   return False
   

s = "ilikesamsung"
words = ["i", "lik", "ilike", "il" "sam", "sung", "samsung", "mobile", "ice","cream", "icecream", "man", "go", "mango"]
print(wordBreak(s, words))