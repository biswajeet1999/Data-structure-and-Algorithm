# O(V+E) time | O(V) space
def isBipartite(graph):
   stack = []
   stack.append(list(graph.keys())[0])
   color = {}
   color[list(graph.keys())[0]] = 0
   visited = {vertex: False for vertex in graph.keys()}
   
   while len(stack) > 0:
      curVertex = stack.pop()
      visited[curVertex] = True
      
      for child in graph[curVertex]:
         if visited[child] == True:
            if color[child] != 1-color[curVertex]:
               return False
         else:
            color[child] = 1 - color[curVertex]
            stack.append(child)
   return True




graph = {
   1: [2, 4],
   2: [1, 3],
   3: [2, 4],
   4: [3, 1],
   
}

print(isBipartite(graph))