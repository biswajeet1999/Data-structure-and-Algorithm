# O(n!) time | O(n) space
#  there are n places. 1st place can be filled by n city, 2nd place can be filled by n-1 city and so on.
# so time complexity is n!
# def tsp(graph, curVertex, mask):
#    if mask == (1 << len(graph)) - 1:
#       return graph[curVertex][0]
#    minCost = float('inf')   
#    for vertex in range(len(graph)):
#       if mask & (1 << vertex) == 0: # that vertex is not expolored
#          cost = graph[curVertex][vertex] + tsp(graph, vertex, mask|(1 << vertex))
#          minCost = min(minCost, cost)
#    return minCost


# O(2^n*n^2) time | O(2^n*n) space
#  here we are filling dp matrix[2^n][n] so time complexity is 2^n*n^2
def tsp(graph, curVertex, mask):
   dp = [[None for col in range(len(graph))] for row in range(2**len(graph))]
   return tspUtil(graph, curVertex, mask, dp)

def tspUtil(graph, curVertex, mask, dp):
   if mask == (1 << len(graph)) - 1:
      return graph[curVertex][0]
   if dp[mask][curVertex] is not None:
      return dp[mask][curVertex]
   minCost = float('inf')   
   for vertex in range(len(graph)):
      if mask & (1 << vertex) == 0: # that vertex is not expolored
         cost = graph[curVertex][vertex] + tspUtil(graph, vertex, mask|(1 << vertex), dp)
         minCost = min(minCost, cost)
   dp[mask][curVertex] = minCost
   return minCost

graph = [
   [0, 20, 42, 25],
   [20, 0, 30, 34],
   [42, 30, 0, 10],
   [25, 34, 10, 0]
]

print(tsp(graph, 0, 1))