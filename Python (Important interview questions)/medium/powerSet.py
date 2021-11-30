# Iterative approach
# O(n*2^n) time | O(n*2^n) space
# def powerset(array):
#   subsets = [[]]
#   for ele in array:
#      for i in range(len(subsets)):
#         currentSubset = subsets[i]
#         subsets.append(currentSubset + [ele])
#   print(subsets)



# Recursive approach
# O(n*2^n) time | O(n*2^n) space
def powerset(lst = [], curIdx = 0, result = [], currentSet = []):
    if curIdx == len(lst):
        result.append(currentSet[:])
        return

    powerset(lst, curIdx + 1, result, currentSet)
    currentSet.append(lst[curIdx])
    powerset(lst, curIdx + 1, result, currentSet)
    currentSet.pop()
    return result


print(powerset([1, 2, 3]))
