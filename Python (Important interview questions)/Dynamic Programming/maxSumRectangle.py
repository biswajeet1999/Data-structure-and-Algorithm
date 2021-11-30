
def kadens(arr):
   maxSum = arr[0]
   start = 0
   end = 0
   curSum = arr[0]
   for idx in range(1, len(arr)):
      if curSum + arr[idx] >= arr[idx]:
         curSum += arr[idx]
         if maxSum < curSum:
            end = idx
      else:
         curSum = arr[idx]
         if maxSum < curSum:
            start = end = idx
      maxSum = max(maxSum, curSum)
   return (start, end, maxSum)

def getMaxSumRectagle(mat):
   rows = len(mat)
   cols = len(mat[0])
   finalLeftCol = -1
   finalRightCol = -1
   finalTopRow = -1
   finalBottomRow = -1
   maxSum = -float('inf')
   for left in range(0, cols):
      rowSum = [0 for _ in range(rows)]
      for right in range(left, cols):
         for idx in range(0, rows):
            rowSum[idx] += mat[idx][right]
         top, bottom, curSum = kadens(rowSum)
         if curSum > maxSum:
            maxSum = curSum
            finalLeftCol = left
            finalRightCol = right
            finalTopRow = top
            finalBottomRow = bottom
   return maxSum, finalLeftCol, finalRightCol, finalTopRow, finalBottomRow

mat = [[1,2,-1,-4,-20],
   [-8,-3,4,2,1],
   [3,8,10,1,3],
   [-4,-1,1,7,-6]
]

print(getMaxSumRectagle(mat))