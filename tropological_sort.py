from collections import defaultdict

def topological_sort(graph):
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)

    visited = set()
    result = []
    for node in graph:
        if node not in visited:
            dfs(node)
    return result[::-1]

# Example 1
graph1 = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['d'],
    'd': []
}
print(topological_sort(graph1))  # Output: ['a', 'c', 'b', 'd']

# Example 2
graph2 = {
    'a': ['b', 'c'],
    'b': ['c', 'd'],
    'c': ['d'],
    'd': []
}
print(topological_sort(graph2))  # Output: ['a', 'b', 'c', 'd']
