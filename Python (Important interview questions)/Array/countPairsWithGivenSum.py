def countPairs(array, s):
   cache = {}
   result = 0
   for ele in array:
      targetNo = s - ele
      if targetNo in cache:
         result += cache[targetNo]
      if ele not in cache:
         cache[ele] = 0
      cache[ele] += 1
   return result


array = [1, 5, 7, 1]
k = 6
print(countPairs(array, k))

array = [1, 1, 1, 1]
k = 2
print(countPairs(array, k))