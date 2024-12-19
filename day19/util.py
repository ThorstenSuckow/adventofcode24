from fileinput import input
from functools import cmp_to_key
import sys, os, time, re



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
  
    test = designs[0]

    patterns = sorted(patterns, key = cmp_to_key(lambda a, b: len(b) - len(a)))


    res = 0
    for design in designs:
        if is_valid(patterns, design, ''):
            res += 1
    
    return res



'''
PART 2
'''
def part2_process(patterns: list, designs: list) -> int:

    return 0



'''
HELPER
'''

CACHE = []

def is_valid(patterns:list , design: str, validated : str) -> bool:
    global CACHE

    if (design in patterns):
        return True
    
    for pattern in patterns:
        if design.endswith(pattern):
            sub = design[:-len(pattern)]
            validated = pattern + validated 

            if sub == '': return True 
            if is_valid(patterns, sub, validated):
                return True
    
    
    return False

def test_pattern(pattern, design):

    pass