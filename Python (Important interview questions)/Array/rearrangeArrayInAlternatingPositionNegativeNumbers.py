def swap(array, i, j):
   array[i], array[j] = array[j], array[i]

def moveNegativeOneSide(array):
   i = 0
   j = len(array) - 1
   while i < j:
      while i <= j and array[i] < 0: i += 1
      while j >= i and array[j] > 0: j -= 1
      if i < len(array) and j >= 0:
         swap(array, i, j)
      else:
         break

def rearrange(array):
   moveNegativeOneSide(array)
   evnIdx = 0
   oddIdx = 1
   
   while evnIdx < len(array) and array[evnIdx] < 0:
      evnIdx += 1
   
   evnIdx = evnIdx if evnIdx % 2 == 0 else evnIdx + 1
   while evnIdx < len(array) and oddIdx < len(array) and array[evnIdx] > 0 and array[oddIdx] < 0:
      swap(array, oddIdx, evnIdx)
      evnIdx += 2
      oddIdx += 2


array = [-2, 3, 4, -1]
rearrange(array)
print(array)
array = [-2, 3, 1]
rearrange(array)
print(array)
array = [-5, 3, 4, 5, -6, -2, 8, 9, -1, -4]
rearrange(array)
print(array)