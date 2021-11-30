class Trie:
   def __init__(self, wordList):
      self.root = {}
      self.endSymbol = '*'
      self.populateTrieFrom(wordList)
   
   # O(noOfWord * wordLength) time | O(noOfWord * wordLength) space
   def populateTrieFrom(self, wordList):
      for word in wordList:
         self.insert(word)

   # O(wordLength) space | O(1) space
   def insert(self, word):
      node = self.root
      for letter in word:
         if letter not in node:
            node[letter] = {}
         node = node[letter]
      node[self.endSymbol] = True

   # O(wordLength) time | O(1) spae
   def contains(self, word):
      node = self.root
      for letter in word:
         if letter not in node:
            return False
         node = node[letter]
      return self.endSymbol in node