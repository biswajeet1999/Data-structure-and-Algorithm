# O(V!) time | O(V) space
def isAtleastKLengthPathExists(graph, src, k):
   visited = {vertex: False for vertex in graph.keys()}
   return dfs(graph, src, k, visited)

def dfs(graph, curVertex, k, visited):
   if k <= 0:
      return True
   visited[curVertex] = True
   for child in graph[curVertex]:
      v, cost = child
      if visited[v] == False:
         if dfs(graph, v, k - cost, visited):
            return True
   visited[curVertex] = False
   return False


graph = {
   0: [(1, 4), (7, 8)],
   1: [(2, 8), (7, 11)],
   2: [(3, 7), (8, 2), (5, 4)],
   3: [(4, 9), (5, 14)],
   4: [(5, 10)],
   5: [(6, 2)],
   6: [(7, 1), (8, 6)],
   7: [(8, 7)],
   8: []
}

print(isAtleastKLengthPathExists(graph, 0, 62))
print(isAtleastKLengthPathExists(graph, 0, 49))
