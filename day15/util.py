from fileinput import input
import re, sys, os, time

V = [
              (0, -1),
    (-1,  0),          (1,  0), 
               (0,  1),  
]

SLEEP = None


class Player:
    x = 0
    y = 0
    dir = None

    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __str__(self):
        return str(self.dir)

    def move(self, x, y):
        self.x = x
        self.y = y


class Mesh:
    _mesh = None

    _player = None
    _boxes = None

    def __init__(self):
        self._mesh = []
        self._boxes = []

    def __str__(self):
        mesh_str = ""
        mesh = self._mesh
        player = self._player

        for y in range(0, len(mesh)):
            for x in range(0, len(mesh[y])):
                c = mesh[y][x]
                pos = (x, y)
                if player.x == x and player.y == y:
                    c = "@"
                elif pos in self._boxes:
                    c = "O"
                mesh_str += c

            mesh_str += "\n"

        return  mesh_str + "\n" + str(player)

    def add(self, x: int, y: int, c: str):
        mesh = self._mesh

        if y + 1 > len(mesh):
            mesh.append([])
        
        if y >= len(mesh):
            raise Exception(y)
        row = mesh[y]

        if c == "@" and not self._player:
            self._player = Player(x, y)
            c = '.'

        if c == "O":
            ppos = (x, y)
            self._boxes.append(ppos)
            c = '.'


        row.append(c)

        
    def next(self, x, y, dir) -> list:
        return [x + dir[0], y + dir[1]]

    def stone_at(self, x, y):
        return self._mesh[y][x] == '#'

    def box_at(self, x, y):
        return (x, y) in self._boxes

    def walk(self, direction: tuple):

        player = self._player

           
        player.dir = direction
        dir = direction
        next_x = player.x + dir[0]
        next_y = player.y + dir[1]
      
        if self.stone_at(next_x, next_y):
            return
        
        box_moved = True
        if self.box_at(next_x, next_y):
            box_moved = self.move_box(next_x, next_y, dir)
        
        if box_moved:
            player.move(next_x, next_y)
        

    def move_box(self, x, y, dir) -> bool:

        moved = True   
        boxes = self._boxes

        if self.stone_at(x + dir[0], y + dir[1]):
            return False
        if self.box_at(x + dir[0], y + dir[1]):    
            moved = self.move_box(x + dir[0], y + dir[1], dir)
        if moved == True:
           idx = boxes.index((x, y))
           boxes[idx] = (x + dir[0], y + dir[1]) 
        return moved

    def sum_stones(self) -> int:
        res = 0

        for b in self._boxes:
            res += b[0] + 100 * b[1]

        return res


def parse_input(file_name = "") -> list:

    if not file_name:
        file_name = './input.txt'

    mesh = Mesh()
    x = 0
    y = 0
    directions = []
    for line in input(files=(file_name)):
        line = line.strip()
        
        x = 0
        if len(line) > 0 and line[0] == '#': 
            for i in range(0, len(line)):
                mesh.add(x, y, line[i])            
                x += 1
        else:
            for i in range(0, len(line)):
                directions.append(c_to_v(line[i]))
        y += 1

    return [mesh, directions]


'''
PART 1
'''
def part1_process(mesh: Mesh, directions: list) -> int:
  
    res = 0
    for d in directions:
        mesh.walk(d)
        animate(mesh)
    
    res = mesh.sum_stones()

    return res

'''
PART 2
'''
def part2_process(mesh: Mesh) -> int:
    pass
    
'''
HELPER
'''

def c_to_v(c: str) -> tuple:

    match (c):

        case '^':
            return V[0]
        case '<':
            return V[1]
        case '>':
            return V[2]
        case 'v':
            return V[3]
            

def animate(mesh: Mesh):
    if SLEEP is None:
        return
    os.system('CLS')
    sys.stdout.write(f"{mesh}")
    sys.stdout.flush()
    time.sleep(SLEEP)