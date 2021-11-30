def maxSumPairWithDifferenceLessThanK(arr, N, K): 
   arr.sort(reverse=True)
   ans = 0
   idx = 1
   while idx < N:
      if arr[idx-1] - arr[idx] < K:
            ans += arr[idx-1] + arr[idx]
            idx += 2
      else:
            idx += 1
   return ans