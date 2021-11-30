# O(n^2) time | O(n) space
def getKthPermutation(n, k):
   nums = [num for num in range(1, n+1)]
   fact = 1
   for i in range(2, n):
      fact *= i
   kthPermutation = []
   k = k - 1
   while True:
      if k == 0:
         kthPermutation += nums
         return kthPermutation
      group = k // fact
      k = k % fact
      kthPermutation.append(nums.pop(group))
      fact = fact // len(nums)

print(getKthPermutation(4, 17))