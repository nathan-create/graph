class Node():
    def __init__(self, index, val = None):
        self.index = index
        self.parents = []
        self.children = []
        self.val = val
        self.dist = None
        self.prev = None

class DirectedGraph():
    def __init__(self, edges):
        self.edges = edges
        index_list = []
        for pair in edges:
            index_list.append(pair[0])
            index_list.append(pair[1])
        self.nodes = [Node(num) for num in range(max(index_list) + 1)]

    def build_from_edges(self):
        for pair in self.edges:
            self.nodes[pair[0]].children.append(self.nodes[pair[1]])
            self.nodes[pair[1]].parents.append(self.nodes[pair[0]])
    
    def get_nodes_breadth_first(self, node_index):
        queue = [self.nodes[node_index]]
        visited = []
        while len(queue) != 0:
            curr_node = queue[0]
            visited.append(curr_node)
            for child in curr_node.children:
                if child not in visited and child not in queue:
                    queue.append(child)
            queue.remove(curr_node)
        return visited

    def get_nodes_depth_first(self, node_index):
        stack = [self.nodes[node_index]]
        visited = []
        while len(stack) != 0:
            curr_node = stack[0]
            visited.append(curr_node)
            for child in curr_node.children:
                if child not in visited and child not in stack:
                    stack.insert(0, child)
            stack.remove(curr_node)
        return visited

    def set_breadth_first_dist_and_prev(self, start_node_index):
        for node in self.nodes:
            node.dist = None
            node.prev = None
        first_node = self.nodes[start_node_index]
        first_node.dist = 0
        queue = [first_node]
        visited = []
        while len(queue) != 0:
            curr_node = queue[0]
            visited.append(curr_node)
            for child in curr_node.children:
                if child not in visited and child not in queue:
                    queue.append(child)
                    child.dist = curr_node.dist + 1
                    child.prev = curr_node
            queue.remove(curr_node)
    
    def calc_dist(self, start_node, end_node):
        self.set_breadth_first_dist_and_prev(start_node)
        if self.nodes[end_node].dist == None:
            return False
        return self.nodes[end_node].dist
    
    def calc_shortest_path(self, start_node, end_node):
        self.set_breadth_first_dist_and_prev(start_node)
        curr_node = self.nodes[end_node]
        if curr_node.dist == None:
            return False
        node_index_list = [curr_node.index]
        while curr_node.index != start_node:
            node_index_list.append(curr_node.prev.index)
            curr_node = curr_node.prev
        return node_index_list[::-1]
