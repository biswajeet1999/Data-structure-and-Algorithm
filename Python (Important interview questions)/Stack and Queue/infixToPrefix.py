# O(n) time | O(n) space
def convert(infix):
   operators = []
   operands = []
   operatorsList = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 4}

   for char in infix:
      if char in operatorsList:
         if char is ')':
            op = operators.pop()
            while op != '(':
               op2 = operands.pop()
               op1 = operands.pop()
               operands.append(op + op1 + op2)
               op = operators.pop()
         elif char is '(':
            operators.append('(')
         else:
            while len(operators) > 0 and operatorsList[operators[-1]] >= operatorsList[char]:
               op2 = operands.pop()
               op1 = operands.pop()
               op = operators.pop()
               operands.append(op + op1 + op2)
            operators.append(char)
      else:
         operands.append(char)
   while len(operators) > 0:
      op2 = operands.pop()
      op1 = operands.pop()
      op = operators.pop()
      operands.append(op + op1 + op2)
   return operands.pop()


print(convert('A*B+C/D'))
print(convert('(A-B/C)*(A/K-L)'))