# O(M^N) time | O(N) space
def mColor(edges, m):
   graph = {}
   colorAssigned = {}
   for edge in edges:
      u,v = edge
      if u not in graph:
         graph[u] = []
      if v not in graph:
         graph[v] = []
      graph[u].append(v)
      graph[v].append(u)
      colorAssigned[u] = None
      colorAssigned[v] = None
   sourceNode = list(graph.keys())[0]
   return mColorUtil(graph, m, sourceNode, None, colorAssigned)

def isColorValid(graph, curNode, curCol, colorAssigned):
   for child in graph[curNode]:
      if colorAssigned[child] == curCol:
         return False
   return True

def mColorUtil(graph, m, curNode, parent, colorAssigned):
   if colorAssigned[curNode]:
      return True
   for color in range(m):
      if isColorValid(graph, curNode, color, colorAssigned):
         colorAssigned[curNode] = color
         # visit each child
         for child in graph[curNode]:
            if child != parent:
               result = mColorUtil(graph, m, child, curNode, colorAssigned)
               if result == False:
                  for child in graph[curNode]:
                     if child != parent:
                        colorAssigned[child] = None
                  break
         else:
            return True
   colorAssigned[curNode] = None
   return False



edges = [(1,2),(2,3),(3,4),(4,1),(1,3)]
print(mColor(edges, 2))