class Node():
    def __init__(self, data, parent, index, children):
        self.data = data
        self.parent = parent
        self.index = index
        self.children = children

class Tree():
    def __init__(self, edges, node_data):
        self.edges = edges
        self.node_data = node_data
        self.root = Node(None, self.node_data[self.get_root(self.edges)],self.get_root(self.edges),None)
    
    def get_parent(self, index, tree_list):
        for pair in tree_list:
            if pair[1] == index:
                return pair[0]

    def get_children(self, index, tree_list):
        result = []
        for pair in tree_list:
            if pair[0] == index:
                result.append(pair[1])
        return result


    def get_root(self, tree_list):
        for pair in tree_list:
            if self.get_parent(pair[0], tree_list) == None:
                return pair[0]

    def build_from_edges(self):
        current_nodes = [self.root]
        while len(current_nodes) != 0:
            children = []
            for node in current_nodes:
                children = self.get_children(node.data, self.edges)
                for num in range(len(node_children)):
                    children[num] = Node(node, children[num], None)
                node.children = children
                for child in node_children:
                    children.append(child)
            current_nodes = children
    
    def breadth_first_search(self):
        queue = [self.root]
        visited = []
        while len(queue) != 0:
            node = queue[0]
            visited.append(node)
            if node.children != None:
                for child in node.children:
                    queue.append(child)
            queue.remove(node)
        return visited
    
    def depth_first_search(self):
        stack = [self.root]
        visited = []
        while len(stack) != 0:
            first = stack[0]
            visited.append(first)
            if first.children != None:
                for child in first.children:
                    stack.insert(0, child)
            stack.remove(first)
        return visited
