def buildSequence(array = [], sequences = [], maxSumIdx = -1):
   curIdx = maxSumIdx
   seq = []
   while True:
      seq.append(array[curIdx])
      if curIdx == sequences[curIdx]:
         break
      curIdx = sequences[curIdx]
   return list(reversed(seq))

def maxSumIncreasingSubsequence(array = []):
   sums = array[:]
   sequences = [i for i in range(len(array))]
   maxSumIdx = 0

   for i in range(1, len(array)):
      currNum = array[i]
      for j in range(0, i):
         if currNum > array[j] and sums[j] + currNum > sums[i]:
            sums[i] = sums[j] + currNum
            sequences[i] = j
      if sums[i] > sums[maxSumIdx]:
         maxSumIdx = i
   print(sequences, maxSumIdx)
   return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]

array = [8, 12, 2, 3, 15, 5, 7]
print(maxSumIncreasingSubsequence(array))