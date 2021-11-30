def isVallidPages(pages, noOfStudents, maxPages):
   student = 1
   allocatedPages = pages[0]

   for idx in range(1, len(pages)):
      if(allocatedPages + pages[idx] > maxPages):
         student += 1
         allocatedPages = pages[idx]
      else:
         allocatedPages += pages[idx]
   return noOfStudents == student

# O(nlogn) time | O(1) space
def getMinPages(pages, noOfStudents):
   maxPages = sum(pages)
   minPages = pages[-1]
   result = 0
   while(minPages <= maxPages):
      mid = (minPages + maxPages)// 2
      if(isVallidPages(pages, noOfStudents, mid)):
         result = mid
         maxPages = mid - 1
      else:
         minPages = mid + 1
   return result

print(getMinPages([12,34,67,90], 2))