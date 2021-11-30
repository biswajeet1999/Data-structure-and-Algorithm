# O(n*log(n)) time | O(n) space
def merge(intervals):
   intervals.sort(key = lambda interval: interval[0])
   mergedIntervals = [intervals[0]]
   for i in range(1, len(intervals)):
      lastInterval = mergedIntervals[-1]
      currentInterval = intervals[i]
      if currentInterval[0] <= lastInterval[1]:
            lastInterval[1] = max(lastInterval[1], currentInterval[1])
      else:
            mergedIntervals.append(currentInterval)
   return mergedIntervals