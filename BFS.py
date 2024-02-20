from collections import deque

def BFS(graph, initial, goal):
    visited = set()
    queue = deque([initial])

    while queue:
        current_node = queue.popleft()
        visited.add(current_node)

        print(f"Visited Node: {current_node}")

        if current_node == goal:
            print(f"Goal {goal} reached!")
            return

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                queue.append(neighbor)


small_graph = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}

BFS(small_graph, 'A', 'D')
