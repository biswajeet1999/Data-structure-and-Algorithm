def allSubSequence(string):
   return subsequenceUtil(string, 0, len(string), [], [])

def subsequenceUtil(s, curIdx, length, subSequence, result):

   if(curIdx == length):
      result.append("".join(subSequence))
      return
   #  dont add current character
   subsequenceUtil(s, curIdx + 1, length, subSequence, result)
   subSequence.append(s[curIdx])
   subsequenceUtil(s, curIdx + 1, length, subSequence, result)
   subSequence.pop()
   return result



s = "abc"
print(allSubSequence(s))