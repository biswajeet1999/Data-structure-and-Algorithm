# check 2 array are same bst or not without creating bst

# solution 1:-
# O(n) time | O(n) space
# def getSmallerThenRootValues(array = []):
#    root = array[0]
#    values = []
#    for i in range(1, len(array)):
#       if array[i] < root:
#          values.append(array[i])
#    return values

# # O(n) time | O(n) space
# def getLargerThenRootValues(array = []):
#    root = array[0]
#    values = []
#    for i in range(1, len(array)):
#       if array[i] > root:
#          values.append(array[i])
#    return values

# # O(n^2) time | O(n^2) space
# def checkBSTs(array1 = [], array2 = []):
#    if array1 == [] or array2 == []:
#       return array1 == array2

#    root1 = array1[0]
#    root2 = array2[0]

#    leftSubtree1 = getSmallerThenRootValues(array1)
#    rightSubtree1 = getLargerThenRootValues(array1)
   
#    leftSubtree2 = getSmallerThenRootValues(array2)
#    rightSubtree2 = getLargerThenRootValues(array2)

#    return root1 == root2 and checkBSTs(leftSubtree1, leftSubtree2) and checkBSTs(rightSubtree1, rightSubtree2)

# solution 2:- 
# # O(n) time | O(1) space
def getNextSmallerIdx(array, rootIdx, minVal):
   for i in range(rootIdx+1, len(array)):
      if minVal < array[i] < array[rootIdx] :
         return i
   return -1
# # O(n) time | O(1) space
def getNextLargerIdx(array, rootIdx, maxVal):
   for i in range(rootIdx+1, len(array)):
      if array[i] > array[rootIdx] and array[i] < maxVal:
         return i
   return -1
# # O(n^2) time | O(h) space
def checkBSTs(array1, array2, root1Idx, root2Idx, minVal, maxVal):
   if root1Idx == -1 or root2Idx == -1:
      return root1Idx == root2Idx
   if array1[root1Idx] != array2[root2Idx]:
      return False
   
   leftRoot1Idx = getNextSmallerIdx(array1, root1Idx, minVal)
   rightRoot1Idx = getNextLargerIdx(array1, root1Idx, maxVal)
   
   leftRoot2Idx = getNextSmallerIdx(array2, root2Idx, minVal)
   rightRoot2Idx = getNextLargerIdx(array2, root2Idx, maxVal)
   
   currentRoot = array2[root2Idx]
   return checkBSTs(array1, array2, leftRoot1Idx, leftRoot2Idx, minVal, currentRoot) and checkBSTs(array1, array2, rightRoot1Idx, rightRoot2Idx, currentRoot, maxVal)

# we are passing min max value inorder to avoid conflict
# e.g. when calculating next max value for 10 which gives 15 and next max value 8 also 15 (refer array 2) 

array1 = [10, 15, 8, 12, 94, 81, 5, 2, 11]
array2 = [10, 8, 5, 15, 2, 12, 11, 94, 81]
print(checkBSTs(array1, array2, 0, 0, float("-inf"), float("inf")))