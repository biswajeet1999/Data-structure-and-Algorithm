# ref:- https://youtu.be/YHSjvswCXC8

def countPallendromicSubsequences(s, i, j, cache = {}):
   if (i, j) in cache:
      return cache[(i, j)]
   if i > j:
      cache[(i, j)] = 0
      return 0
   if i == j:
      cache[(i, j)] = 1
      return 1   
   if s[i] == s[j]:
      cache[(i, j)] = countPallendromicSubsequences(s, i + 1, j) + countPallendromicSubsequences(s, i, j - 1) + 1
      return cache[(i, j)]
   else:
      cache[(i, j)] =  countPallendromicSubsequences(s, i + 1, j) + countPallendromicSubsequences(s, i, j - 1) - countPallendromicSubsequences(s, i + 1, j - 1)
      return cache[(i, j)]

print(countPallendromicSubsequences("abcd", 0, len("abcd") - 1))
print(countPallendromicSubsequences("aab", 0, len("aab") - 1))
print(countPallendromicSubsequences("aaaa", 0, len("aaaa") - 1))