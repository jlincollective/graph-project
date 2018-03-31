class GraphConstructor:
    # initializes the graph given the number of vertices
    @staticmethod
    def initialize_graph(graph, num_vertices):
        for i in range(num_vertices):
            graph[i] = set()

    # constructs and returns a graph given the graph input file
    # assumes input file is well formed
    def construct_graph(self, file_path, directed=False):
        graph = {}
        graph_file = open(file_path, "r")
        num_vertices = int(graph_file.readline())
        self.initialize_graph(graph, num_vertices)

        for edge in graph_file:
            vertex_a, vertex_b = (int(vertex) for vertex in edge.split())
            # usage of set takes care of possible duplicates
            if directed:
                graph[vertex_a].add(vertex_b)
            else:
                graph[vertex_a].add(vertex_b)
                graph[vertex_b].add(vertex_a)

        return graph
