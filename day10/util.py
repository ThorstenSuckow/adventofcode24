from fileinput import input


V = [
              (0, -1),
    (-1,  0),          (1,  0), 
               (0,  1),  
]


class Mesh:
    _data = None

    _zs = None

    def __init__(self):
        self._data = []
        self._zs = {}  

    def add_zero(self, x, y):
        if self._zs.get((x, y)):
            raise Exception("whoops")
        
        self._zs[(x, y)] = {
            'x': x,
            'y': y,
            'heads': [],
            'rating' : 0
        }
        

    def add(self, c, y):
        data = self._data
        c = int(c) if c != '.' else 1
        if y >= len(data):
            data.append([])
            
        row = data[y]
        row.append(c)

        if c == 0:
            self.add_zero(len(row) - 1, y)

    def next(self, x, y, dir) -> list:
        return [x + dir[0], y + dir[1]]


    def walk(self):

        zs = self._zs

        trailheads = 0
        rating = 0

        for xy in zs:
            zero = zs[xy]
            x = xy[0]
            y = xy[1]
            self.find_path(0, *self.next(x, y, V[0]), V[0], zero)
            self.find_path(0, *self.next(x, y, V[1]), V[1], zero)
            self.find_path(0, *self.next(x, y, V[2]), V[2], zero)
            self.find_path(0, *self.next(x, y, V[3]), V[3], zero)
            trailheads += len(zero['heads'])
            rating += zero['rating']

        return [trailheads, rating]

    def find_path(self, prev, x,y, dir, zero): 

        if self.in_bounds(x, y) is False:
            return False

        v = self.at(x, y)

        if v == 9 and prev ==  8:
            zero['rating'] += 1
            if (x, y) not in zero['heads']:
                zero['heads'].append((x, y))
            return True

        if v - prev != 1:
            return False 
        
        oppos = self.oppos(dir)

      
        for i in oppos:
            self.find_path(v, *self.next(x, y, i), i, zero)

    def oppos(self, dir):
        match dir:
            case (1, 0):
                return [V[2], V[0], V[3]]
            
            case (-1, 0):
                return [V[1], V[0], V[3]]
            
            case (0, 1):
                return [V[3], V[2], V[1]]
            
            case (0, -1):
                return [V[0], V[2], V[1]]

    def at(self, x, y) -> int:
        if self.in_bounds(x, y) is False:
            raise Exception("out of bounds")
        return self._data[y][x]

    def in_bounds(self, x, y) -> bool:
        return x >= 0 and y >= 0 and x < len(self._data[0]) and y < len(self._data) 


def parse_input(file_name = "") -> list:

    if not file_name:
        file_name = './input.txt'

    mesh = Mesh()
    x = 0
    y = 0
    for line in input(files=(file_name)):
        
        line = line.strip()
        x = 0
        for i in range(0, len(line)):
            mesh.add(line[i], y)            
            x+=1

        y+=1

    return mesh


'''
PART 1
'''
def part1_process(mesh: Mesh) -> int:
    return mesh.walk()[0]
    

'''
PART 2
'''
def part2_process(mesh: Mesh) -> int:
    return mesh.walk()[1]
    
    
'''
HELPER
'''
