def shiftedBinarySearchHelper(array, start, end, valueToSearch):
   while start <= end:
      mid = (start + end) // 2
      if array[mid] == valueToSearch:
         return mid
      elif array[start] <= array[mid]: # left sorted array
         if valueToSearch < array[mid] and valueToSearch >= array[start]:
            end = mid - 1
         else:
            start = mid + 1
      else: # right sorted array
         if array[mid] < valueToSearch and valueToSearch <= array[end]:
            start = mid + 1
         else:
            end = mid - 1
   return -1

def shiftedBinarySearch(array, valueToSearch):
   return shiftedBinarySearchHelper(array, 0, len(array) - 1, valueToSearch)



array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 45]
valueToSearch = 33
print(shiftedBinarySearch(array, valueToSearch))