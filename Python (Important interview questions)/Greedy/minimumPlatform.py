# O(m + n) time | O(m + n) space
def minPlatform(arr, dep):
   times = [(t, 'arr') for t in arr]
   for t in dep:
      times.append((t, 'dep'))
   times.sort(key=lambda x: x[0])
   noOfPlatForms = [None for _ in times]
   noOfPlatForms[0] = 1

   for idx in range(1, len(times)):
      noOfPlatfromsSoFar = noOfPlatForms[idx - 1]
      if times[idx][1] == "arr":
         noOfPlatForms[idx] = noOfPlatfromsSoFar + 1
      else:
         noOfPlatForms[idx] = noOfPlatfromsSoFar - 1
   return max(noOfPlatForms)

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(minPlatform(arr, dep))