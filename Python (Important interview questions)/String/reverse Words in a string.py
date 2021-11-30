class Solution:
    def reverse(self, charList, startIdx, endIdx):
        while startIdx < endIdx:
            charList[startIdx], charList[endIdx] = charList[endIdx], charList[startIdx]
            startIdx += 1
            endIdx -= 1
    
    def reverseWords(self, s: str) -> str:
        charList = list(s)
        n = len(s)
        
#       reverse string
        startIdx = 0
        endIdx = n-1
        self.reverse(charList, startIdx, endIdx)
            
#       reverse each word
        wordStartIdx = 0
        wordEndIdx= 0
        while wordStartIdx < n and wordEndIdx < n:
            while wordStartIdx < n and charList[wordStartIdx] == ' ':
                wordStartIdx += 1
            if wordStartIdx == n:
                break
            wordEndIdx = wordStartIdx + 1
            while wordEndIdx < n and charList[wordEndIdx] != ' ':
                wordEndIdx += 1
            self.reverse(charList, wordStartIdx, wordEndIdx - 1)
            wordStartIdx = wordEndIdx + 1  

#       trim extra spaces
        trimmedEndIdx = 0
        isStartWord = True
        curIdx = 0
        while curIdx < n:
            if charList[curIdx] == ' ':
                curIdx += 1
                continue
            if isStartWord == True:
                charList[trimmedEndIdx] = charList[curIdx]
                isStartWord = False
            elif curIdx > 0 and charList[curIdx - 1] == ' ':
                charList[trimmedEndIdx] = ' '
                trimmedEndIdx += 1
                charList[trimmedEndIdx] = charList[curIdx]
            else:
                charList[trimmedEndIdx] = charList[curIdx]
            trimmedEndIdx += 1
            curIdx += 1
        
        trimmedString = ''.join(charList)[:trimmedEndIdx]
        return trimmedString