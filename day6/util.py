from fileinput import input
import re

MAX_X = 0
MAX_Y = 0
# collects values for f(x). f(1) = 2 is (1, 2) as a point 
# in a 2-dim cart. coord. system. X[0] = [1, 2, 3]
# means that for x=0, three y-values 1, 2, 3 are computed
X = []
#  the same , for f(y)
Y = []

V = [
              (0, -1),
    (-1,  0),          (1,  0), 
               (0,  1),  
]


def parse_input(file_name = "") -> list:
    global MAX_Y, MAX_X, X, Y

    if not file_name:
        file_name = './input.txt'

    guard_pos = []
    dir = []
    
    MAX_Y = 0
    for line in input(files=(file_name)):
        
        row = line.strip()
        regex = r"(#)|(\^)|(\>)|(v)|(\<)"
        matches = re.finditer(regex, row, re.IGNORECASE)
        
        if MAX_X == 0:
            MAX_X = len(row) - 1
            for i in range(0, MAX_X + 1):
                X.append([])

        
        Y.append([])

        for _, match in enumerate(matches, start=1):
            
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                group = match.group(groupNum)
                if group is None: 
                    continue

                match groupNum:
                    case 1: 
                        x = match.start(groupNum)
                        Y[MAX_Y].append(x)
                        Y[MAX_Y].sort()
                        X[x].append(MAX_Y)
                        X[x].sort()

                    case _: 
                        dir = dir_match(group)
                        guard_pos = [match.start(groupNum), MAX_Y] 
                                
        MAX_Y += 1

    MAX_Y -=1    

    return [guard_pos, dir]


'''
PART 1
'''
def part1_process(guard: list) -> int:
    global X, Y
    [lines, _] = walk(guard, X, Y)
    
    sum = 0
    intersections = 0
    for idx, line in enumerate(lines, 0):
        start = line[0]
        end = line[1]
        sum += abs(start[0] - end[0])
        sum += abs(start[1] - end[1])
        
        match = []
        if (start[1] == end[1]):
            match = intersect(start, end, lines[:idx], 'x')
        elif (start[0] == end[0]):
            match = intersect(start, end, lines[:idx], 'y')
       
        intersections += len(match)
        
    return sum - intersections       



'''
PART 2
'''
def part2_process(guard: list) -> int:


    [lines, _] = walk(guard, X, Y)
    obis = []
    reaches = []
    for idx, line in enumerate(lines, 0):
        
        dir = line[2] 
        reaches = lines[:idx + 1]
        
        [x1, y1, x2, y2] = [line[0][0], line[0][1], line[1][0], line[1][1]] 

        if dir is V[0] or dir is V[3]:
            start = max(y1, y2) - 1 if dir is V[0] else min(y1, y2) + 1
            weight = -1 if dir is V[0] else 1 
            while (True):
                if dir is V[0] and start < 0:
                    break    
                elif dir is V[3] and start > MAX_Y:
                    break

                new_ob = start 
                
                if new_ob in X[x1]:
                    break
                start += 1 * weight
                    
                [Xt, Yt] = place_obstacle(x1, new_ob, X, Y)
                [new_walk, has_cycle] = walk(guard, Xt, Yt, True)  
                
                if has_cycle and sub_path(reaches, new_walk):
                    obis.append((x1, new_ob))
                
        elif dir is V[2] or dir is V[1]:
            
            start = min(x1, x2) + 1 if dir is V[2] else max(x1, x2) - 1
            weight = -1 if dir is V[1] else 1 
            
            while (True):

                if dir is V[1] and start < 0:
                    break    
                elif dir is V[2] and start > MAX_X:
                    break

                new_ob = start 

                if new_ob in Y[y1]:
                    break
               
                start += 1 * weight

                [Xt, Yt] = place_obstacle(new_ob, y1, X, Y)
                [new_walk, has_cycle] = walk(guard, Xt, Yt, True)  
                if has_cycle and sub_path(reaches, new_walk):
                    obis.append((new_ob, y1))
                    
                
    return len(obis)    

    
