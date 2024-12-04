from fileinput import input
import re

V = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0), 
    (-1,  1), (0,  1), (1,  1) 
]

DIRS = ['t', 'tr', 'r', 'br', 'b', 'bl', 'l', 'tl']
MAS_DIRS = ['tr', 'br', 'bl', 'tl']


def parse_input(file_name = "") -> list:

    list = []

    if not file_name:
        file_name = './input.txt'


    for line in input(files=(file_name)):
        list.append(line.strip())

    return list

'''
PART 1
'''
def part1_process(rows: list) -> int:

    global DIRS

    xs = collect_pivots('X', rows)
    xs = sum_xmas(xs, rows)
    sum = 0
    for i in range(0, len(xs)):
        for j in range(0, len(DIRS)):
            sum += int(xs[i][DIRS[j]] / 4)

    return sum

def sum_xmas(xs: list, rows: list) -> list:
    global DIRS
    i = 0
    xcount = len(xs)
    while i < xcount:
        for dc in range(0, len(DIRS)):
            dir = DIRS[dc]
            xs[i][dir] = walk(xs[i]['x'], xs[i]['y'], rows, dir)
        i+=1
    return xs

def walk(x: int, y: int, rows: list, dir: str):

    # right
    XMAS = 'XMAS'
    ch = rows[y][x]
    res = 0
    nxt = ''
    while XMAS.startswith(ch) and len(ch) < 4 and nxt is not None:
        [u, v] = accelerate(dir)
        x += u
        y += v
        nxt =  char_at(x, y, rows)   
        ch += nxt if nxt is not None else ''
        
    if (len(ch) > 4):
        raise Exception(f"ch {ch} ")

    return 0 if ch != XMAS else 4


'''
PART 2
'''
def part2_process(rows: list) -> int:
    global MAS_DIRS

    masses = collect_pivots('A', rows)
    masses = sum_masses(masses, rows)
    sum = 0

    for i in range(0, len(masses)):
        res = 0
        for j in range(0, len(MAS_DIRS)):
            res += int(masses[i][MAS_DIRS[j]])

        if (res == 6):
            sum += 1
    return sum

def sum_masses(masses: list, rows: list) -> list:
    global MAS_DIRS
    i = 0
    mascount = len(masses)
    while i < mascount:
        for dc in range(0, len(MAS_DIRS)):
            dir = MAS_DIRS[dc]
            masses[i][dir] = walk_mas(masses[i]['x'], masses[i]['y'], rows, dir)
        i+=1
    return masses
    
def walk_mas(x: int, y: int, rows: list, dir: str):

    res = 0
    match dir:
        case 'tr':
            if char_at(x-1, y+1, rows) == 'M' and char_at(x+1, y-1, rows) == 'S':
                res = 3 
        case 'br':
            if char_at(x-1, y-1, rows) == 'M' and char_at(x+1, y+1, rows) == 'S':
                res = 3 
        case 'bl':
            if char_at(x+1, y-1, rows) == 'M' and char_at(x-1, y+1, rows) == 'S':
                res = 3 
        case 'tl':
            if char_at(x+1, y+1, rows) == 'M' and char_at(x-1, y-1, rows) == 'S':
                res = 3 

    return res

'''
Helper
'''

def collect_pivots(ch: str, rows: list) -> list:

    j = 0
    rowlen = len(rows)
    linelen = len(rows[0])
    xs = []
    while j < rowlen:
        
        i = 0
        line = rows[j]
        while i < linelen: 
            if line[i] == ch:
                xs.append({'x': i, 'y': j})
            i+=1
        j+=1 

    return xs



def accelerate(dir) -> list:
    global V
    match dir:
        case 't':
            return V[1]        
        case 'tr':
            return V[2]        
        case 'r':
            return V[4]        
        case 'br':
            return V[7]        
        case 'b':
            return V[6]        
        case 'bl':
            return V[5]        
        case 'l':
            return V[3]        
        case 'tl':
            return V[0]        

    raise Exception(f"dir {dir} not defined")    


def char_at(x, y, rows) -> str:
    if x < 0:
        return None
    
    if x >= len(rows[0]):
        return None
    
    if y < 0:
        return None
    
    if y >= len(rows):
        return None
    
    return rows[y][x]