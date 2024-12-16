from fileinput import input
import sys, os, time

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
        boxes = self._boxes

        for y in range(0, len(mesh)):
            x = 0
            while x < len(mesh[y]):
                c = mesh[y][x]
                if player.x == x and player.y == y:
                    c = "@"
                elif self.box_at(x,y) != -1:
                    c = boxes[self.box_at(x,y)][2]
                mesh_str += c
                x+=1

            mesh_str += "\n"

        return  mesh_str + "\n" + str(player)


    def add(self, y: int, c: str):
        mesh = self._mesh

        if y + 1 > len(mesh):
            mesh.append([])
        
        if y >= len(mesh):
            raise Exception(y)
        row = mesh[y]
        x = len(row)
        
        if c == "@" and not self._player:
            self._player = Player(x, y)
            c = '.'

        if c in "O[]":
            self._boxes.append((x, y, c))
            c = '.'

        row.append(c)

        
    def next(self, x, y, dir) -> list:
        return [x + dir[0], y + dir[1]]


    def stone_at(self, x, y):
        return self._mesh[y][x] == '#'

    def box_at(self, x, y) -> int:
        boxes = self._boxes
        i = -1
        for idx, b in enumerate(boxes, 0): 
            if b[0] == x and b[1] == y:
                i = idx
                break
        return i


    def walk(self, direction: tuple):

        player = self._player   
        player.dir = direction
        dir = direction
        next_x = player.x + dir[0]
        next_y = player.y + dir[1]
      
        if self.stone_at(next_x, next_y):
            return
        
        box_moved = True
        if self.box_at(next_x, next_y) != -1:
            if self.box_moveable(next_x, next_y, dir):
                box_moved = self.move_box(next_x, next_y, dir)
            else:
                box_moved = False

        if box_moved:
            player.move(next_x, next_y)
        

    def box_moveable(self, box_x, box_y, dir) -> bool:
        return self.move_box(box_x, box_y, dir, None, True)
    
    def move_box(self, box_x, box_y, dir, source = None, peek = False) -> bool:
        curr = self.box_at(box_x, box_y)
        if curr == -1:
            return True
        boxes = self._boxes
        
        type = boxes[curr][2]

        next_x = box_x + dir[0]
        next_y = box_y + dir[1]

        if self.stone_at(next_x, next_y):
            return False
        
        moved = self.move_box(next_x, next_y, dir, None, peek)
        if moved and type != 'O' and  dir[1] != 0:
            sib = box_x + (1 if type == '[' else -1)
            if sib != source:
                moved = self.move_box(sib, box_y, dir, box_x, peek)
        
        if moved == True and peek != True:
            boxes[curr] = (next_x, next_y, boxes[curr][2])

        return moved


    def sum_stones(self) -> int:
        res = 0
        for b in self._boxes:
            if b[2] != ']':
                res += b[0] + 100 * b[1]

        return res


def parse_input(file_name = "", widen = False) -> list:

    if not file_name:
        file_name = './input.txt'

    mesh = Mesh()
    y = 0
    directions = []
    for line in input(files=(file_name)):
        line = line.strip()
        
        if len(line) > 0 and line[0] == '#': 
            for i in range(0, len(line)):
                c = line[i]
                if widen == False:
                    mesh.add(y, c)            
                else: 
                    if c == '#' or c == '.':
                        mesh.add(y, c)
                        mesh.add(y, c)
                    if c == '@':
                        mesh.add(y, '@')
                        mesh.add(y, '.')
                    if c == 'O':
                        mesh.add(y, '[')
                        mesh.add(y, ']')
                        
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
def part2_process(mesh: Mesh, directions: list) -> int:
    res = 0
    for d in directions:
        mesh.walk(d)
        animate(mesh)
    
    res = mesh.sum_stones()

    return res
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