
def bellmanford(edges, source):
   vertices = {}
   for edge in edges:
      u, v, _ = edge
      vertices[u] = True
      vertices[v] = True
   noOfVertices = len(vertices.keys())
   distance = {vertex: float('inf') for vertex in vertices}
   parent = {vertex: None for vertex in vertices}
   distance[source] = 0
   
   for _ in range(noOfVertices):
      for edge in edges:
         u, v, cost = edge
         if distance[u] + cost < distance[v]:
            distance[v] = distance[u] + cost
            parent[v] = u
   for edge in edges:
      u, v, cost = edge
      if distance[u] + cost < distance[v]:
         return "Negative cycle"   
   return distance

graph = [
   ('A', 'B', -1),
   ('A', 'C', 4),
   ('B', 'C', 3),
   ('B', 'E', 2),
   ('B', 'D', 2),
   ('D', 'C', 5),
   ('D', 'B', 1),
   ('E', 'D', -3)
]

print(bellmanford(graph, 'A'))




