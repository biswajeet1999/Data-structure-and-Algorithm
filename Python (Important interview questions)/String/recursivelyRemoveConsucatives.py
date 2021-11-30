def removeConsugatives(s):
   stack = []
   for char in s:
      while len(stack) != 0 and stack[-1] == char:
         stack.pop()
      stack.append(char)
   return "".join(stack)
      
s = "aabac"
print(removeConsugatives(s))