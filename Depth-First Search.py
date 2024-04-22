def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example 1
graph1 = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': []
}
print("DFS traversal for graph 1:")
dfs(graph1, 'a')  # Output: a b d c

# Example 2
graph2 = {
    'a': ['b', 'c'],
    'b': ['c', 'd'],
    'c': ['d'],
    'd': []
}
print("\nDFS traversal for graph 2:")
dfs(graph2, 'a')  # Output: a b c d
