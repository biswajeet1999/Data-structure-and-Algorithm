def getMaxSegment(l, a, b, c):
   maxSegmentTill = [0 for _ in range(l + 1)]

   for length in range(1, l+1):
      if length >= a:
         maxSegmentTill[length] = max(maxSegmentTill[length], 1 + maxSegmentTill[length - a])
      if length >= b:
         maxSegmentTill[length] = max(maxSegmentTill[length], 1 + maxSegmentTill[length - b])
      if length >= c:
         maxSegmentTill[length] = max(maxSegmentTill[length], 1 + maxSegmentTill[length - c])
   return maxSegmentTill[-1]

l = 11
p = 2
q = 3
r = 5 
ans = getMaxSegment(l, p, q, r)
print(ans)