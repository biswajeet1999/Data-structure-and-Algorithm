# O(2^(n+m)) time | O(n+m)
# def interweavingString(str1, str2, str3):
#    return interweavingStringHelper(str1, str2, str3, 0, 0, 0)

# def interweavingStringHelper(str1, str2, str3, i, j, k):
#    if k == len(str3) and j == len(str2) and i == len(str1):
#       return True
#    elif k == len(str3) or (i == len(str1) and j == len(str2)):
#       return False
#    elif i == len(str1):
#       if str2[j] == str3[k]:
#          return interweavingStringHelper(str1, str2, str3, i, j+1, k+1)
#       return False
#    elif j == len(str2):
#       if str1[i] == str3[k]:
#          return interweavingStringHelper(str1, str2, str3, i+1, j, k+1)
#       return False
#    # handle bsecase
#    elif str1[i] == str2[j] == str3[k]:
#       return interweavingStringHelper(str1, str2, str3, i+1, j, k+1) or interweavingStringHelper(str1, str2, str3, i, j+1, k+1)
#    elif str1[i] == str3[k]:
#       return interweavingStringHelper(str1, str2, str3, i+1, j, k+1)
#    elif str2[j] == str3[k]:
#       return interweavingStringHelper(str1, str2, str3, i, j+1, k+1)
#    return False

# O(2^(n+m)) time | O(n+m)
# def interweavingString(str1, str2, str3):
#    return interweavingStringHelper(str1, str2, str3, 0, 0)

# def interweavingStringHelper(str1, str2, str3, i, j):
#    k = i + j
#    if k == len(str3):
#       return True
#    if i < len(str1) and str1[i] == str3[k]:
#       if interweavingStringHelper(str1, str2, str3, i+1, j):
#          return True
#    if j < len(str2):
#       return interweavingStringHelper(str1, str2, str3, i, j+1)
#    return False


# O(n*m) time | O(n*m)
def interweavingString(str1, str2, str3):
   return interweavingStringHelper(str1, str2, str3, 0, 0, cache = {})

def interweavingStringHelper(str1, str2, str3, i, j, cache = {}):
   if (i, j) in cache:
      return cache[(i, j)]
   k = i + j
   if k == len(str3):
      cache[(i, j)] = True
      return True
   if i < len(str1) and str1[i] == str3[k]:
      if interweavingStringHelper(str1, str2, str3, i+1, j):
         cache[(i, j)] = True
         return True
   if j < len(str2):
      cache[(i, j)] = interweavingStringHelper(str1, str2, str3, i, j+1)
      return cache[(i, j)]
   cache[(i, j)] = False   
   return False




str1 = "aaa"
str2 = "aaaf"
str3 = "aaafaaa"

print(interweavingString(str1, str2, str3))