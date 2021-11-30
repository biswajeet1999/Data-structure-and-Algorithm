def getMaxProfit(jobs):
   jobs.sort(key=lambda job: job[1])
   profits = [0 for _ in jobs]
   profits[0] = jobs[0][2]
   maxProfit = jobs[0][2]

   for idx in range(1, len(jobs)):
      start = jobs[idx][0]
      profit = jobs[idx][2]
      curMaxProfit = profit
      for j in range(0, idx):
         if(jobs[j][1] <= start):
            curMaxProfit = max(curMaxProfit, profit + profits[j])
      profits[idx] = curMaxProfit
      maxProfit = max(maxProfit, profits[idx])
      
   return maxProfit

jobs = [ (3, 10, 20), (1, 2, 50),
           (6, 19, 100), (2, 100, 200) ]
print(getMaxProfit(jobs))