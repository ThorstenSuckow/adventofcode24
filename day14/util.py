from fileinput import input
import re, sys, os, time
import copy

V = [
              (0, -1),
    (-1,  0),          (1,  0), 
               (0,  1),  
]


class Mesh: 

    mesh = None
    blueprint = None

    def __str__(self):
        mesh_str = ""

        mesh = self.mesh

        for y in range(0, len(mesh)):
            for x in range(0, len(mesh[y])):
                pos = self.mesh[y][x]
                mesh_str += " " if  pos == 0 else str(pos)
            mesh_str += "\n"

        return mesh_str


    def __init__(self, w: int, h: int):
        self.mesh = []

        mesh = self.mesh
        for y in range(0, h):
            mesh.append([])
            for x in range(0, w):
                mesh[y].append(0)

        self.blueprint = copy.deepcopy(self.mesh)

    def reset(self):
        self.mesh = copy.deepcopy(self.blueprint)

    def inc(self, x, y): 
        self.mesh[y][x] += 1

    def add(self, r: "Robot"):
        self.inc(r.position[0], r.position[1])


    def center_weighted(self, weight):
        mesh = self.mesh
        x_width = len(mesh[0])
       
        possible_match = False
        for y in range(0, len(mesh)):
            x = 0
            sim = 0
            for x in range(0, x_width - 1):
                if mesh[y][x] != 0 and mesh[y][x+1] != 0:
                    sim+=1
                if sim > weight:
                    possible_match = True
                    break
            
        return possible_match

            

class Robot:

    id = None
    position=None
    velocity=None
    mesh_w = None
    mesh_h = None


    def __init__(self, id, position, velocity):
        self.id = id
        self.position = position
        self.velocity = velocity
        self.start = position
        pass

    def __str__(self):
        return f"[{self.id}: {self.position}, {self.velocity}], w: {self.mesh_w}, h: {self.mesh_h}"
    
    def place_in(self, mesh: "Mesh"):
        self.mesh_h = len(mesh.mesh)
        self.mesh_w = len(mesh.mesh[0])

    def teleport(self, ticks: int):
        x = self.position[0]
        y = self.position[1]
        
        vx = self.velocity[0]
        vy = self.velocity[1]
        
        #for tick in range(1, ticks + 1):
            #print(x, y)
        x = (self.start[0] + ticks * vx) % (self.mesh_w)
        y = (self.start[1] + ticks * vy ) % (self.mesh_h)

        self.position = (x, y)
        
 
    def add_to_tile(self, tiles):

        x = self.position[0]
        y = self.position[1]
        mx = int(self.mesh_w / 2)
        my = int(self.mesh_h / 2)

        tile = -1
        if x < mx and y < my:
            tile = 0
        if x > mx and y < my:
            tile = 1
        if x < mx and y > my:
            tile = 2
        if x > mx and y > my:
            tile = 3

        if tile != -1:
            tiles[tile] += 1 


def parse_input(file_name = "") -> list:

    if not file_name:
        file_name = './input.txt'

    robots = []
    i = 0
    for line in input(files=(file_name)):
        line = line.strip()
        data = re.split(r"\s", line)
        position = re.split(r"\,", data[0])
        x = int(position[0][2:])
        y = int(position[1])
        
        velocity =  re.split(r"\,", data[1])
        v1 = int(velocity[0][2:])
        v2 = int(velocity[1])

        robots.append(Robot(i, (x, y), (v1, v2)))    


    return robots


'''
PART 1
'''
def part1_process(robots: list, mesh_w: int, mesh_h: int, teleport: int) -> int:

    res = 1
    tiles = [0, 0, 0 ,0]
    
    mesh = Mesh(mesh_w, mesh_h)
    for r in robots:
        r.place_in(mesh)
        r.teleport(teleport)
        r.add_to_tile(tiles)

    for i in tiles:
        res *= i

    return res
    


'''
PART 2
'''
def part2_process(robots: list, mesh_w: int, mesh_h: int, frame: int) -> int:
    
    
    mesh = Mesh(mesh_w, mesh_h)

    for r in robots:
        r.place_in(mesh)
    
    mesh.reset()
    for r in robots:
        r.teleport(frame)
        mesh.add(r)
    
    if mesh.center_weighted(12):
        os.system('CLS')
        sys.stdout.write(f"Frame: {frame}\n{mesh}")
        sys.stdout.flush()
    else:
        raise Exception("No similiarities found :(")  
    
    pass
    
'''
HELPER
'''
