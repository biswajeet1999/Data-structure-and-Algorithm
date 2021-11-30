
# O(p + n) | O(n + p)
def waterConnection(pipeConnections):
   result = []
   pipeConnectionsMap = {connection[0]: (connection[1], connection[2]) for connection in pipeConnections}
   allNodes = {}
   inDegreeNodes = {}
   zeroIndegreeNodes = []
   # store all nodes in all node map and indegree node in indegree map 
   for connection in pipeConnections:
      allNodes[connection[0]] = True
      allNodes[connection[1]] = True
      inDegreeNodes[connection[1]] = True
   for node in allNodes.keys():
      if node not in inDegreeNodes:
         zeroIndegreeNodes.append(node)
   
   for node in zeroIndegreeNodes:
      minDiameter = float("inf")
      curNode = node
      while curNode in pipeConnectionsMap:
         outGoingNode, diameter = pipeConnectionsMap[curNode]
         minDiameter = min(minDiameter, diameter)
         curNode = outGoingNode
      result.append([node, curNode, minDiameter])

   return result
   

print(waterConnection([[7, 4, 98], 
                       [5, 9, 72], 
                       [4, 6, 10 ], 
                       [2, 8, 22 ], 
                       [9, 7, 17], 
                       [3, 1, 66]]))