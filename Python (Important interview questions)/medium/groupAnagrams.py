# n:- length of strings list, s:- max length of string 
# O(s) time | O(1) space
def getMask(string):
   mask = [0 for _ in range(26)]
   for alphabet in string:
      idx = 97 - ord(alphabet)
      mask[idx] = 1
   return tuple(mask)

# O(n * s) time | O(n * s) space
def groupAnagram(strings):
   anagrams = {}
   for string in strings:
      mask = getMask(string)
      if mask in anagrams:
         anagrams[mask].append(string)
      else:
         anagrams[mask] = [string]
   return list(anagrams.values())



strings = ['oy', 'flap', 'act', 'yo', 'falp', 'tac', 'cat']
print(groupAnagram(strings))