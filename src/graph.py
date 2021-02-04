class Node():
    def __init__(self, index, value = None):
        self.index = index
        self.neighbors = []
        self.value = value

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

    def set_breadth_first_distance_and_previous(self,starting_node_index): 
        for node in self.nodes:
            node.distance = None
            node.previous = None
        main_node = self.nodes[starting_node_index]
        main_node.distance = 0
        queue = [main_node]
        visited = []
        while len(queue) != 0:
            curr_node = queue[0]
            visited.append(curr_node)
            for neighbor in curr_node.neighbors:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    neighbor.distance = curr_node.distance + 1
                    neighbor.previous = curr_node
            queue.remove(curr_node)

    def calc_distance(self, start_node, end_node):
        self.set_breadth_first_distance_and_previous(start_node)
        return self.nodes[end_node].distance
    
    def calc_shortest_path(self, start_node, end_node):
        self.set_breadth_first_distance_and_previous(start_node)
        curr_node = self.nodes[end_node]
        nodes = [curr_node]
        while curr_node.index != start_node:
            nodes.append(curr_node.previous)
            curr_node = curr_node.previous
        return [node.index for node in nodes][::-1]