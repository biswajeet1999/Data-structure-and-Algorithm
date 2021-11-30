exp1 = input('Enter expression1:  ')
exp2 = input('Enter expression2:  ')

evaluated_exp1 = ''
stack = []

def resultant_operator(op1, op2):
    if op1 == None:
        return op2
    elif op2 == None:
        return op1
    elif (op1 == '+' and op2 == '+') or (op1 == '-' and op2 == '-'):
        return '+'
    else:
        return '-'

for i in range(len(exp1)):
    if exp1[i] == '(':
        op1 = None if len(stack) == 0 else stack[-1]
        op2 = '+' if i == 0 else '-' if exp1[i-1] == '-' else '+'
        resultant = resultant_operator(op1, op2)
        stack.append(resultant)
    elif exp1[i] == ')':
        stack.pop()
    elif exp1[i] == '+' or exp1[i] == '-':
        pass
    elif 'a' <= exp1[i] <= 'z':
        if i == 0:
            evaluated_exp1 += exp1[i]
        else:
            op1 = None if len(stack) == 0 else stack[-1]
            op2 = '+' if exp1[i-1] == '(' else exp1[i-1]
            resultant = resultant_operator(op1, op2)
            evaluated_exp1 += resultant + exp1[i]

if(evaluated_exp1[0] == '+'):
    evaluated_exp1 = evaluated_exp1[1:]
if(exp2[0] == '+'):
    exp2 = exp2[1:]

print(evaluated_exp1 == exp2)


