from fileinput import input
import sys, os, time, re
# https://github.com/brean/python-pathfinding
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder



def parse_input(file_name = "") -> list:

    KB = []
    if not file_name:
        file_name = './input.txt'

    for line in input(files=(file_name)):
        line = line.strip()

        xy = re.split(r",", line)
        KB.append((int(xy[0]), int(xy[1])))
    
    return KB

def build_matrix(KB, size, limit):

    matrix = []
    for y in range(0, size[0]):
        matrix.append([])
        for x in range(0, size[1]):
            matrix[y].append(1)
    
    i = 0 
    for xy in KB:
        
        x = int(xy[0])
        y = int(xy[1])

        matrix[y][x] = 0
        
        if i == limit:
            break
        
        i += 1


    return matrix


'''
PART 1
'''
def part1_process(KB: list, size, limit) -> int:
  

    matrix = build_matrix(KB, size, limit)    



    grid = Grid(matrix=matrix)

    start = grid.node(0, 0)
    end = grid.node(len(matrix) - 1, len(matrix[0]) - 1)

    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    #print('operations:', runs, 'path length:', len(path))
    #print(grid.grid_str(path=path, start=start, end=end))

    return len(path) - 1



'''
PART 2
'''
def part2_process(KB: list, size, limit) -> int:

    matrix = build_matrix(KB, size, limit)
    
    grid = Grid(matrix=matrix)
    start = grid.node(0, 0)
    end = grid.node(len(matrix) - 1, len(matrix[0]) - 1)

    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    
    kb = 1
    while True:

        if kb >= len(KB):
            break
        xy = KB[kb]
        
        matrix[xy[1]][xy[0]] = 0

        grid = Grid(matrix=matrix)
        start = grid.node(0, 0)
        end = grid.node(len(matrix) - 1, len(matrix[0]) - 1)

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
        path, runs = finder.find_path(start, end, grid)
        if (len(path) == 0):
            return xy
        
        kb += 1

    return (-1,-1) 

'''
HELPER
'''

def to_str(matrix, path = []):
    mesh_str = ''
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[0])):
            c = str(matrix[y][x])
            if c == '0':
                c = '#'
            if c == '1':
                c = '.'
            if (x, y) in path:
                c = 'O'
            
            mesh_str += c
            pass
        mesh_str += "\n"

    return mesh_str
