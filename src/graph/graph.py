import json

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node_origin, nodes: set):
        if type(nodes) is not set:
            raise TypeError('nodes must be a set type')
        
        if node_origin in self.graph:
            for node in nodes:
                self.graph[node_origin].append(node)
        else:
            self.graph[node_origin] = list(nodes)

    def __repr__(self) -> str:
        return json.dumps(self.graph, indent=4, sort_keys=True)