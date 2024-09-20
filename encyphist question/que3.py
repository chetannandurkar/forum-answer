#  Depth-First Search
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
        
    visited.add(vertex)
    print(vertex, end=' ')  # Process the current vertex

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS Traversal (Recursive):")
dfs_recursive(graph, 'A')


