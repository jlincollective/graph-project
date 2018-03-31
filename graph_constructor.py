from pprint import PrettyPrinter


class GraphConstructor:
    # initializes the graph given the number of vertices
    @staticmethod
    def initialize_graph(graph, num_vertices):
        for i in range(num_vertices):
            graph[i] = set()

    # constructs and returns a graph given the graph input file
    # assumes input file is well formed
    def construct_graph(self, file_path):
        graph = {}
        graph_file = open(file_path, "r")
        num_vertices = int(graph_file.readline())
        self.initialize_graph(graph, num_vertices)

        for edge in graph_file:
            vertex_a, vertex_b = (int(vertex) for vertex in edge.split())
            # usage of set takes care of possible duplicates
            graph[vertex_a].add(vertex_b)
            graph[vertex_b].add(vertex_a)

        return graph


def main():
    constructor = GraphConstructor()
    graph = constructor.construct_graph("graphs/n10.txt")
    pp = PrettyPrinter(indent=4)
    pp.pprint(graph)


if __name__ == "__main__":
    main()
