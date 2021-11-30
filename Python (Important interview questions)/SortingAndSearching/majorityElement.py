def getMajority(arr):
   majority = arr[0]
   count = 1

   for idx in range(1, len(arr)):
      curElement = arr[idx]
      if curElement == majority:
         count += 1
      else:
         count -= 1
      if count == 0:
         majority = curElement
         count = 1

   # verify
   count = 0
   for ele in arr:
      if ele == majority:
         count += 1
   if count > len(arr)//2:
      return majority
   return "No majority element found"

arr = [1, 3, 2, 3, 4, 3, 3]
print(getMajority(arr))

arr = [1, 3, 2, 3, 4, 3]
print(getMajority(arr))