# approach 1
# O(n^2) time | O(1) space
# def rotateRectangle(mat, tr, br, lc, rc):
#    count = 0
#    for i in range(lc, rc):
#       temp = mat[tr][lc + count]
#       mat[tr][lc + count] = mat[br - count][lc]
#       mat[br - count][lc] = mat[br][rc - count]
#       mat[br][rc - count] = mat[tr + count][rc]
#       mat[tr + count][rc] = temp
#       count += 1

# def rotateMatrix(mat):
#    n = len(mat)

#    tr, br = 0, n-1
#    lc, rc = 0, n-1

#    while tr < br and lc < rc:
#       rotateRectangle(mat, tr, br, lc, rc)
#       tr += 1
#       br -= 1
#       lc += 1
#       rc -= 1

# approach 2
# O(n^2) time | O(1) space
def transpose(mat):
   for i in range(1, len(mat)):
      for j in range(0, i):
         mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

def swapColumn(mat, l, r):
   for row in range(0, len(mat)):
      mat[row][l], mat[row][r] = mat[row][r], mat[row][l]


def rotateMatrix(mat):
   transpose(mat)

   # swapColumns
   l = 0
   r = len(mat) - 1
   while l < r:
      swapColumn(mat, l, r)
      l += 1
      r -= 1

# Test case 1 
mat = [ [1, 2, 3, 4 ], 
        [5, 6, 7, 8 ], 
        [9, 10, 11, 12 ], 
        [13, 14, 15, 16 ] ] 
          
''' 
# Test case 2 
mat = [ [1, 2, 3 ], 
        [4, 5, 6 ], 
        [7, 8, 9 ] ] 
  
# Test case 3 
mat = [ [1, 2 ], 
        [4, 5 ] ] 
          
'''
  
rotateMatrix(mat)
print(mat)