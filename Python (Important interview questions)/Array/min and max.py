# O(n) time | O(1) space
def maxMin(array = []):
   maxx = array[0]
   minn = array[0]

   for ele in array:
      if ele > maxx:
         maxx = ele
      elif ele < minn:
         minn = ele
   return maxx, minn

array = [1, 2, 3, 4, -5, 2, 5]
print(maxMin(array))