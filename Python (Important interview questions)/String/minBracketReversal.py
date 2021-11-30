def getMinBracketReversal(brackets):
   if len(brackets) % 2 == 1:
      return -1
   
   count = 0
   stack = []
   for bracket in brackets:
      if bracket == "{":
         stack.append(bracket)
      else:
         if len(stack) == 0 or stack[-1] != "{":
            stack.append(bracket)
         else:
            stack.pop()

   while len(stack) > 0:
      bracket1 = stack.pop()
      bracket2 = stack.pop()

      if bracket1 == bracket2:
         count += 1
      else:
         count += 2

   return count


exp = "}{"
print(getMinBracketReversal(exp))
exp = "{{{"
print(getMinBracketReversal(exp))
exp = "{{{{"
print(getMinBracketReversal(exp))
exp = "{{{{}}"
print(getMinBracketReversal(exp))
exp = "}{{}}{{{"
print(getMinBracketReversal(exp))