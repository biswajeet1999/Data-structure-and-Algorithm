def longestCommonPrefix(strs) -> str:
        if len(strs) == 0:
          return ""
        longestLength = 0
        minLength = float("inf")
        for string in strs:
          minLength = min(minLength, len(string))
        for i in range(minLength):
          char = strs[0][i]
          for j in range(1, len(strs)):
            if strs[j][i] != char:
              return strs[0][:longestLength]
          longestLength += 1
        return strs[0][:longestLength]
