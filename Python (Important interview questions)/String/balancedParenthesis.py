def isBalanced(brackets):
   match = {')':'(', '}': '{', ']': '['}
   stack = []
   for bracket in brackets:
      if bracket in ('(', '{', '['):
         stack.append(bracket)
      else:
         if len(stack) > 0 and match[bracket] == stack[-1]:
            stack.pop()
         else:
            return False
   return True if len(stack) == 0 else False


print(isBalanced('[{()}]'))
print(isBalanced('[{)()}]'))
print(isBalanced('[({)}]'))
print(isBalanced('][({)}]'))