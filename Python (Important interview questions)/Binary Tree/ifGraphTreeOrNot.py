class Node:
   def __init__(self, vertex):
      self.vertex = vertex
      self.childrens = []


class Graph:
   def __init__(self, relations):
      self.vertices = {}
      self.noOfVertex = 0
      self.buildGraphFromRelations(relations)
   
   def buildGraphFromRelations(self, relations):
      for relation in relations:
         source = relation[0]
         target = relation[1]
         if source not in self.vertices:
            self.vertices[source] = Node(source)
         if target not in self.vertices:
            self.vertices[target] = Node(target)
         self.vertices[source].childrens.append(self.vertices[target])
         self.vertices[target].childrens.append(self.vertices[source])
   def getSource(self):
      return self.vertices[list(self.vertices.keys())[0]]
   
   def printGraph(self):
      graph = {}
      for vertex in self.vertices:
         graph[vertex] = []
         for child in self.vertices[vertex].childrens:
            graph[vertex].append(child.vertex)
      return graph
   

def isTree(graph: Graph):
   # 0: not visited, 1: processing, 2: visited
   status = {v: 0 for v in list(graph.vertices.keys())}
   parent = {}
   queue = []
   sourceNode = graph.getSource()
   queue.append(sourceNode)
   status[sourceNode.vertex] = 1

   while len(queue) > 0:
      curVertex = queue.pop(0)
      status[curVertex.vertex] = 2
      childrens = curVertex.childrens
      
      for child in childrens:
         if curVertex.vertex in parent and parent[curVertex.vertex] == child.vertex:
            continue
         if status[child.vertex] in (1, 2):
            return False
         else:
            queue.append(child)
            status[child.vertex] = 1
            parent[child.vertex] = curVertex.vertex
   for key, val in status.items(): # for isolated vertex
      if val == 0:
         return False
   return True

g = Graph([(1, 0), (2, 0), (0, 3), (3, 4)])
print(isTree(g))

g = Graph([(1, 0), (2, 0), (0, 3), (3, 4), (4, 0)])
print(isTree(g))