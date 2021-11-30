# O(2^n) time | O(n^2) space
def removeInvalidParenthesis(s):
   minBracketToRemove = findMinBracketToRemove(s)  
   removeBracketsUtil(s, 0, minBracketToRemove, '', {})

def removeBracketsUtil(s, curIdx, mbr, solution, cache):
   if curIdx >= len(s):
      if mbr == 0 and findMinBracketToRemove(solution) == 0 and solution not in cache:
         print(solution)
      cache[solution] = True
      return 

   # remove curBracket
   if mbr > 0:
      removeBracketsUtil(s, curIdx + 1, mbr - 1, solution, cache)
   #  keep current bracket
   solution += s[curIdx]
   removeBracketsUtil(s, curIdx + 1, mbr, solution, cache)

def findMinBracketToRemove(s):
   stack = []
   invalidClosingBracketsCount = 0
   for char in s:
      if char == '(':
         stack.append('(')
      else:
         if len(stack) == 0:
            invalidClosingBracketsCount += 1
         else:
            stack.pop()
   return invalidClosingBracketsCount + len(stack)

s = '()())()'
removeInvalidParenthesis(s)