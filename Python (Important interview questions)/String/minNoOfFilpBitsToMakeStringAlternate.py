def getMinFlips(string):
   return min(getMinFlipHelper(string, "0"), getMinFlipHelper(string, "1"))

def getMinFlipHelper(s, startChar):
   strToNumMap = {"0": 0, "1": 1}
   numToStrMap = {0: "0", 1: "1"}

   TargetNum = strToNumMap[startChar]
   count = 0
   for char in s:
      if char != numToStrMap[TargetNum]:
         count += 1
      TargetNum = 1 - TargetNum
   return count


string = "001"
print(getMinFlips(string))

string = "0001010111"
print(getMinFlips(string))
