def getLsp(p):
   lsp = [0]
   m = len(p)

   i = 0
   j = 1
   while j < m:
      if p[i] == p[j]:
         lsp.append(i + 1)
         i += 1
         j += 1
      else:
         lsp.append(0)
         if i == 0:
            j += 1
         else:
            i = lsp[i - 1]
   return lsp

def kmp(s, p):
   n = len(s)
   m = len(p)
   result = []
   lsp = getLsp(p)

   j = 0
   i = 0

   while m - j <= n - i:
      if s[i] == p[j]:
         i += 1
         j += 1
      else:
         if j > 0:
            j = lsp[j - 1]
      if j == m:
         result.append(i - m)
         # reset pattern to find overlaping or next pattern in string else you can break here
         j = lsp[j - 1]
   return result

s = "onionion"
p = "onion"
print(kmp(s, p))