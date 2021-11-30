# O(n^2 + m) time | O(m) space
def matchPattern(string, pattern):
   newPattern = flipPattern(pattern)
   isFliped = pattern[0] != newPattern[0]
   count = getCounts(newPattern)

   for lenOfX in range(1, len(string) + 1):
      lenOfY = (len(string) - lenOfX * count["x"]) / count["y"]
      if lenOfY < 0 or lenOfY % 1 != 0:
         continue
      isValid, x, y = validatePattern(string, pattern, lenOfX, int(lenOfY))
      if isValid:
         return [x, y] if not isFliped else [y, x]
   else:
      return []   

def validatePattern(string, pattern, lenOfX, lenOfY):
   potentialTokens = {"x": "", "y": ""}
   idx = 0
   patternIdx = 0
   while idx < len(string):
      if pattern[patternIdx] == "x":
         token = string[idx: idx+lenOfX]
         idx = idx+lenOfX
      else:# pattern[patternIdx] == "y":
         token = string[idx: idx+lenOfY]
         idx = idx+lenOfY
      if potentialTokens[pattern[patternIdx]] == "":
         potentialTokens[pattern[patternIdx]] = token
      elif potentialTokens[pattern[patternIdx]] != token:
         return [False, "", ""]
      patternIdx += 1
   return [True, potentialTokens["x"], potentialTokens["y"]]

def getCounts(pattern):
   count = {"x": 0, "y": 0}
   for char in pattern:
      count[char] += 1
   return count

def flipPattern(pattern):
   if pattern[0] == "x":
      return pattern
   patternMap = {"x": "y", "y": "x"}
   newPattern = []
   for char in pattern:
      newPattern.append(patternMap[char])
   return "".join(newPattern)

string = "gogopowerrangergogopowerranger"
pattern = "xxyxxy"
print(matchPattern(string, pattern))