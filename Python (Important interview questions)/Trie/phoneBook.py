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

   # n = search word length | m = total nodes in trie
   # example:- trie contains = [t, tt, ttt, tttt], word to search = tttt
   # O(n*m) time | (m^2) space
   def phoneBookSearch(self, word):
      result = []
      node = self.root
      prefix = ''
      for letter in word:
         if letter not in node:
            break
         node = node[letter]
         prefix += letter
         self.printAllWordsFromPrefix(prefix, node, result)
      return result

   # O(m) time | O(m) space
   def printAllWordsFromPrefix(self, prefix, node, result):
      if self.endSymbol in node:
         result.append(prefix)
      
      for letter in node:
         if self.endSymbol != letter:
            child = node[letter]
            self.printAllWordsFromPrefix(prefix+letter, child, result)


wordList = ['gforgeeks' , 'geeksquiz']
wordToSearch = 'gekk'
phoneBook = Trie(wordList)
result = phoneBook.phoneBookSearch(wordToSearch)
print(result)