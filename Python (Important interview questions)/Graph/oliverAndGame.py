def createGraph(n, edges):
   graph = {}
   for u, v in edges:
      if u not in graph:
         graph[u] = []
      if v not in graph:
         graph[v] = []
      graph[u].append(v)
   return graph

def check(visited, discoveryTime, oliver, bob, direction):
   if visited[bob] == False or visited[oliver] == False:
      return False
   if direction == 0:
      return discoveryTime[oliver] < discoveryTime[bob]
   return discoveryTime[oliver] > discoveryTime[bob]

def dfs(graph, curVertex, time, visited, discoveryTime, oliver, bob, direction):
   visited[curVertex] = True
   discoveryTime[curVertex] = time[0]
   time[0] += 1

   if len(graph[curVertex]) == 0:
      return check(visited, discoveryTime, oliver, bob, direction)
   
   for child in graph[curVertex]:
      result = dfs(graph, child, time, visited, discoveryTime, oliver, bob, direction)
      if result == True:
         return True

   # during back track we will make this as unvisited. here we make vertices visited only for current branch and during backtrack
   # make that unvisited so that at leaf node we can check 2 target nodes belong to same branch or not
   visited[curVertex] = False
   return False

# O(V+E) time | O(V) space
def oliverAndGame(n, edges, direction, oliver, bob):
   graph = createGraph(n, edges)
   visited = [False for _ in range(0, n+1)]
   discoveryTime = [float('inf') for _ in range(0, n+1)]
   time = [1]
   result = dfs(graph, 1, time, visited, discoveryTime, oliver, bob, direction)
   return result

edges = [
   [1, 2],
   [1, 3],
   [2, 6],
   [2, 7],
   [6, 9],
   [7, 8],
   [3, 4],
   [3, 5]
]

print(oliverAndGame(9, edges, 0, 2, 8))
print(oliverAndGame(9, edges, 1, 2, 8))
print(oliverAndGame(9, edges, 1, 6, 5))
print(oliverAndGame(9, edges, 0, 6, 5))
print(oliverAndGame(9, edges, 1, 9, 1))