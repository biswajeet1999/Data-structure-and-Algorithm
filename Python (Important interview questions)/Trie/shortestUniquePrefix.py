class Trie:
   def __init__(self, words=[]):
      self.root = {}
      self.endSymbole = '*'
      self.populateTrieFrom(words)
   
   def populateTrieFrom(self, words):
      for word in words:
         self.insert(word)
   
   def insert(self, word):
      node = self.root
      for letter in word:
         if letter not in node:
            node[letter] = {'charFreq': 0}
         node[letter]['charFreq'] += 1
         node = node[letter]
      node[self.endSymbole] = True

   def getAllUniquePrefix(self):
      uniquePrefixes = []
      node = self.root
      self.getAllUniquePrefixUtil(node, uniquePrefixes, curPrefix=[])
      return uniquePrefixes
   
   def getAllUniquePrefixUtil(self, node, uniquePrefixes, curPrefix):
      # root node doesn't have charFreq attribute
      if 'charFreq' in node and node['charFreq'] == 1:
         uniquePrefixes.append(''.join(curPrefix))
         return
      
      for char in node:
         if char != 'charFreq':
            curPrefix.append(char)
            self.getAllUniquePrefixUtil(node[char], uniquePrefixes, curPrefix)
            curPrefix.pop()

trie = Trie(['zebra', 'dog', 'dove', 'duck'])
# print(trie.root)
print(trie.getAllUniquePrefix())