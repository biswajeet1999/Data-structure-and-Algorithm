class Node:
   def __init__(self, vertex):
      self.vertex = vertex
      self.children = []

#  Directed graph
class Graph:
   def __init__(self, edges = []):
      self.graph = {}
      self.noOfVertices = 0
      self.buildGraphFrom(edges)
   
   def buildGraphFrom(self, edges):
      for (u, v) in edges:
         if u not in self.graph:
            newNode = Node(u)
            self.graph[u] = newNode
            self.noOfVertices += 1
         if v not in self.graph:
            newNode = Node(v)
            self.graph[v] = newNode
            self.noOfVertices += 1
         self.graph[u].children.append(self.graph[v])

def getInDegree(graph: Graph):
   inDegree = {vertex: 0 for vertex in graph.graph.keys()}
   for vertex in graph.graph:
      for child in graph.graph[vertex].children:
         inDegree[child.vertex] += 1
   return inDegree

# O(V+E) time | O(V) space
#  variation of topological sort
def getMinTime(graph):
   # inDegree = {}
   time = {}
   parent = {}
   inDegree = getInDegree(graph)
   queue = []

   for key, val in inDegree.items():
      if val == 0:
         queue.append(key)
         parent[key] = None
   
   while len(queue) > 0:
      curVertex = queue.pop(0)
      if parent[curVertex] == None:
         time[curVertex] = 1
      else:
         time[curVertex] = time[parent[curVertex]] + 1
      
      for child in graph.graph[curVertex].children:
         inDegree[child.vertex] -= 1
         if inDegree[child.vertex] == 0:
            parent[child.vertex] = curVertex
            queue.append(child.vertex)
   return time

graph = Graph([(1, 3), (1, 4), (1, 5), (2, 3), (2, 8), (2, 9), (3, 6), (4, 6), (4, 8), (5, 8), (6, 7), (7, 8), (8, 10)])
print(getMinTime(graph))