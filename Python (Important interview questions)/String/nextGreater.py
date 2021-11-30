def nextGreater(digits):
   n = len(digits)

   for idx in range(n-2, -1, -1):
      if digits[idx] < digits[idx + 1]:
         nextGreaterDigitIdx = idx + 1
         for j in range(idx+2, n):
            if digits[j] > digits[idx] and digits[j] < digits[nextGreaterDigitIdx]:
               nextGreaterDigitIdx = j
         swap(digits, idx, nextGreaterDigitIdx)
         reverse(digits, idx + 1, n-1)
         return digits
   return -1

def reverse(digits, start, end):
   while start < end:
      swap(digits, start, end)
      start += 1
      end -= 1

def swap(digits, i, j):
   digits[i], digits[j] = digits[j], digits[i]


digits = [1, 2, 3, 6, 5, 4]
print(nextGreater(digits))