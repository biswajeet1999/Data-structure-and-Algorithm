def calculateNoKills(N, sholdiers, rounds, powers):
   sholdiers.sort()
   sumSoFar = {}
   sumTillNow = 0

   for i in range(N):
      sumTillNow += sholdiers[i]
      sumSoFar[i] = sumTillNow


   for i in range(rounds):
      curPower = powers[i]
      count = getCountUsingBinarySearch(sholdiers, curPower)
      idx = count - 1
      print(count, sumSoFar[idx])


def getCountUsingBinarySearch(arr, key):
   l = 0
   r = len(arr) - 1

   while l <= r:
      mid = (l+r)//2      
      if(arr[mid] <= key):
         if mid+1 <= r and arr[mid+1] <= key:
            l = mid + 1
         else:
            return mid + 1 # returning no of element
      else:
         r = mid - 1
   return 0

calculateNoKills(7, [1, 2, 3, 4, 5, 6, 7], 3, [3, 20, 2])