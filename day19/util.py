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
    CACHE = {}
    for design in designs:
        if is_valid(patterns, design, CACHE) != 0:
            res += 1

    return res


'''
PART 2
'''
def part2_process(patterns: list, designs: list) -> int:

    res = 0
    CACHE = {}
    for design in designs:
        res += is_valid(patterns, design, CACHE)                    
    return res


'''
HELPER
'''
def is_valid(patterns:list , design: str, memo: map) -> bool:
    
    res = 0

    if memo.get(design) is not None:
        return memo.get(design)

    if design == '':
        return 0

    t = 0
    for pattern in patterns:
        
        if design.endswith(pattern):
            t = ((1 if pattern == design else 0) + 
                is_valid(patterns, design[:-len(pattern)], memo))
            res += t
            
    if t != 0:
        memoize(memo, design, res)      

    return res


def memoize(memo, design, val):
    if memo.get(design) is None:
        memo[design] = 0

    memo[design] = val 