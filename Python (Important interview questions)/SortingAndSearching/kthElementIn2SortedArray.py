def merge(arr1, start1, end1,  arr2, start2, end2, k):
   counter = 0
   idx1 = start1
   idx2 = start2
   
   while idx1 <= end1 and idx2 <= end2:
      if arr1[idx1] < arr2[idx2]:
         idx1 += 1
         counter += 1
         if counter == k: 
            return arr1[idx1 - 1]
      else:
         idx2 += 1
         counter += 1
         if counter == k:
            return arr2[idx2 - 1]

   if idx1 <= end1:
      return arr1[idx1 + (k - counter) - 1]
   else:
      return arr2[idx2 + (k - counter) - 1]
         

# O(log(m) + log(n) + k) time | O(min(log(m), log(n)) space
def kthElement(arr1, start1, end1,  arr2, start2, end2, k):
   if(start1 > end1):
      return arr2[start2 + k - 1]
   if(start2 > end2):
      return arr1[start1 + k - 1]

   if(len(arr1[start1: end1 +1]) == 1 or len(arr2[start2: end2 +1]) == 1):
      # merge both sublist then return kth ekement
      return merge(arr1, start1, end1,  arr2, start2, end2, k)
   
   mid1 = (start1 + end1)//2
   mid2 = (start2 + end2)//2

   if((mid1 - start1 + 1) + (mid2 - start2 + 1) < k):
      if(arr1[mid1] < arr2[mid2]):
         return kthElement(arr1, mid1 + 1, end1, arr2, start2, end2, k - (mid1 - start1 + 1))
      else:
         return kthElement(arr1, start1, end1, arr2, mid2+1, end2, k - (mid2 - start2 + 1))
   else:
      if(arr1[mid1] < arr2[mid2]):
         return kthElement(arr1, start1, end1, arr2, start2, mid2, k)
      else:
         return kthElement(arr1, start1, mid1, arr2, start2, end2, k)


print(kthElement([2, 3, 6, 7, 9], 0, 4, [1, 4, 8, 10], 0, 3, 5))