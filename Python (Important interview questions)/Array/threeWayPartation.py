# use the logic of moveNegativeNumber onse side 2 times.
# first move all elements which are less then a to the left of the array
# then move all elements which are greater then b to the right of the array

def threeWayPartation(arr, a, b):
   left = 0
   right = len(arr) - 1
   while left < right:
      while left < right and arr[left] < a: left += 1
      while right >left and arr[right] >= a: right -= 1
      swap(arr, left, right)

   left = 0
   right = len(arr) - 1
   while left < right:
      while left < right and arr[left] <= b: left += 1
      while right > left and arr[right] > b: right -= 1
      swap(arr, left, right)

   return arr

def swap(arr, i, j):
   arr[i], arr[j] = arr[j], arr[i]


arr = [3, 4, 2, 1, 6, 4, 2, 3, 1, 3]
a = 2
b = 3
print(threeWayPartation(arr, a, b))