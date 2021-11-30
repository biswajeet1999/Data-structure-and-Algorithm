# O(nlogn) time | O(1) space
def get(arr):
   arr.sort()
   leftSum = sum(arr)
   rightSum = 0
   count = 0

   for i in range(len(arr)-1, -1, -1):
      num = arr[i]
      rightSum += num
      leftSum -= num
      count += 1
      if leftSum < rightSum:
         return count
   return count


arr = [3, 1, 7, 1]
print(get(arr))