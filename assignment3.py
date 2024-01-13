from collections import deque

class Graph:
    def __init__(self, adjacency_list):
        self.graph = adjacency_list

def find_cycles(graph):
    visited = set()
    all_cycles = []

    def dfs(node, current_path):
        visited.add(node)
        print("Visiting:", node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, current_path + [neighbor])
            elif neighbor in current_path:
        
                cycle = current_path[current_path.index(neighbor):]
                all_cycles.append(cycle)
            elif len(current_path) == 1 and neighbor == current_path[0]:
             
                cycle = [current_path[0], neighbor]
                all_cycles.append(cycle)
       
    print("\nDFS Tree:")
    for node in graph:
        if node not in visited:
            print("Starting DFS from:", node)
            dfs(node, [node])


    print("\nCycles:")
    for cycle in all_cycles:
        print("Cycle:", cycle)

    return all_cycles

def bfs(graph, start_node):
    visited = set()
    bfs_tree = {}
    queue = deque([(start_node, None)])

    while queue:
        current_node, parent = queue.popleft()

        if current_node not in visited:
            visited.add(current_node)
            bfs_tree.setdefault(parent, []).append(current_node)

           
            neighbors = sorted(graph[current_node])
            queue.extend((neighbor, current_node) for neighbor in neighbors if neighbor not in visited)

    return bfs_tree

def print_tree(tree, level=0, parent=None):
    indent = '  ' * level
    node_str = f"{indent}Node: {parent}" if parent is not None else f"{indent}Root: {tree[parent][0]}"
    print(node_str)

    children = tree.get(parent, [])
    for child in children:
        print_tree(tree, level + 1, child)

def is_bipartite(cycles):
    for cycle in cycles:
        if len(cycle) % 2 == 1:
            return False
    return True


adjacency_list = {1: [3, 4], 2: [1, 3], 3: [4], 4: [1, 2]}
g = Graph(adjacency_list)

cycles = find_cycles(adjacency_list)

if is_bipartite(cycles):
    print("\nThe graph is bipartite.")
else:
    print("\nThe graph is not bipartite.")

bfs_tree = bfs(g.graph, 1)
print("\nBFS Tree:")
print_tree(bfs_tree)
