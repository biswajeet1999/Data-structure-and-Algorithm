

'''

#Backtracking approach

#Time Complexity:- O(2^n-1)
#Space Complexity:- O(n) for call stack
#if we consider the space for finalList then it should be O(n*2^n-1)


def isPallendrom(s):
    return True if s == s[::-1] else False


def generate(s, finalList, currentStringList):

    if(s == ""):
        finalList.append(currentStringList[:])

    for i in range(len(s)):
        if(isPallendrom(s[:i+1])):
            currentStringList.append(s[:i+1])
            generate(s[i+1:], finalList, currentStringList)
            currentStringList.pop()
            

final = []
s = "aab"
generate(s, final, [])
print(final)
'''


'''
Dynamic programming:- Top Down Approach
'''




def isPallendrom(s):
    return True if s == s[::-1] else False

def merge(currentList, nextPallendrom):

    if nextPallendrom == []:
        return [currentList]
    
    mergedList = []
    for ele in nextPallendrom:
        mergedList.append(currentList + ele)
    return mergedList
    

def generate(s):
    if(s == ""):
        return []
    elif len(s) == 1:
        dp[s] = [[s]]
        return dp[s]
    elif dp.get(s) != None:
        return dp[s]
    else:
        result = []
        for i in range(len(s)):
            if isPallendrom(s[:i+1]):
                currentList = [s[:i+1]]
                nextPallendrom = generate(s[i+1:])
                result.extend( merge(currentList, nextPallendrom) )
        dp[s] = result
        return result
                
                    
    


dp = dict()
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
result = generate(s)
print(result)

































