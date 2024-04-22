class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find_parent(parent, x)
        y_root = self.find_parent(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result

# Example 1
g1 = Graph(4)
g1.add_edge(0, 1, 10)
g1.add_edge(0, 2, 6)
g1.add_edge(0, 3, 5)
g1.add_edge(1, 3, 15)
g1.add_edge(2, 3, 4)
print("Minimum Spanning Tree for Graph 1:")
print(g1.kruskal_mst())  # Output: [[2, 3, 4], [0, 3, 5], [0, 1, 10]]

# Example 2
g2 = Graph(4)
g2.add_edge(0, 1, 5)
g2.add_edge(0, 2, 10)
g2.add_edge(0, 3, 20)
g2.add_edge(1, 3, 30)
g2.add_edge(2, 3, 15)
print("\nMinimum Spanning Tree for Graph 2:")
print(g2.kruskal_mst())  # Output: [[0, 1, 5], [2, 3, 15], [0, 2, 10]]
