def union(arr1, arr2):
   result = []
   idx1 = 0
   idx2 = 0
   while idx1 < len(arr1) and idx2 < len(arr2):
      if arr1[idx1] < arr2[idx2]:
         result.append(arr1[idx1])
         idx1 += 1
      elif arr2[idx2] < arr1[idx1]:
         result.append(arr2[idx2])
         idx2 += 1
      else:
         result.append(arr2[idx2])
         idx1 += 1
         idx2 += 1
   while idx1 < len(arr1):
      result.append(arr1[idx1])
      idx1 += 1
   while idx2 < len(arr2):
      result.append(arr2[idx2])
      idx2 += 1
   return result


def intersection(arr1, arr2):
   result = []
   idx1 = 0
   idx2 = 0
   while idx1 < len(arr1) and idx2 < len(arr2):
      if arr1[idx1] < arr2[idx2]:
         idx1 += 1
      elif arr2[idx2] < arr1[idx1]:
         idx2 += 1
      else:
         result.append(arr2[idx2])
         idx1 += 1
         idx2 += 1
   return result


arr1 = [1, 2, 3, 4, 55, 56, 57]
arr2 = [2, 3, 20, 21, 55, 58]
print(union(arr1, arr2))
print(intersection(arr1, arr2))