from fileinput import input
import re


V = [
              (0, -1),
    (-1,  0),          (1,  0), 
               (0,  1),  
]


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
        pass

    def __str__(self):
        return f"[{self.id}: {self.position}, {self.velocity}], w: {self.mesh_w}, h: {self.mesh_h}"
    
    def place_in(self, w : int, h: int):
        self.mesh_h = h
        self.mesh_w = w

    def teleport(self, ticks: int):
        x = self.position[0]
        y = self.position[1]
        
        vx = self.velocity[0]
        vy = self.velocity[1]
        
        for tick in range(1, ticks + 1):
            #print(x, y)
            x = (x + vx) % (self.mesh_w)
            y = (y + vy ) % (self.mesh_h)

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
    for r in robots:
        r.place_in(mesh_w, mesh_h)
        r.teleport(teleport)
        r.add_to_tile(tiles)
        
    for i in tiles:
        res *= i

    return res
    pass
    


'''
PART 2
'''
def part2_process(robots: list) -> int:
    
    pass
    
'''
HELPER
'''
