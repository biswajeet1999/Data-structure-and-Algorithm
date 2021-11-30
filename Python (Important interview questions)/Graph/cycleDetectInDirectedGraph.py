class Node:
   def __init__(self, vertex):
      self.vertex = vertex
      self.children = []

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
         self.graph[v].children.append(self.graph[u])

   # O(|V| + |E|) time | O(|V|) space
   # detect cycle in undirected graph
   def isCyclePresent(self):
      status = {vertex: 'notVisited' for vertex in self.graph.keys()}
      queue = []
      curNode = list(self.graph.keys())[0]
      queue.append(self.graph[curNode])
      status[curNode] = 'processing'

      while len(queue) > 0:
         curNode = queue.pop(0)
         status[curNode.vertex] = 'visited'

         for child in curNode.children:
            if status[child.vertex] == 'notVisited':
               status[child.vertex] = 'processing'
               queue.append(child)
            else:
               return True
      return False

graph = Graph([(0, 1), (0, 2), (0, 3), (2, 4)])
graph = Graph([(0, 1), (0, 2), (2, 1)])
print(graph.isCyclePresent())
