# O(n*m) time | O(m) space
def getCommonElement(mat):
   n = len(mat)
   commonTillPrevRow = {}
   commonTIllNow = {element: True for element in mat[0]}

   for row in range(1, n):
      commonTillPrevRow = commonTIllNow
      commonTIllNow = {}

      for element in mat[row]:
         if element in commonTillPrevRow:
            commonTIllNow[element] = True
   return list(commonTIllNow.keys())


mat = [[1, 2, 1, 4, 8], 
       [3, 7, 8, 5, 1], 
       [8, 7, 7, 3, 1], 
       [8, 1, 2, 7, 9]]
print(getCommonElement(mat))