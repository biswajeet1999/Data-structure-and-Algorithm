
# ballmanford algorithm
def getLongestPath(edges, source):
   vertices = {}
   for edge in edges:
      u, v, _ = edge
      vertices[u] = True
      vertices[v] = True
   noOfVertices = len(vertices.keys())
   distance = {vertex: -float('inf') for vertex in vertices}
   parent = {vertex: None for vertex in vertices}
   distance[source] = 0
   
   for _ in range(noOfVertices):
      for edge in edges:
         u, v, cost = edge
         if distance[u] + cost > distance[v]:
            distance[v] = distance[u] + cost
            parent[v] = u
   return distance

graph = [
   (0, 1, 5),
   (0, 2, 3),
   (1, 3, 6),
   (1, 2, 2),
   (2, 4, 4),
   (2, 5, 2),
   (2, 3, 7),
   (3, 5, 1),
   (3, 4, -1),
   (4, 5, -2),
]

print(getLongestPath(graph, 1))




