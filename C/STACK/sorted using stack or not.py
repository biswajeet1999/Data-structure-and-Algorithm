l = [int(x) for x in input('Enter the list: ').split()]
stack = []
flag = True

for i in range(len(l)-1):
    if l[i]  > l[i+1]:
        stack.append(l[i])

while(len(stack) > 1):
    num1 = stack.pop()
    num2 = stack.pop()
    if (num1 > num2) and num1 - num2 == 1:
        flag = False
        break
    stack.append(num2)

print('Yes' if flag else 'No')