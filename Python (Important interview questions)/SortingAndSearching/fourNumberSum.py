# method-1:
# O(n) time
# def getTwoNoSum(arr, startIdx, k):
#    i = startIdx
#    j = len(arr) - 1
#    result = []
#    while i < j:
#       summ = arr[i] + arr[j]
#       if summ == k:
#          result.append([arr[i], arr[j]])
#          i += 1
#          j -= 1
#       elif summ > k:
#          j -= 1
#       else:
#          i += 1
#    return result

# O(nlog(n) + n^3) time
# def getFourNoSum(arr, k):
#    arr.sort()
#    result = []
#    for i in range(0, len(arr) - 4 + 1):
#       for j in range(i+1, len(arr) - 3 + 1):
#          remainingSum = k - (arr[i] + arr[j])
#          pairs = getTwoNoSum(arr, j+1, remainingSum)
#          for pair in pairs:
#             res = [arr[i], arr[j], pair[0], pair[1]]
#             result.append(res)
#    return result

# method-2:
# O(n^2) time | O(n^2) space
def getFourNoSum(arr, targetSum):
   result = []
   pairs = {}
   for i in range(1, len(arr)):
      for j in range(i+1, len(arr)):
         requiredSum = targetSum - (arr[i] + arr[j])
         if requiredSum in pairs:
            for pair in pairs[requiredSum]:
               result.append(pair + [arr[i], arr[j]])
      for k in range(0, i):
         summ = arr[i] + arr[k]
         if summ not in pairs:
            pairs[summ] = []
         pairs[summ].append([arr[i], arr[k]])
   return result


arr = [10,2,3,4,5,7,8]
print(getFourNoSum(arr, 23))

arr = [7, 6, 4, -1, 1, 2]
print(getFourNoSum(arr, 16))