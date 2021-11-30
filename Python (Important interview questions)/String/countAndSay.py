# O(2^n) time | O(2^n + n) space
# worst case in each case the string get doubled so time become 2^n
# in order to store prevNum we need 2^n space bcz string get doubled and n stack space

# def countAndSay(n):
#    return countAndSayHelper(n, None)

# def countAndSayHelper(n, prevNum):   
#    if n == 0:
#       return prevNum
   
#    curNum = generateNum(prevNum)
#    return countAndSayHelper(n-1, curNum)

# def generateNum(prevNum):
#    if prevNum == None:
#       return '1'
   
#    curNum = ''
#    idx = 0
#    while idx < len(prevNum):
#       cnt = count(prevNum, idx)
#       curNum += str(cnt) + prevNum[idx]
#       idx += cnt
#    return curNum

# def count(s, idx):
#    cnt = 0
#    targetChar = s[idx]
#    for i in range(idx, len(s)):
#       if s[i] != targetChar:
#          break
#       cnt += 1
#    return cnt

def countAndSay(n, prevNum):
   if n == 0:
      return prevNum
   
   curNum = generateNum(prevNum)
   
   return countAndSay(n-1, curNum)


def generateNum(prevNum):
   if prevNum == None:
      return '1'
   
   curNum = ''
   print(prevNum)
   curChar = prevNum[0]
   freq = 1

   for idx in range(1, len(prevNum)):
      if prevNum[idx] == curChar:
         freq += 1
      else:
         curNum += (str(freq)+curChar)
         curChar = prevNum[idx]
         freq = 1
   curNum += (str(freq)+curChar)
   return curNum
   

print(countAndSay(5, None))