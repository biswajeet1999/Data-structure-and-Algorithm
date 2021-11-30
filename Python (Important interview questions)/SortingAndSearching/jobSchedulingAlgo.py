
# O(2^n) time | O(n) space
# def jobScheduling(jobs):
#    jobs.sort(key= lambda x: x[1])
#    return jobSchedulingUtil(jobs, 0)

# def jobSchedulingUtil(jobs, curIdx):
#    if curIdx == len(jobs) - 1:
#       return jobs[curIdx][2]
   
#    # include current job
#    includedProfit = jobs[curIdx][2]
#    nextJobIdx = getNextNonOverLappingJobIdx(jobs, curIdx)
#    if(nextJobIdx != -1):
#       includedProfit += jobSchedulingUtil(jobs, nextJobIdx)
#    # exclude current job
#    excludedProfit = jobSchedulingUtil(jobs, curIdx + 1)
#    # return max of both
#    return max(includedProfit, excludedProfit)

# def getNextNonOverLappingJobIdx(jobs, curIdx):
#    for idx in range(curIdx+1, len(jobs)):
#       if jobs[curIdx][1] <= jobs[idx][0]:
#          return idx
#    return -1



# Dynamic programming solution (Buttom up)
# O(n^2) time | O(n) space

# In getPreviousNonOverLappingJobIdx method we are using linear search which can be replaced by 
# binary search(since array is sorted based on finish time) to get O(nlogn) time 

def getPreviousNonOverLappingJobIdx(jobs, curIdx):
   for idx in range(curIdx - 1, -1, -1):
      if jobs[idx][1] <= jobs[curIdx][0]:
         return idx
   return -1

def jobScheduling(jobs):
   jobs.sort(key= lambda x: x[1])
   profits = [0 for _ in jobs]
   profits[0] = jobs[0][2]
   for idx in range(1, len(jobs)):
      # included profit
      includedProfit = jobs[idx][2]
      previousJobIdx = getPreviousNonOverLappingJobIdx(jobs, idx)
      if(previousJobIdx != -1):
         includedProfit += profits[previousJobIdx]
      # excluded profit
      excludedProfit = profits[idx - 1]
      profits[idx] = max(includedProfit, excludedProfit)
   return profits[-1]


print(jobScheduling([[3, 10, 20], [1, 2, 50], [6, 19, 100], [2, 100, 200]]))