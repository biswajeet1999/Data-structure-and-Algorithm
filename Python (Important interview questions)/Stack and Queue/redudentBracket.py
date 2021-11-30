def chk(s):
   stack = []
   for c in s:
      if c == ')':
         removeCount = 0
         while stack.pop() != '(':
            removeCount += 1
         if removeCount < 2:
            return True # redudent exists
      else:
         stack.append(c)
   return False # redudent doesn't exists


print(chk('((a+b))'))
print(chk('(a+(b)/c)'))
print(chk('(a+b*(c-d))'))