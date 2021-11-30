def canSurvive(totalDays, maxUnitPerDay, requiredUnitPerDay):
   if maxUnitPerDay < requiredUnitPerDay or (totalDays > 6 and 6*maxUnitPerDay < 7*requiredUnitPerDay):
      return ("No", float('inf'))
   
   maxUnitRequiredForSurvive = totalDays * requiredUnitPerDay
   days = maxUnitRequiredForSurvive // maxUnitPerDay
   days += 1 if maxUnitRequiredForSurvive % maxUnitPerDay != 0 else 0
   return ("Yes", days)
   