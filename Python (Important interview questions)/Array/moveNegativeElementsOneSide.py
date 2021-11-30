# O(n) time | O(1) space
def moveNegatives(array):
   idxToReplace = 0
   while array[idxToReplace] < 0:
      idxToReplace += 1
   for idx in range(idxToReplace + 1, len(array)):
      if array[idx] < 0:
         swap(array, idxToReplace, idx)
         idxToReplace += 1
   return array

def swap(array, i, j):
   array[i], array[j] = array[j], array[i]

array = [3, 2, -1, 4, -2, 3, -7, -8]
print(moveNegatives(array))