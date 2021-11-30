def maxArraySum(arr, k):
   arr.sort()
   for i in range(len(arr)):
      if k == 0:
         break
      if arr[i] < 0:
         arr[i] = -arr[i]
         k -= 1
      else:
         break
   if arr[i] != 0 and k %2 != 0:
      if arr[i] > arr[i-1]:
         arr[i-1] = -arr[i-1]
      else:
         arr[i] = -arr[i]
   return sum(arr)
