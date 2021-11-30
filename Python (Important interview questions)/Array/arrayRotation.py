def rotate(array, k):
   n = len(array)
   k = k % n
   if k == 0:
      return array
   elementToShift = array[0]
   oldIdx = 0
   count = 0
   while count < n:
      newIdx = (oldIdx + k) % n
      temp = array[newIdx]
      array[newIdx] = elementToShift
      oldIdx = newIdx
      elementToShift = temp
      count += 1
   return array

array = [1, 2, 3, 4, 5]
k = 10
print(rotate(array, k))