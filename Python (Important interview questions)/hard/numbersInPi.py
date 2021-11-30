# top down approach
# O(n^2) time | O(n) space
def getMinSpace(pi, numbers = []):
   cache = {}
   minSpaces = getMinSpaceHelper(pi, numbers, cache, 0)
   return -1 if minSpaces == float("inf") else minSpaces

def getMinSpaceHelper(pi, numbers, cache, idx):
   if idx == len(pi):
      return -1
   if idx in cache:
      return cache[idx]
   minSpaces = float("inf")
   for i in range(idx, len(pi)):
      prifix = pi[idx: i + 1]
      if prifix in numbers:
         minSpaceInSuffix = getMinSpaceHelper(pi, numbers, cache, i + 1)
         minSpaces = min(minSpaces, minSpaceInSuffix + 1)
   cache[idx] = minSpaces
   return minSpaces

# bottom up approach
# O(n^2) time | O(n) space
# def getMinSpace(pi, numbers = []):
#    cache = {num: True for num in numbers}
#    minSpaces = [float("inf") for num in numbers]
#    for i in range(len(pi)):
#       for j in range(0, i+1):
#          numberToFind = pi[j: i+1]
#          if numberToFind in cache:
#             minSpaces[i] = min(minSpaces[i], 1 + minSpaces[j - 1]) if j > 0 else 1
#    return minSpaces[-1] - 1   

pi = "3141592"
numbers = ["3141", "5", "31", "2", "4159", "9", "42"]
print(getMinSpace(pi, numbers))
