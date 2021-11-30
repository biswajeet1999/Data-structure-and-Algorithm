# O(n) time | O(min(a, n)) space a = length of alphabet set
# def getLongestSubstringWithoutDuplication(string):
#    longestSubstringRange = [0, 0]
#    longestSubstringLength = 0
#    characterHistory = {}
#    currentRange = [0, 0]
#    currentLength = 0
#    for i in range(0, len(string)):
#       if string[i] in characterHistory and characterHistory[string[i]] >= longestSubstringRange[0]:
#          if currentLength > longestSubstringLength:
#             longestSubstringLength = currentLength
#             longestSubstringRange = currentRange
#          currentRange = [characterHistory[string[i]] + 1, i]
#          currentLength = currentRange[1] - currentRange[0] + 1
#       else:
#          currentLength += 1
#          currentRange[1] = i
#       characterHistory[string[i]] = i
#    return string[longestSubstringRange[0]: longestSubstringRange[1] + 1]

# O(n) time | O(min(a, n)) space a = length of alphabet set
def getLongestSubstringWithoutDuplication(string):
   lastSeen = {}
   longest = [0, 1]
   startIdx = 0
   for i, char in enumerate(string):
      if char in lastSeen and lastSeen[char] >= startIdx:
         startIdx = lastSeen[char] + 1
      if longest[1] - longest[0] < i+1 - startIdx:
         longest = [startIdx, i+1]
      lastSeen[char] = i
   return string[longest[0]: longest[1]]


string = "clementisacap"
print(getLongestSubstringWithoutDuplication(string))