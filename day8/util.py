from fileinput import input
import re

class Mesh:
    _data = None
    _max_x = 0
    _max_y = 0
    _rays = {}


    def antinodes(self, bounce = False):
        antennas = self._data

        antinodes = []
    
        for a in antennas:
            grp = antennas[a]
            node_a = None
            node_b = None

            for i in range(0, len(grp)):
                node_a = grp[i]
                for j in range(i + 1, len(grp)):
                    node_b = grp[j]
                    
                    v = (node_b[0] - node_a[0], node_b[1] - node_a[1])
                    
                    anode_b = (node_b[0] + v[0], node_b[1] + v[1])
                    anode_a = (node_a[0] - v[0], node_a[1] - v[1])
                    
                    if self.in_bounds(anode_b) and anode_b not in antinodes:
                        antinodes.append(anode_b)
                    if self.in_bounds(anode_a) and anode_a not in antinodes:
                        antinodes.append(anode_a)

                    if bounce is True:

                        # add antennas to list of antinodes
                        # for part two
                        if (node_a not in antinodes):
                            antinodes.append(node_a)
                        if (node_b not in antinodes):
                            antinodes.append(node_b)
                            
                        # bounce points as long as in bounds
                        while (self.in_bounds(anode_b)):
                            if (anode_b not in antinodes):
                                antinodes.append(anode_b)
                            anode_b = (anode_b[0] + v[0], anode_b[1] + v[1])   
                            
                        while (self.in_bounds(anode_a)):
                            if (anode_a not in antinodes):
                                antinodes.append(anode_a)
                            anode_a = (anode_a[0] - v[0], anode_a[1] - v[1])   
                            
        return antinodes
        

    def in_bounds(self, node: tuple) -> bool:

        return (node[0] >= 0 and 
                node[0] <= self._max_x and 
                node[1] >= 0 and 
                node[1] <= self._max_y)
    
    

def parse_input(file_name = "") -> Mesh:

    mesh = Mesh()

    if not file_name:
        file_name = './input.txt'

    res = {}
    x = 0
    y = 0
    max_x = 0
    for line in input(files=(file_name)):
        line = line.strip()
        max_x = max(max_x, len(line) - 1)
        
        x = 0
        for c in line:
            if c != ".":
                if res.get(c) is None:
                    res[c] = []
                res[c].append((x, y))

            x += 1
        y += 1

    mesh._max_x = max_x
    mesh._max_y = y - 1
    mesh._data = res     

    return mesh


'''
PART 1
'''
def part1_process(mesh: Mesh) -> int:
        
    antonides = mesh.antinodes()
    return len(antonides)


    pass

'''
PART 2
'''
def part2_process(mesh: Mesh) -> int:
    
    antonides = mesh.antinodes(True)
    return len(antonides)

    pass

    
'''
HELPER
'''
