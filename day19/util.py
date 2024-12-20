from fileinput import input
import sys, os, time, re
from functools import cmp_to_key
import itertools


def parse_input(file_name = "") -> list:

    patterns = []
    designs = []
   
    if not file_name:
        file_name = './input.txt'

    for line in input(files=(file_name)):
        line = line.strip()

        if (line == ""):
            continue
        
        if len(patterns) == 0:
            patterns = list(map(lambda k: k.strip(), re.split(r",", line)))
        else:
            designs.append(line)
            
    return [patterns, designs]


'''
PART 1
'''
def part1_process(patterns: list, designs: list) -> int:
    res = 0
    for design in designs:
        if is_valid(patterns, design) != 0:
            res += 1

    return res


'''
PART 2
'''
def part2_process(patterns: list, designs: list) -> int:

    res = 0
    for design in designs:
        res += is_valid(patterns, design)                    
    return res


'''
HELPER
'''
def is_valid(patterns:list , design: str, CACHE = {}) -> bool:
    
    res = 0

    if design == '':
        return 1

    if CACHE.get(design) is not None:
        return CACHE.get(design)

    for pattern in patterns:
        if design.endswith(pattern):
            t = is_valid(patterns, design[:-len(pattern)], CACHE)
            res += t
            if t != 0:
                cache(CACHE, design, t)  

    return res


def cache(CACHE, design, val):
    if CACHE.get(design) is None:
        CACHE[design] = 0

    CACHE[design] += val 