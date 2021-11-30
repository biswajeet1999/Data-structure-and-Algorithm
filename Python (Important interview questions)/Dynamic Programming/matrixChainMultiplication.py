class Node:
   def __init__(self, row, col, cost):
      self.row = row
      self.col = col
      self.cost = cost
      self.left = self.right = None

def getMinCostMatrix(matrixNodes):
   maxIdx = -1
   maxCost = float('inf')
   for idx in range(1, len(matrixNodes)):
      leftMatrix = matrixNodes[idx - 1]
      rightMatrix = matrixNodes[idx]
      totalCost = leftMatrix.cost + rightMatrix.cost + (leftMatrix.row * rightMatrix.col * leftMatrix.col)
      if totalCost < maxCost:
         maxIdx = idx
         maxCost = totalCost
   return maxIdx
   
# O(n^2) time | O(2n) space
def matrixChainMultiplication(matrixDim):
   matrixNodes = [Node(dim[0], dim[1], 0) for dim in matrixDim]

   while len(matrixNodes) > 1:
      maxCostIdx = getMinCostMatrix(matrixNodes)
      leftMatrix = matrixNodes[maxCostIdx - 1]
      rightMatrix = matrixNodes[maxCostIdx]
      totalCost = leftMatrix.cost + rightMatrix.cost + (leftMatrix.row * rightMatrix.col * leftMatrix.col)
      newMatrixNode = Node(leftMatrix.row, rightMatrix.col, totalCost)
      newMatrixNode.left = leftMatrix
      newMatrixNode.right = rightMatrix
      matrixNodes.pop(maxCostIdx)
      matrixNodes.pop(maxCostIdx - 1)
      matrixNodes.insert(maxCostIdx - 1, newMatrixNode)
   printTree(matrixNodes[-1])
   print()
   return matrixNodes[-1].cost

def printTree(root):
   if root.left == None and root.right ==None:
      print('<{}x{}>'.format(root.row, root.col), end="")
      return
   print('(', end="")
   printTree(root.left)
   printTree(root.right)
   print(')', end="")

print(matrixChainMultiplication([(1, 2), (2, 3), (3, 4)]))
print(matrixChainMultiplication([(5, 4), (4, 6), (6, 2), (2, 7)]))
