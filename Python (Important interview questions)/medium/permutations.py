def swap(array, i, j):
  array[i], array[j] = array[j], array[i]

def permutation(array=[], curIdx=0):
  if curIdx + 1 == len(array):
    print(array)
  else:
    for i in range(curIdx, len(array)):
      swap(array, curIdx, i)
      permutation(array, curIdx + 1)
      swap(array, curIdx, i)

permutation([1, 2, 3])
