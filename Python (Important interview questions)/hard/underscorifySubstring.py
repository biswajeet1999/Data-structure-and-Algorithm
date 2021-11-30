# O(nm) time | O(n) space
def getPatternLocations(string, pattern):
   curIdx = 0
   n = len(string)
   m = len(pattern)
   locations = []
   while curIdx <= n-m:
      patternIdx = string.find(pattern, curIdx)
      if patternIdx == -1:
         break
      locations.append([patternIdx, patternIdx + m])
      curIdx = patternIdx + 1
   return locations
      
# O(n) time | O(n) space
def collapseLocation(locations):
   collapsedLocations = [locations[0]]
   for i in range(1, len(locations)):
      if collapsedLocations[-1][1] >= locations[i][0]:
         collapsedLocations[-1][1] = locations[i][1]
      else:
         collapsedLocations.append(locations[i])
   return flattenLocation(collapsedLocations)

# O(n) time | O(n) space
def flattenLocation(collapsedLocations):
   flattenLocations = []
   for location in collapsedLocations:
      flattenLocations.extend(location)
   return flattenLocations

# O(n) time | O(n) space
def underscorify(string, collapsedLocations):
   result = []
   currentUnderScorPosition = 0
   for i in range(len(string)):
      if currentUnderScorPosition < len(collapsedLocations) and i == collapsedLocations[currentUnderScorPosition]:
         result.append("_")
         currentUnderScorPosition += 1
      result.append(string[i]) 
   if collapsedLocations[-1] == len(string):
      result.append("_")  
   return "".join(result)

# O(nm) time | O(n) space
def underscorifySubstring(string, pattern):
   locations = getPatternLocations(string, pattern)
   # print(locations) [[0, 4], [14, 18], [18, 22], [33, 37], [36, 40], [39, 43]]
   collapsedLocations = collapseLocation(locations)
   # print(collapsedLocations) [0, 4, 14, 22, 33, 43]
   return underscorify(string, collapsedLocations)


string = "testthis is a testtest to see if testestest it workstest"
pattern = "test"
print(underscorifySubstring(string, pattern))