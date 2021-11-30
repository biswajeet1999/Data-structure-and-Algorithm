# O(n1 + n2 + n3) time | O(max(n1, n2, n3)) space
def getCommon(arr1, arr2, arr3):
   i, j, k = 0, 0, 0
   result = []
   while i < len(arr1) and j < len(arr2) and k < len(arr3):
      num1 = arr1[i]
      num2 = arr2[j]
      num3 = arr3[k]
      maxx = max(num1, num2, num3)
      if num1 < maxx:
         i+=1
      if num2 < maxx:
         j+=1
      if num3 < maxx:
         k+=1
      if num1 == num2 == num3:
         if len(result) == 0 or result[-1] != num1:
            result.append(num1)
         i += 1
         j += 1
         k += 1
   return result


arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
print(getCommon(arr1, arr2, arr3))