# BFS
def waterJug(m, n, target):
   queue = []
   visited = {}
   path = []
   queue.append((0, 0))
   visited[(0, 0)] = True
   solutionPossible = False
   while len(queue) > 0:
      curState = queue.pop(0)
      path.append(curState)
      
      if isFinalStateReached(curState, target):
         solutionPossible = True
         break
      
      # fill
      if (m, curState[1]) not in visited:
         visited[(m, curState[1])] = True
         queue.append((m, curState[1]))
      if (curState[0], n) not in visited:
         visited[(curState[0], n)] = True
         queue.append((curState[0], n))

      # empty
      if (0, curState[1]) not in visited:
         visited[(0, curState[1])] = True
         queue.append((0, curState[1]))
      if (curState[0], 0) not in visited:
         visited[(curState[0], 0)] = True
         queue.append((curState[0], 0))

      # transfer

      # transfer water from jug2 to jug1
      waterRequiredInJug1 = m - curState[0]
      # make jug1 full
      newState = (curState[0] + waterRequiredInJug1, curState[1] - waterRequiredInJug1)
      if isValidState(newState, m, n) and newState not in visited:
         visited[newState] = True
         queue.append(newState)
      # make jug2 empty
      newState = (curState[0] + curState[1], 0)
      if isValidState(newState, m, n) and newState not in visited:
         visited[newState] = True
         queue.append(newState)

      # transfer water from jug1 to jug2
      # make jug2 full
      waterRequiredInJug2 = n - curState[1]
      newState = (curState[0] - waterRequiredInJug2, curState[1] + waterRequiredInJug2)
      if isValidState(newState, m, n) and newState not in visited:
         visited[newState] = True
         queue.append(newState)
      # make jug1 empty
      newState = (0, curState[1] + curState[0])
      if isValidState(newState, m, n) and newState not in visited:
         visited[newState] = True
         queue.append(newState)
      
   return (solutionPossible, path)

def isValidState(newState, m, n):
   if 0 <= newState[0] <= m and 0 <= newState[1] <= n:
      return True
   return False

def isFinalStateReached(curState, target):
   if curState == (0, target) or curState == (target, 0):
      return True
   return False

print( waterJug(4, 3, 2) )