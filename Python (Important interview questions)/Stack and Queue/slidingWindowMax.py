# O(n) time | O((n-k) + k) space
def slidingWindowMax(arr, k):
   result = []
   queue = []
   
   for idx in range(0, k):
      if len(queue) == 0:
         queue.append(arr[idx])
         continue
      while queue[-1] < arr[idx]:
         queue.pop()
         if len(queue) == 0:
            break
      queue.append(arr[idx])
   result.append(queue[0])

   l = 1
   r = l+k-1

   while r < len(arr):
      prevWindowLstNum = arr[l - 1]
      if queue[0] == prevWindowLstNum:
         queue.pop(0)
      curWindowLastNum = arr[r]

      while queue[-1] < curWindowLastNum:
         queue.pop()
         if len(queue) == 0:
            break
      queue.append(curWindowLastNum)
      result.append(queue[0])
      l+=1
      r+=1
   return result


print(slidingWindowMax([12, 1, 78, 90, 57, 89, 56], 3))