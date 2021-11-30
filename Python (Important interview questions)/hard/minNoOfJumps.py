# O(n^2) time | O(n) space
# def minJumps(array = []):
#    jumps = [float("inf") for _ in array]
#    jumps[-1] = 0
#    for i in range(len(array) - 1, -1, -1):
#       for j in range(1, array[i]+1):
#          if i + j >= len(array):
#             break
#          jumps[i] = min(jumps[i], 1 + jumps[i + j])
#    return jumps[0]

# O(n) time | O(1) space
def minJumps(array = []):
   if len(array) == 1:
      return 0
   maxReach = array[0]
   steps = array[0]
   jumps = 0
   for i in range(1, len(array)):
      steps -= 1
      maxReach = max(maxReach, i + array[i])
      if steps == 0:
         jumps += 1
         steps = maxReach - i
   return jumps + 1


array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
print(minJumps(array))