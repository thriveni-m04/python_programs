
# Q43. Find Euler Path

def find_euler_path(n, edges):
    graph = [[] for _ in range(n)]
    degree = [0] * n

    # Build graph using edge IDs
    for edge_id, (u, v) in enumerate(edges):
        graph[u].append((v, edge_id))
        graph[v].append((u, edge_id))
        degree[u] += 1
        degree[v] += 1

    print("Node Degrees:")
    for i in range(n):
        print(i, "->", degree[i])

    odd_nodes = [i for i in range(n) if degree[i] % 2 == 1]
    print("Odd Degree Nodes:", odd_nodes)

    # Find a starting node with an edge
    start = -1
    for i in range(n):
        if degree[i] > 0:
            start = i
            break

    # Handle a graph with no edges
    if start == -1:
        print("Euler Path Exists: True")
        print("Start Node: None")
        print("Euler Path: []")
        return

    # Check connectivity of all non-isolated vertices
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        for neighbour, edge_id in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour)

    active_nodes = {i for i in range(n) if degree[i] > 0}

    if visited != active_nodes or len(odd_nodes) not in (0, 2):
        print("Euler Path Exists: False")
        return

    if len(odd_nodes) == 2:
        start = odd_nodes[0]

    print("Euler Path Exists: True")
    print("Start Node:", start)

    # Construct Euler path
    used = [False] * len(edges)
    path = []
    stack = [start]

    while stack:
        node = stack[-1]

        while graph[node] and used[graph[node][-1][1]]:
            graph[node].pop()

        if graph[node]:
            neighbour, edge_id = graph[node].pop()

            if not used[edge_id]:
                used[edge_id] = True
                stack.append(neighbour)
        else:
            path.append(stack.pop())

    path.reverse()

    print("Euler Path:", " -> ".join(map(str, path)))


# Sample input
n = 4
edges = [[0, 1], [1, 2], [2, 0], [1, 3]]

find_euler_path(n, edges)
