# size of arr1 = n, size of arr2 = m
# here the idea is, we assume arr2 as minHeap and for 
# each element in arr1 we remove the first element from the arr2(minHeap)
# and compare with the current elemnt of arr1. if current element in array
# is smaller than first element of arr2(min lement of arr2) then the element 
# of arr1 is in right position. else we swap the current element of arr1 and 
# top element of arr2 then we applow prelocatedown method for the newly added 
# top element in arr2. once we traversed all the element of arr1 then arr1 is 
# sorted but arr2 contains corrent elements which are bigger then arr1 elements 
# but not in sorted order because minHeap doesnot gaurenty the asscending order 
# of elements. so we do heapSort on arr2 which will arrange the elements in 
# descending order. then reverse the arr2 to get elements in ascending order

# O(n*log(m) + m*log(m) + O(m)) time | O(1) space
# O((n+m)*log(m)) time | O(1) space
def merge(arr1, arr2):
   for idx, num in enumerate(arr1):
      numToCompare = arr2[0]
      if numToCompare < num:
         swap(arr1, arr2, idx, 0)
         prelocateDown(arr2, len(arr2) - 1, 0)
   heapSort(arr2)
   arr2.reverse()   

def swap(arr1, arr2, idx1, idx2):
   arr1[idx1], arr2[idx2] = arr2[idx2], arr1[idx1]
# O(m*log(m)) time | O(1) time
def heapSort(arr):
   lastIdx = len(arr) - 1
   while lastIdx > 0:
      arr[0], arr[lastIdx] = arr[lastIdx], arr[0]
      lastIdx -= 1
      prelocateDown(arr, lastIdx, 0)
# O(log(m)) time | O(1) space
def prelocateDown(arr, lastIdx, idx):
   firstChildIdx = 2*idx + 1
   while firstChildIdx <= lastIdx:
      secondChildIdx = 2*idx + 2
      if secondChildIdx > lastIdx or arr[firstChildIdx] < arr[secondChildIdx]:
         idxToSwap = firstChildIdx
      else:
         idxToSwap = secondChildIdx
      if arr[idxToSwap] > arr[idx]:
         return
      arr[idxToSwap], arr[idx] = arr[idx], arr[idxToSwap]
      idx = idxToSwap
      firstChildIdx = 2*idx + 1

   
arr1 = [7, 8, 9, 10]
arr2 = [1, 2, 3, 4, 5, 6]
merge(arr1, arr2)
print(arr1)
print(arr2)