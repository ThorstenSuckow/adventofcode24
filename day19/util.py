from fileinput import input
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

def is_valid(patterns:list , design: str, validated : str) -> bool:


    if (design in patterns):
        return True
    
    for pattern in patterns:
        if design.endswith(pattern):
            sub = design[:-len(pattern)]
            validated = pattern + validated 

            if is_valid(patterns, sub, validated):
                return True
    
    
    return False

def test_pattern(pattern, design):

    pass