def getMinSwaps(brackets):
   openingBrackets = []
   closingBrackets = []
   noOfSwaps = 0
   for bracket in brackets:
      if bracket == '[':
         if len(closingBrackets) == 0:
            openingBrackets.append("[")
         else:
            noOfSwaps += 1
            closingBrackets.pop()
      else:
         if len(openingBrackets) == 0:
            closingBrackets.append(']')
         else:
            openingBrackets.pop()
   return noOfSwaps


string = "[]][]["
print(getMinSwaps(string))