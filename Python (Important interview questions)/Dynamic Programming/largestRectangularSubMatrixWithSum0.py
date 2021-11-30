def maxSubarrayHavingSum0(nums):
   sumCache = {}
   prefixSum = 0
   maxLength = 0
   start = -1
   end = -1
   for idx in range(0, len(nums)):
      prefixSum += nums[idx]
      if prefixSum == 0:
         maxLength = idx+1
         start = 0
         end = idx
      elif prefixSum in sumCache:
         curLength = idx - sumCache[prefixSum]
         if curLength > maxLength:
            maxLength = curLength
            start = sumCache[prefixSum] + 1
            end = idx
      else:
         sumCache[prefixSum] = idx
   return start, end, maxLength


def getLargestSubMatrixHavingSum0(mat):
   rows = len(mat)
   cols = len(mat[0])
   finalLeftCol = -1
   finalRightCol = -1
   finalTopRow = -1
   finalBottomRow = -1
   maxArea = 0
   for left in range(0, cols):
      rowSum = [0 for _ in range(rows)]
      for right in range(left, cols):
         for idx in range(0, rows):
            rowSum[idx] += mat[idx][right]
         top, bottom, length = maxSubarrayHavingSum0(rowSum)
         curArea = length * (right - left + 1)
         if curArea > maxArea and length > 0:
            maxArea = curArea
            finalLeftCol = left
            finalRightCol = right
            finalTopRow = top
            finalBottomRow = bottom
   return finalTopRow, finalLeftCol, finalBottomRow, finalRightCol

mat = [[1,2,1,4,20],
   [8,3,4,2,1],
   [3,8,10,1,3],
   [4,1,1,7,6]
]

mat = [[9, 7, 16, 5 ], 
       [ 1, -6, -7, 3 ],
       [ 1, 8, 7, 9 ], 
       [ 7, -2, 0, 10]
]

print(getLargestSubMatrixHavingSum0(mat))