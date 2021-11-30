# O(n) time | O(1) space
def sort012(array):
   counts = [0 for i in range(3)]

   for ele in array:
      counts[ele] += 1
   idx = 0
   for ele, freq in enumerate(counts):
      for _ in range(freq):
         array[idx] = ele
         idx += 1

   return array   


array = [2, 1, 0, 2, 1, 0, 0, 1, 2, 2, 1, 1]
print(sort012(array))