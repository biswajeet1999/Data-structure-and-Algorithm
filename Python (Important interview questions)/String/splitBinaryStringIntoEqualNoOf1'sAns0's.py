def countBalancedSubstring(s):
   count = 0
   frequency = {'0':0, '1': 0}

   for char in s:
      frequency[char] += 1
      if frequency['0'] == frequency['1']:
         count += 1
         frequency = {'0':0, '1': 0}
   return count


s = "0100110101"
print(countBalancedSubstring(s))
