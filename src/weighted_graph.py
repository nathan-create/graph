class Node():
    def __init__(self, index, val = None):
        self.index = index
        self.val = val
        self.previous = None
        self.neighbors = []
        self.d_val = 99999999

class WeightedGraph():
    def __init__(self, edge_weights, node_vals):
        self.edge_weights = edge_weights
        self.node_vals = node_vals
        self.edges = [key for key in self.edge_weights]
        indices = []
        for pair in self.edges:
            indices.append(pair[0])
            indices.append(pair[1])
        self.nodes = [Node(x, self.node_vals[x]) for x in range(max(indices) + 1)]

    def build_from_edges(self):
        for pair in self.edges: 
            self.nodes[pair[0]].neighbors.append(self.nodes[pair[1]])
            self.nodes[pair[1]].neighbors.append(self.nodes[pair[0]])

    def get_edge_weight(self, first, second):
        for edge in self.edge_weights:
            if first.index in edge and second.index in edge:
                return self.edge_weights[edge]

    def set_distance_and_previous(self, start_index):
        nodes = [node for node in self.nodes]
        start_node = self.nodes[start_index]
        start_node.d_val = 0
        queue = [start_node]
        visited = []
        curr_node = queue[0]
        while len(visited) < len(self.nodes):
            visited.append(curr_node)
            nodes.remove(curr_node)
            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    weight = self.get_edge_weight(curr_node, neighbor)
                    if curr_node.d_val + weight < neighbor.d_val:
                        neighbor.d_val = curr_node.d_val + weight
                    neighbor.previous = curr_node
                    queue.append(neighbor)
            queue.remove(curr_node)

            if len(nodes) != 0:
                smallest_d_val = nodes[0].d_val
                curr_node = nodes[0]
                for node in nodes:
                    if node.d_val < smallest_d_val:
                        curr_node = node
                        smallest_d_val = node.d_val
    

    def calc_distance(self, start, end):
        self.set_distance_and_previous(start)
        if self.nodes[end].d_val == None:
            return False
        return self.nodes[end].d_val