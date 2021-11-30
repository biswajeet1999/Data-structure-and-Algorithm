# O(n*s*log(s)) time | O(n*s) space
def getAnagrams(words):
   sortedWords = []
   wordCache = {}
   for word in words:
      sortedWords.append(''.join(sorted(word)))
   
   for idx in range(len(words)):
      sortedWord = sortedWords[idx]
      if sortedWord not in wordCache:
         wordCache[sortedWord] = []
      wordCache[sortedWord].append(words[idx])
   
   result = []
   for _, anagramList in wordCache.items():
      result.append(anagramList)
   return result


wordList = ['dog', 'cat', 'god', 'tac', 'act']
anagramList = getAnagrams(wordList)
print(anagramList)
