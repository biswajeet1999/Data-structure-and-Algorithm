
# O(n) time | O(n) space
def zeroSumSubarray(arr):
   subarraySumStartsAtZero = {0: True}
   summ = 0
   for num in arr:
      summ += num
      if summ in subarraySumStartsAtZero:
         return True
      subarraySumStartsAtZero[summ] = True
   return False

print(zeroSumSubarray([1, 2, -3, 1, -2]))
