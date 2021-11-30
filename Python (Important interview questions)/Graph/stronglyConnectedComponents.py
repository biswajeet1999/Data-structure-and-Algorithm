def transposeGraph(graph):
   transposedGraph = {}
   for u in graph.keys():
      for v in graph[u]:
         if v not in transposedGraph:
            transposedGraph[v] = []
         transposedGraph[v].append(u)
   return transposedGraph

def dfs(graph, stack):
   visited = {vertex: False for vertex in graph.keys()}
   for vertex in graph.keys():
      if visited[vertex] is False:
         dfsHelper(graph, vertex, visited, stack)

def dfsHelper(graph, vertex, visited, stack):
   visited[vertex] = True
   for child in graph[vertex]:
      if visited[child] == False:
         dfsHelper(graph, child, visited, stack)
   stack.append(vertex)

# modified dfs
def getComponents(graph, stack):
   visited = {vertex: False for vertex in graph.keys()}
   components = []
   while len(stack) > 0:
      vertex = stack.pop()
      if visited[vertex] == False:
         component = []
         dfsHelper(graph, vertex, visited, component)
         components.append(component)
         component = []
   return components

# O(V+E) time | O(V) space
def getStronglyConnectedComponents(graph):
   stack = []
   dfs(graph, stack)
   transposedGraph = transposeGraph(graph)
   components = getComponents(transposedGraph, stack)
   return components

graph = {
   1: [2],
   2: [3],
   3: [4, 5],
   4: [1],
   5: [6],
   6: [7],
   7: [5, 8],
   8: [9],
   9: [8, 10],
   10: []
}

print(getStronglyConnectedComponents(graph))