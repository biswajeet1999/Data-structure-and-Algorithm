def getMaxEqualSum(stack1, stack2, stack3):
   sum1 = sum(stack1)
   sum2 = sum(stack2)
   sum3 = sum(stack3)

   top1, top2, top3 = 0, 0, 0

   while top1 < len(stack1) and top2 < len(stack2) and top3 < len(stack3):
      if sum1 == sum2 and sum2 == sum3:
         return 3*sum1
      topEle1 = stack1[top1]
      topEle2 = stack2[top2]
      topEle3 = stack3[top3]
      if sum1 >= sum2 and sum1 >= sum3:
         sum1 -= topEle1
         top1 += 1
      elif sum2 >= sum1 or sum2 >= sum3:
         sum2 -= topEle2
         top2 += 1
      else:
         sum3 -= topEle3
         top3 += 1
   return 3*sum1 if sum1 == sum2 and sum2 == sum3 else 0

