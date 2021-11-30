# O(log(n)) time | O(1) space
def getLeftMostIdx(array, value, start, end):
   while start <= end:
      mid = (start + end) // 2
      if array[mid] == value:
         if mid > start and array[mid - 1] == value:
            end = mid - 1
         else:
            return mid
      elif value < array[mid]:
         end = mid - 1
      else:
         start = mid + 1
   return -1

# O(log(n)) time | O(1) space
def getRightMostIdx(array, value, start, end):
   while start <= end:
      mid = (start + end) // 2
      if array[mid] == value:
         if mid < end and array[mid + 1] == value:
            start = mid +1
         else:
            return mid
      elif value < array[mid]:
         end = mid - 1
      else:
         start = mid + 1
   return -1
# O(log(n)) time | O(1) space
def getRange(array, value):
   return [getLeftMostIdx(array, value, 0, len(array) - 1), getRightMostIdx(array, value, 0, len(array) -1)]

array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
value = 45

print(getRange(array, value))