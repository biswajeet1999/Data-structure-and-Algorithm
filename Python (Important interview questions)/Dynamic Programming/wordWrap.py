def getWordWrap(wordLengths, lineLength):
   noOfWords = len(wordLengths)
   costMatrix = [[float("inf") for col in range(noOfWords)] for row in range(noOfWords)]
   minCostWrap = [float('inf') for _ in range(noOfWords)]
   breakPoint = [None for _ in wordLengths]
   # fill cost matrix
   for i in range(noOfWords):
      curLineLength = 0
      gap = 0
      for j in range(i, noOfWords):
         curLineLength += wordLengths[j] + gap
         if curLineLength <= lineLength:
            costMatrix[i][j] = (lineLength - curLineLength)**2
         gap += 1

   # find min cost of rline and break point
   minCostWrap[0] = costMatrix[0][0]
   breakPoint[0] = 0
   for i in range(1, noOfWords):
      for j in range(i, -1, -1):
         currentCost = minCostWrap[j-1]+costMatrix[j][i] if j-1 >= 0 else costMatrix[j][i]
         if minCostWrap[i] > currentCost:
            minCostWrap[i] = currentCost
            breakPoint[i] = j

   # create lines
   lines = []
   curLine = []
   startWordIdxOfTheLine = None
   for i in range(noOfWords-1, -1, -1):
      if startWordIdxOfTheLine is None:
         startWordIdxOfTheLine = breakPoint[i]
      curLine.insert(0, i)
      if i == startWordIdxOfTheLine:
         lines.append(curLine)
         curLine = []
         startWordIdxOfTheLine = None
   return lines[::-1]


print(getWordWrap([3, 2, 2, 6], 6))