def findDuplicate(s):
   cache = {}
   duplicates = []

   for char in s:
      if char not in cache:
         cache[char] = 0
      cache[char] += 1
      if cache[char] == 2:
         duplicates.append(char)
   return duplicates

s = 'abcacdcccaa'
print(findDuplicate(s))


      