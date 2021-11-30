def getProductArray(arr):
   leftProduct = [1 for _ in arr]
   rightProduct = [1 for _ in arr]
   product = 1
   result = []
   for idx in range(1, len(arr)):
      product *= arr[idx-1]
      leftProduct[idx] = product
   product = 1
   for idx in range(len(arr) - 2, -1, -1):
      product *= arr[idx+1]
      rightProduct[idx] = product
   
   for idx in range(len(arr)):
      result.append(leftProduct[idx] * rightProduct[idx])
   return result
   

print(getProductArray([10, 3, 5, 6, 2]))