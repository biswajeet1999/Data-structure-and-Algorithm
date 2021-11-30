def permutation(string):
   if(len(string) == 0):
      return ""
   s = list(string)
   return permutationHelper(s, 0, len(s))

def permutationHelper(s, curIdx, length, result=[]):
   if curIdx == length:
      result.append("".join(s))
   for idx in range(curIdx, length):
      swap(s, curIdx, idx)
      permutationHelper(s, curIdx + 1, length, result)
      swap(s, curIdx, idx)
   return result

def swap(s, i, j):
   s[i], s[j] = s[j], s[i]

s = "ABC"
print(permutation(s))