def getAllAnagrams(strs):
   anagramDict = {}
   sortedWords = ["".join(sorted(s)) for s in strs]

   for i in range(len(strs)):
      sortedWord = sortedWords[i] 
      if sortedWord not in anagramDict:
         anagramDict[sortedWord] = []
      anagramDict[sortedWord].append(strs[i])
   return [value for key, value in anagramDict.items()]


strings = ["act","god","cat","dog","tac"]
print(getAllAnagrams(strings))