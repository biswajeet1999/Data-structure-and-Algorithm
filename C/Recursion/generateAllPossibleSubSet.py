# time complexity:- O(2^n)

def generateSubset(l, n, cur = 0, subList = []):
    if cur >= n:
        print(subList)
        return
    generateSubset(l, n, cur+ 1, subList)
    subList.append(l[cur])
    generateSubset(l, n, cur+ 1, subList)
    subList.pop()



l = [1, 2, 3, 4]
generateSubset(l, len(l))