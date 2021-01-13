class Node():
    def __init__(self, data, parent, children):
        self.data = data
        self.parent = parent
        self.children = children

class Tree():
    def __init__(self, edges):
        self.edges = edges
        self.root = Node(self.get_root(self.edges),None, None)
    
    def get_parents(self, value, tree_list):
        for pair in tree_list:
            if pair[1] == value:
                return pair[0]

    def get_children(self, value, tree_list):
        result = []
        for pair in tree_list:
            if pair[0] == value:
                result.append(pair[1])
        return result


    def get_root(self, tree_list):
        for pair in tree_list:
            if self.get_parents(pair[0], tree_list) == None:
                return pair[0]

    def build_from_edges(self):
        current_nodes = [self.root]
        while len(current_nodes) != 0:
            children = []
            for node in current_nodes:
                node_children = self.get_children(node.data, self.edges)
                for num in range(len(node_children)):
                    node_children[num] = Node(node, node_children[num], None)
                node.children = node_children
                for num in node_children:
                    children.append(num)
            current_nodes = list(children)
    
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
