# O(n) time | O(n) space
def find(array, k):
   cache = {}
   result = []
   n = len(array)
   for ele in array:
      if ele not in cache:
         cache[ele] = 0
      cache[ele] += 1
   
   for key, value in cache.items():
      if value > n // k:
         result.append(key)
   return result


print("First Test", end="\t") 
arr1 = [4, 5, 6, 7, 8, 4, 4] 
k = 3
print(find(arr1, k))
  
print("Second Test", end="\t") 
arr2 = [4, 2, 2, 7] 
k = 3
print(find(arr2, k)) 
  
print("Third Test", end="\t") 
arr3 = [2, 7, 2] 
k = 2
print(find(arr3, k)) 
  
print("Fourth Test", end="\t") 
arr4 = [2, 3, 3, 2] 
k = 3
print(find(arr4, k))