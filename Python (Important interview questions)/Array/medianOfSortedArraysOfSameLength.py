def findMedian(arr1, arr2):
   # print(arr1, arr2)
   n = len(arr1)
   if n == 1:
      return (arr1[0] + arr2[0])/2

   median1 = getMedian(arr1)   
   median2 = getMedian(arr2)
   if median1 == median2:
      return median1
   elif median1 < median2:
      if n%2 == 0:
         return findMedian(arr1[(n-1)//2+1 :], arr2[: ((n-1)//2) + 1])
      return findMedian( arr1[ (n-1)//2: ], arr2[ : ((n-1)//2) + 1])
   else: 
      if n%2 == 0:
         return findMedian(arr1[: ((n-1)//2) + 1], arr2[((n-1)//2) + 1 :])
      return findMedian(arr1[: ((n-1)//2)+1], arr2[(n-1)//2:])


def getMedian(arr):
   n = len(arr)
   if n%2 == 1:
      return arr[(n-1)//2]
   leftIdx = (n-1)//2
   rightIdx = leftIdx + 1
   return (arr[leftIdx] + arr[rightIdx])/2

arr1 = [1, 2, 3, 6] 
arr2 = [4, 6, 8, 10] 
print(findMedian(arr1,arr2))

arr1 = [1, 3] 
arr2 = [4, 6] 
print(findMedian(arr1,arr2)) 