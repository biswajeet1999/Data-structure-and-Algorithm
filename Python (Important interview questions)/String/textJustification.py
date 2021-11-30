def justifyText(words, maxLineWidth):
   if len(words) == 0:
      return ""

   justifiedLines = []
   curLine = []
   curLineLength = 0
   wordLengthPerLine = []
   # add words to the line in gready approach
   for word in words:
      if curLineLength + len(curLine) + len(word) <= maxLineWidth:
         curLine.append(word)
         curLineLength += len(word)
      else:
         justifiedLines.append(curLine)
         wordLengthPerLine.append(curLineLength)
         curLine = [word]
         curLineLength = len(word)
   # append last curLine to the justifiedLines list
   justifiedLines.append(curLine)
   wordLengthPerLine.append(curLineLength)

   # justify lines
   for lineNo, line in enumerate(justifiedLines):

      extraSpaces = maxLineWidth - wordLengthPerLine[lineNo]
      # line with singleWord is also left justified
      if len(line) == 1:
         print(maxLineWidth, wordLengthPerLine[lineNo], extraSpaces)
         line[-1] = line[-1] + " " * extraSpaces
         continue
      # lastline always left justified with single space between each word
      if lineNo == len(justifiedLines) - 1:
         for idx, word in enumerate(line):
            if idx < len(line) - 1: 
               line[idx] = word + " "
         line[-1] = line[-1] + " " * (extraSpaces - (len(line) - 1))        
         break

      noOfGaps = len(line) - 1
      for gaps in range(noOfGaps, 0, -1):
         noOfSpacesPadedAfterEachWord = extraSpaces // gaps
         extraSpaces = extraSpaces % gaps
         for idx in range(gaps):
            line[idx] = line[idx] + " "*noOfSpacesPadedAfterEachWord

   return ["".join(line) for line in justifiedLines]




words =  ["What","must","be","acknowledgment","shall","be"]
maxLineWidth = 16
print(justifyText(words, maxLineWidth))