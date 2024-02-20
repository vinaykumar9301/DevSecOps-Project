def DFS(graph, initial, goal):
    visited = set()
    stack = [initial]

    while stack:
        current_node = stack.pop()
        visited.add(current_node)

        print(f"Visited Node: {current_node}")

        if current_node == goal:
            print(f"Goal {goal} reached!")
            return

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                stack.append(neighbor)

small_graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}


DFS(small_graph, 'A', 'D')
