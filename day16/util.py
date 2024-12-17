from fileinput import input
import sys, os, time

V = [
              (0, -1),
    (-1,  0),          (1,  0), 
               (0,  1),  
]

class Edge:
    u = None
    v = None 
    weight = None

    def __str__(self):
        
        return f"{self.u}, {self.v}, {self.weight}"
    

    def __init__(self, u, v, weight = 0):
        
        if weight == 0:
            self.weight = max(abs(u[0] - v[0]), abs(u[1] - v[1]))
        else:
            self.weight = weight

        l = sorted([u, v])
        self.u = l[0]
        self.v = l[1]    


    def equals(self, edge = "Edge"):
        return (self == edge or (edge.u == self.u and edge.v == self.v) or
                (edge.v == self.u and edge.u == self.v) )

    def connects(self, edge):
        return edge.u == self.u or edge.u == self.v or edge.v == self.u or edge.v == self.v
        

class Mesh:
    _nodes = None
    _edges = None
    _raw = None

    def __str__(self):

        raw = self._raw
        nodes = self._nodes
        
        mesh_str = ''
        for y in range(0, len(raw)):
            
            for x in range(0, len(raw[y])):
                xy = (x, y)
                c = raw[y][x]
                if xy in nodes:
                    c = 'o'
                if xy == self._start:
                    c = c#'s'
                if xy == self._end:
                    c = c#'e'

                mesh_str += c
            mesh_str += '\n' 

        return f"{mesh_str}\nS: {self._start}, E: {self._end}"

    def __init__(self, start: tuple, end: tuple, raw: list):
        self._raw = raw
        self._start = start
        self._end = end
        self._edges = []
        self._paths = []

    def node_match(self, x, y):
        raw = self._raw
        
        if ((raw[y][x-1] == '.' or raw[y][x+1] == ".")
            and 
            (raw[y - 1][x] == '.' or raw[y + 1][x] == ".")):
            return True

        return False

    def init_nodes(self):
        raw = self._raw

        nodes = [self._start, self._end]
        y = 0
        for y in range(0, len(raw)):
            row = raw[y]
            for x in range(0, len(row)):
                c = row[x]
                if c == '.' and self.node_match(x, y):
                    if (x, y) not in nodes:
                        nodes.append((x, y))

        self._nodes = nodes
        pass

    mn = 0

    def edge_exists(self, edge: Edge):
        edges = self._edges

        for e in edges:
            if (e.equals(edge)):
                return True
        
        return False

    def init_edges(self):
        nodes = self._nodes
        edges = self._edges
        raw = self._raw

        for node in nodes:
            
            for v in V:
                [x, y] = node
                x += v[0]
                y += v[1]
                while True:
                    c = raw[y][x]
                    if c == '#': 
                        break
                    if (x, y) in nodes:
                        new_edge = Edge(node, (x, y))
                        if self.edge_exists(new_edge) == False:
                            edges.append(new_edge)
                        
                    x += v[0]
                    y += v[1]


def parse_input(file_name = "") -> list:

    if not file_name:
        file_name = './input.txt'

    y = 0
    raw = []
    start = None
    end = None
    for line in input(files=(file_name)):
        line = line.strip()
        raw.append([])
        for i in range(0, len(line)):
            c = line[i]
            
            match c:
                case 'S':
                    c = '.'
                    start = (len(raw[y]), y)
                case 'E':
                    c = '.'
                    end = (len(raw[y]), y)
             
            raw[y].append(c)
        y += 1

    mesh = Mesh(start, end, raw)
    
    return mesh


'''
PART 1
'''
def part1_process(mesh: Mesh) -> int:
  
    mesh.init_nodes()
    mesh.init_edges()
    edges = mesh._edges
    nodes = mesh._nodes
    
    g = Graph(len(nodes), mesh._start, mesh._end)
    n = 0
    for node in nodes:
        g.add_vertex_data(n, node)
        n+= 1
    
    for edge in edges:
        l = edge.u
        r = edge.v
        lid = g.vertex_data.index(l)
        rid = g.vertex_data.index(r)
        g.add_edge(lid, rid, edge.weight)

    start = mesh._start
    distances = g.dijkstra(start)
    for i, d in enumerate(distances):
        if g.vertex_data[i] == mesh._end:
            return d


'''
PART 2
'''
def part2_process(mesh: Mesh) -> int:
    pass


'''
HELPER
'''
# source: https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php
class Graph:
    def __init__(self, size, start, end):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.start = start
        self. end = end
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size
        paths = []

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i] 
                    u = i

            if u is None:
                break
            visited[u] = True

            
            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    add = 0
                    
                    # consider turns
                    node = self.vertex_data[u]
                    if node == start_vertex_data and self.vertex_data[v][1] == node[1]:
                        add = 0
                    elif ((self.vertex_data[u][0] != self.vertex_data[v][0]) 
                        or (self.vertex_data[u][1] != self.vertex_data[v][1])):
                        add = 1000
                    
                    alt = distances[u] + self.adj_matrix[u][v] + add
                    if alt < distances[v]:
                        distances[v] = alt
                        paths.append(self.vertex_data[v])

        return distances