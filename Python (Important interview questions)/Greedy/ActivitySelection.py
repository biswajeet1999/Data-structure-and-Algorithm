# O(nlogn) time | O(n) space
def selectMeetings(start, finish):
   mergedTime = [(start[i], finish[i]) for i in range(len(start))]
   mergedTime.sort(key = lambda x:x[1] ) # sort based on end time
   scheduledMeetings = []
   for meeting in mergedTime:
      if len(scheduledMeetings) == 0:
         scheduledMeetings.append(meeting)
      else:
         lastMeeting = scheduledMeetings[-1]
         if meeting[0] > lastMeeting[1]:
            scheduledMeetings.append(meeting)
   return scheduledMeetings

print(selectMeetings([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))