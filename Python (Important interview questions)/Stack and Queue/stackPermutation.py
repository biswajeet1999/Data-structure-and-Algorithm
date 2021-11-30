def isvlidPermutation(inputQ, outputQ):
   stack = []
   while len(inputQ) > 0:
      inp = inputQ.pop(0)
      stack.append(inp)
      while len(stack) > 0 and stack[-1] == outputQ[0]:
         stack.pop()
         outputQ.pop(0)
   return True if len(stack) == 0 and len(outputQ) == 0 else False
   
print(isvlidPermutation([1, 2, 3], [2, 1, 3]))
print(isvlidPermutation([1, 2, 3], [3, 1, 2]))
