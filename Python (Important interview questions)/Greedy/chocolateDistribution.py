# O(nlogn) time | O(1) space
def getMinDiff(chocos, noOfStudents):
   n = len(chocos)
   chocos.sort()
   minDiff = float("inf")
   for i in range(0, n - noOfStudents + 1):
      minNoOfChoco = chocos[i]
      maxNoOfChoco = chocos[i + noOfStudents - 1]
      diff = maxNoOfChoco - minNoOfChoco
      minDiff = min(minDiff, diff)
   return minDiff

print(getMinDiff([3, 4, 1, 9, 56, 7, 9, 12], 5))