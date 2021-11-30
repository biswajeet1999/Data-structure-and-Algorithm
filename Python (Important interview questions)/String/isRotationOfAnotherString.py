def check(s1, s2):
   newString = s2 + s2
   if s1 in newString:
      return True
   return False

s1 = 'abcd'
s2 = 'cdab'
print(check(s1, s2))

s1 = 'abcd'
s2 = 'cadb'
print(check(s1, s2))
