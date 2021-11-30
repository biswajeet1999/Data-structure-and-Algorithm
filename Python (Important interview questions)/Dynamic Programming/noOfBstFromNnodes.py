# O(2^(n-2)) time | O(n) space
# def noOfBst(n):
#    if n == 0 or n == 1:
#       return 1
#    if n == 2:
#       return 2
#    ans = 0
#    for root in range(1, n+1):
#       ans += noOfBst(root - 1) * noOfBst(n - root)
#    return ans

# O(n^2) time | O(n) space
cache = {}
def noOfBst(n):
   global cache
   if n in cache:
      return cache[n]
   if n == 0 or n == 1:
      cache[n] = 1
      return cache[n]
   if n == 2:
      cache[n] = 2
      return cache[n]
   ans = 0
   for root in range(1, n+1):
      ans += noOfBst(root - 1) * noOfBst(n - root)
   cache[n] = ans
   return ans


print(noOfBst(40))

