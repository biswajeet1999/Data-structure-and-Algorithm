# O(n) time | O(1) space
def reverse(array = []):
   i = 0
   j = len(array) - 1

   while i < j:
      array[i], array[j] = array[j], array[i]
      i+=1
      j-=1
   return array

array = [1, 2, 3, 4]
print(reverse(array))