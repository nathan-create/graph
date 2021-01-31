class Node():
    def __init__(self, index, value):
        self.index = index
        self.neighbors = []
        self.value = None

class Graph():
    def __init__(self, edges):
        self.edges = edges
        index_list = []
        for pair in edges:
            index_list.append(pair[0])
            index_list.append(pair[1])
        self.nodes = [Node(i) for i in range(max(index_list) + 1)]

    def build_from_edges(self):
        for pair in self.edges: 
            self.nodes[pair[0]].neighbors.append(self.nodes[pair[1]])
            self.nodes[pair[1]].neighbors.append(self.nodes[pair[0]])

    def get_nodes_breadth_first(self, start_node):
        queue = [self.nodes[start_node]]
        visited = []
        while len(queue) != 0:
            curr_node = queue[0]
            visited.append(curr_node)
            for neighbor in curr_node.neighbors:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
            queue.remove(curr_node)
        return visited

    def get_nodes_depth_first(self, start_node):
        stack = [self.nodes[start_node]]
        visited = []
        while len(stack) != 0:
            curr_node = stack[0]
            visited.append(curr_node)
            for neighbor in curr_node.neighbors:
                if neighbor not in visited and neighbor not in stack:
                    stack.insert(0, neighbor)
            stack.remove(curr_node)
        return visited

    