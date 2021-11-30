class Node:
   def __init__(self, vertex):
      self.vertex = vertex
      self.children = []

class Graph:
   def __init__(self, edges = []):
      self.graph = {}
      self.buildFromEdges(edges)
   
   def buildFromEdges(self, edges):
      for edge in edges:
         self.insert(edge)

   def insert(self, edge):
      u, v = edge
      if u not in self.graph:
         newNode = Node(u)
         self.graph[u] = newNode
      if v not in self.graph:
         newNode = Node(v)
         self.graph[v] = newNode
      # undirected graph
      self.graph[u].children.append(self.graph[v])
      self.graph[v].children.append(self.graph[u])

# O(|V+E|) time | O(|V|) space
   def dfs(self):
      isVisited = {vertex: False for vertex in self.graph.keys()}
      result = []
      for vertex in self.graph.keys():
         if isVisited[vertex] == False:
            self.dfsUtil(vertex, isVisited, result)
      return result

   def dfsUtil(self, vertex, isVisited, result):
      result.append(vertex)
      isVisited[vertex] = True
      for childNode in self.graph[vertex].children:
         childVertex = childNode.vertex
         if isVisited[childVertex] == False:
            self.dfsUtil(childVertex, isVisited, result)

graph = Graph([(0, 1), (0, 2), (0, 3), (2, 4)])
print(graph.dfs())