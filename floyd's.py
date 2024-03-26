
def floyd(graph):
    n = len(graph)
    
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u in range(n):
        for v, w in graph[u]:
            dist[u][v] = w
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

graph = [
    [(1, 3), (3, 8)],   
    [(2, 2)],            
    [(3, 1)],           
    [(0, 4), (2, 7)]     
]

shortest_paths = floyd(graph)

print("Shortest paths between all pairs of vertices:")
for i in range(len(shortest_paths)):
    for j in range(len(shortest_paths[i])):
        print(f"Shortest path from vertex {i} to vertex {j}: {shortest_paths[i][j]}")
