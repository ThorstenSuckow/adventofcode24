from fileinput import input
from operator import xor
import re
import time
import copy
def parse_input(file_name = "") -> map:

    if not file_name:
        file_name = './input.txt'

    comps = {}
    for line in input(files=(file_name)):
        line = line.strip()

        pairs = re.split(r"\-", line)

        lft = pairs[0]
        rgt = pairs[1]
        if comps.get(lft):
            comps[lft].append(rgt)
        else: 
            comps[lft] = [rgt]

        if comps.get(rgt):
            comps[rgt].append(lft)
        else: 
            comps[rgt] = [lft]
        

    return comps

'''
PART 1
'''
def part1_process(comps: map) -> int:
    res = 0

    matrix = adjacency(comps)

    found = []
    for row in matrix:
        for col in matrix:
            if matrix[row][col] == 1:
                for key in matrix[col]:
                    if matrix[col][key] == 1 and matrix[key][row] == 1:
                        triplet = [row, col, key]
                        triplet.sort()
                        if triplet not in found:
                            found.append(triplet)
    
    for triplet in found:
        val = list(filter(lambda key:  key.startswith("t"), triplet))
        if len(val) != 0:
            res += 1

    return res
 

'''
PART 2
'''
def part2_process(comps: map) -> int:

    res = ''
    max_result = set()
    for key in comps:
        result = connects(comps, set([key]))
        if len(result) > len(max_result):
            max_result = result
        
    res = ','.join(sorted(list(max_result)))

    return res


def connects(comps, base_set: set):

    res = set()
    for key in comps:
        nodes = set(comps[key])
        if len(base_set) > len(res) and base_set.issubset(nodes):
            
            base_set.add(key)
            tmp = connects(comps, base_set)
            
            if len(base_set) > len(tmp):
                res = base_set
            else: 
                res = tmp
    return res


'''
Helper
'''
def adjacency(comps):
    
    matrix = {}
    keys = []
    for key in comps:
        keys.append(key)
    keys.sort()

    for key in keys:
        matrix[key] = {}
        for lkey in keys:
            matrix[key][lkey] = 0
        
    for key in keys:
        for conn in keys:
            if conn in comps[key]:
                matrix[key][conn] = 1
                
    return matrix
