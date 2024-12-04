from fileinput import input
import re


DIRS = ['o0', 'o2', 'o3', 'o4', 'o6', 'o8', 'o9', 'o10']
MAS_DIRS = ['o2', 'o4', 'o8', 'o10']


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
        [u, v] = calc(x, y, dir)
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
        case 'o2':
            if char_at(x-1, y+1, rows) == 'M' and char_at(x+1, y-1, rows) == 'S':
                res = 3 
        case 'o4':
            if char_at(x-1, y-1, rows) == 'M' and char_at(x+1, y+1, rows) == 'S':
                res = 3 
        case 'o8':
            if char_at(x+1, y-1, rows) == 'M' and char_at(x-1, y+1, rows) == 'S':
                res = 3 
        case 'o10':
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


def calc(x, y, dir) -> list:

    match dir:
        case 'o0':
            return [0, -1]        
        case 'o2':
            return [+1, -1]        
        case 'o3':
            return [+1, 0]        
        case 'o4':
            return [+1, +1]        
        case 'o6':
            return [0, +1]        
        case 'o8':
            return [-1, +1]        
        case 'o9':
            return [-1, 0]        
        case 'o10':
            return [-1, -1]        

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