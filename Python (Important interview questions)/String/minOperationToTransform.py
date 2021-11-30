def minOperation(s1, s2):
   if len(s1) != len(s2):
      return False
   # check wether they have same set of characters or not
   freq = {}
   for char in s1:
      if char not in freq:
         freq[char] = 0
      freq[char] += 1
   for char in s2:
      if char not in freq:
         return False
      freq[char] -= 1
   for _, value in freq.items():
      if value != 0:
         return False


   i = len(s1) - 1
   j = len(s2) - 1
   changes = 0
   while j >=0:
      if s1[i] == s2[j]:
         i -= 1
         j -= 1
      else:
         changes += 1
         j -= 1
   return changes


A = "EACBD"
B = "EABCD"

print(minOperation(A, B))
      
