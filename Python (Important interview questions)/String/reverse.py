def reverse(s):
   reverseString = list(s)
   l = 0
   r = len(s) - 1

   while l < r:
      reverseString[l], reverseString[r] = reverseString[r], reverseString[l]
      l += 1
      r -= 1
   
   return ''.join(reverseString)


s = 'abcsd'
print(reverse(s))