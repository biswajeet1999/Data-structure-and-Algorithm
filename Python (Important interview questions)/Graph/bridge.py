# O(E+V) time | O(V) space
def findBridge(graph):
   discoveryTime = {}
   leastParentDiscoveryTime = {}
   time = [1]
   visited = {vertex: False for vertex in graph.keys()}
   source = list(graph.keys())[0]
   bridges = []
   findBridgeHelper(graph, source, None, visited, time, discoveryTime, leastParentDiscoveryTime, bridges)
   return bridges

def findBridgeHelper(graph, curVertex, parent, visited, time, dt, lpdt, bridges):
   dt[curVertex] = time[0]
   lpdt[curVertex] = time[0]
   time[0] += 1
   visited[curVertex] = True

   # visit each child and after backtrack of child check weather (curVertex, child) edge is bridge or not
   for child in graph[curVertex]:
      if visited[child] == False:
         findBridgeHelper(graph, child, curVertex, visited, time, dt, lpdt, bridges)
         if lpdt[child] > dt[curVertex]:
            bridges.append((curVertex, child))

   # update lpdt of the current vertex
   for child in graph[curVertex]:
      if child != parent:
         lpdt[curVertex] = min(lpdt[curVertex], lpdt[child])


graph = {
   1: [2, 4],
   2: [1, 3],
   3: [2, 4, 5],
   4: [1, 3],
   5: [3, 6, 7],
   6: [5, 7],
   7: [5, 6]
}

print(findBridge(graph))


# for directed graph we can use topological sorting 