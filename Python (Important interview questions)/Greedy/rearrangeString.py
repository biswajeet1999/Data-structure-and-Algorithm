
# O(n + 26log(26) + n) time | O(n + 26) space
def rearrange(s):
   freq = {}
   for char in s:
      if char not in freq:
         freq[char] = 0
      freq[char] += 1
   freqList = [[char, f] for char, f in freq.items()]
   freqList.sort(key=lambda x: x[1], reverse=True)
   newStr = []

   while len(freqList) > 0:
      for idx, char in enumerate(freqList):
         newStr.append(char[0])
         char[1] -= 1
         if char[1] == 0:
            freqList.pop(idx)
         if len(newStr) > 1 and newStr[-1] == newStr[-2]:
            return False
   return ''.join(newStr)

print(rearrange('aaabc'))
print(rearrange('aaabb'))
print(rearrange('aa'))
print(rearrange('aaaabc'))