'''
HELPER
'''

def place_obstacle(x: int, y: int, X: list, Y: list) -> list:

    Xt = X[:]
    Yt = Y[:]

    if y not in Xt[x]:
        Xt[x] = X[x].copy()
        Xt[x].append(y)
        Xt[x].sort()
    
    if x not in Yt[y]:
        Yt[y] = Y[y].copy()
        Yt[y].append(x)
        Yt[y].sort()
     
    return [Xt, Yt]


def sub_path(reaches, path) -> bool:

    for i in range(0, len(reaches) - 1):
        if same(reaches[i], path[i]) is False:
            return False    
    return True


def same(line1, line2) -> bool:
    if line1 == line2:
        return True
    
    return False


def intersect(start, end, lines, axis) -> list:

    [x_1, y_1, x_2, y_2] = [start[0], start[1], end[0], end[1]]
    	
    assert(y_1 == y_2 if axis == 'x' else x_1 == x_2)
    
    match = []
    for line in lines:
        
        [u_1, u_2, v_1, v_2] = [line[0][0], line[1][0], line[0][1], line[1][1]]

        if axis == 'x':
            if min(x_1, x_2) < u_1 and max(x_1, x_2) > u_1:
                if min(v_1, v_2) < y_1 and max(v_1, v_2) > y_1:
                    match.append([line])

        elif axis == 'y':
            if min(y_1, y_2) < v_1 and max(y_1, y_2) > v_1:
                if min(u_1, u_2) < x_1 and max(u_1, u_2) > x_1:
                    match.append([line])

    return match
            

def dir_match(dir: str) -> list:
    global V

    match (dir):
        case 'v':
            return V[3]
        case '^':
            return V[0]
        case '<':
            return V[1]
        case '>':
            return V[2]
        
    raise Exception(f"dir {dir} is unknown")    

    

def next_dir(dir: tuple) -> tuple:
    pos = V.index(dir)
    
    match pos:
        case 0:
            pos = 2
        case 1:
            pos = 0
        case 2:
            pos = 3
        case 3:
            pos = 1 
    
    return V[pos]


def walk(guard: list, X: list, Y:list, cycle_break = False) -> list|bool:
    [pos, dir] = guard

    x = pos[0]
    y = pos[1]
    has_cycle = False
    passed = False
    
    single_line = [(x, y)]
    lines = []
    c = 0
    while (passed is False):
            
        if (has_cycle):
            break
       
        dir_x = dir[0]
        dir_y = dir[1]

        prev_x = x
        prev_y = y
        
        match dir_x:
        
            # right
            case 1:            
                
                if len(Y[y]) == 0 or Y[y][-1] < x:
                    x = MAX_X     
                    passed = True
                else:
                    for o in Y[y]:
                        if x < o:
                            x = o - 1
                            break

            # left            
            case -1:
                if len(Y[y]) == 0 or Y[y][0] > x:
                    passed = True
                    # make sure exited tile is considered
                    x = -1     
                else:
                    for o in list(reversed(Y[y])):
                        if x > o:
                            x = o + 1
                            break
                        
        match dir_y:

            # up
            case 1:
                if len(X[x]) == 0 or X[x][-1] < y:
                    passed = True
                    y = MAX_Y     
                else:
                    for o in X[x]:
                        if y < o:
                            y = o - 1
                            break
            
            # down
            case -1:
                if len(X[x]) == 0 or X[x][0] > y:
                    passed = True
                    # make sure exited tile is considered
                    y = -1     
                else:
                    for o in list(reversed(X[x])):
                        if y > o:
                            y = o + 1
                            break
                    
        prev_dir = dir
        dir = next_dir(dir)
        if (prev_x == x and prev_y == y):
            continue         
        
        single_line.append((x, y))
        single_line.append(prev_dir)    

        if cycle_break == True and single_line in lines:
            has_cycle = True
            
        lines.append(single_line)
        single_line = [(x, y)]
    pass 


    return [lines, has_cycle]