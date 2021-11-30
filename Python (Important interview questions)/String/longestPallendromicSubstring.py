def getLongestPallendrom(string):
   if string == '':
      return ''
   longestPallendrom = string[0]

   for idx in range(1, len(string)):
      p1 = getPallendrom(string, idx - 1, idx + 1) # checking for odd length pallendrome
      p2 = getPallendrom(string, idx - 1, idx) # checking for even length pallendrome
      currentMaxPallendrom = max(p1, p2, key=lambda s: len(s))
      longestPallendrom = max(longestPallendrom, currentMaxPallendrom, key=lambda s: len(s))
   return longestPallendrom


def getPallendrom(string, l, r):
   while l >= 0 and r < len(string):
      if string[l] != string[r]:
         break
      l -= 1
      r += 1
   return string[l+1: r]

string = 'abc'
string = 'abccba'
print(getLongestPallendrom(string))