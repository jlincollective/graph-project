from graph_constructor import GraphConstructor


class ConnectedComponents:
    def __init__(self, file_path):
        self.constructor = GraphConstructor()
        self.graph = self.constructor.construct_graph(file_path, directed=False)

    # returns the number of connected components in the graph
    def num_connected_components(self):
        seen = set()
        num_components = 0
        for vertex in self.graph.keys():
            if vertex not in seen:
                self.bfs(vertex, seen)
                num_components += 1
        return num_components

    # breadth first search graph traversal
    def bfs(self, head, seen):
        queue = [head]
        while queue:
            vertex = queue.pop(0)
            for neighbor in self.graph[vertex]:
                if neighbor not in seen:
                    queue.append(neighbor)
            seen.add(vertex)


def main():
    cc = ConnectedComponents("graphs/n100.txt")
    num_components = cc.num_connected_components()
    output = "This graph has " + str(num_components) + " connected component"
    if num_components != 1:
        output += "s"

    print(output)


if __name__ == "__main__":
    main()
