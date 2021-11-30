# O(2^n) time | O(n) space
def getNoOfSubsetSum(arr, ranges):
   return subsetSumHelper(arr, 0, ranges, 0)

def subsetSumHelper(arr, idx, ranges, summ):
   if idx == len(arr):
      if summ >= ranges[0] and summ <= ranges[1]:
         return 1
      else:
         return 0
   
   return subsetSumHelper(arr, idx + 1, ranges, summ) + subsetSumHelper(arr, idx + 1, ranges, summ + arr[idx])
   

print(getNoOfSubsetSum([1, -2, 3], [-1, 2]))