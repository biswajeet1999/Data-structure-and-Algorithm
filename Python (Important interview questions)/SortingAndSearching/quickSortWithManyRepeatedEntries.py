def quicksort(arr):
   quicksortHelper(arr, 0, len(arr) - 1)

# O(nlogn) best time | O(logn) space best case
# O(n^2) worst time | O(n) space
def quicksortHelper(arr, start, end):
   if(start >= end):
      return
   mid1, mid2 = partation(arr, start, end)

   quicksortHelper(arr, start, mid1 - 1)
   quicksortHelper(arr, mid2 + 1, end)

# O(n) time | O(1) space
def partation(arr, start, end):
   piovetIdx = start
   # move all smaller element to left of piovet element and same and larger elements to the right of piovet element
   for idx in range(start + 1, end + 1):
      if arr[piovetIdx] > arr[idx]:
         if idx - piovetIdx > 1:
            swap(arr, piovetIdx + 1, idx)
         swap(arr, piovetIdx, piovetIdx + 1)
         piovetIdx += 1
   # now in the subarray[piovetIdx: end], put all the element greater than piovet element to the right side of the array
   # and put all piovet elements to the left side of the subarray start at idx piovetIdx
   i = piovetIdx + 1
   j = end

   while i < j:
      while i <= j and arr[i] == arr[piovetIdx]: i += 1
      while j >= i and arr[j] != arr[piovetIdx]: j -= 1
      if i >= j:
         break
      swap(arr, i, j)

   if arr[i] == arr[piovetIdx]:
      return [piovetIdx, i]
   else:
      return [piovetIdx, i - 1]

def swap(arr, i, j):
   arr[i], arr[j] = arr[j], arr[i]


arr = [4, 3, 2, 2, 1, 4, 4, 2, 5, 7]
quicksort(arr)
print(arr)