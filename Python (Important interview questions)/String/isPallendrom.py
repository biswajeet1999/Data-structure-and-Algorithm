def isPallendrom(s):
   l = 0
   r = len(s) - 1
   while l < r:
      if s[l] != s[r]:
         return False
   return True
   