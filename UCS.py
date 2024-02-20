from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights.get((from_node, to_node), float('inf'))

def ucs(graph, initial, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, initial))

    while not queue.empty():
        cost, node = queue.get()

        if node not in visited:
            visited.add(node)
            print(f"Visited Node: {node}")
            if node == goal:
                print(f"Goal {goal} reached with cost {cost}!")
                return

            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    total_cost = cost + graph.get_cost(node, neighbor)
                    queue.put((total_cost, neighbor))

graph = Graph()
graph.edges = {'A': ['B', 'C'], 'B': ['D'], 'C': [], 'D': []}
graph.weights = {('A', 'B'): 1, ('A', 'C'): 2, ('B', 'D'): 3}


ucs(graph, 'A', 'D')
