
# O(n^2*s) time | O(n*s) space
# n:- no of words in the list, s:- avg length of each word
def getMinLength(start, end, words):
   if start == end:
      return 0
   parent = {}
   wordVisited = {word:False for word in words}
   queue = []   
   queue.append(start)
   wordVisited[start] = True
   # apply bfs
   while len(queue) > 0:
      curWord = queue.pop(0)
      for word in words:
         if charDiff(curWord, word) == 1 and not wordVisited[word]:
            queue.append(word)
            wordVisited[word] = True
            parent[word] = curWord
            if word == end:
               break
   wordLadder = []
   curWord = end
   wordLadder.append(end)

   while curWord in parent:
      parentWord = parent[curWord]
      wordLadder.append(parentWord)
      curWord = parentWord
   return [] if wordLadder[-1] != start else wordLadder

def charDiff(word1, word2):
   if len(word1) != len(word2):
      return float('inf')
   diffCount = 0
   for idx in range(len(word1)):
      if word1[idx] != word2[idx]:
         diffCount += 1
   return diffCount


print(getMinLength('toon', 'plea', ["poon", "plee", "same", "poie", "plie", "poin", "plea"]))