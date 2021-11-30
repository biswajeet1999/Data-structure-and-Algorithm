def minJumps(array):
   steps = array[0]
   jumps = 0
   maxJumps = array[0]

   if len(array) == 1:
      return 0

   for i in range(1, len(array) - 1):
      steps -= 1
      maxJumps = max(maxJumps, i + array[i])
      if maxJumps == i:
         return float("inf")
      if steps == 0:
         steps = maxJumps - i
         jumps += 1
   return jumps + 1


array = [3, 4, 1, 2, 2, 1, 0]
print(minJumps(array))
array = [4, 2, 1, 0, 4]
print(minJumps(array))
array = [3, 2, 1, 0, 4]
print(minJumps(array))