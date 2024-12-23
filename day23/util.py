from fileinput import input
from operator import xor
import re

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


    end = []
    for key in comps:
        for l in comps[key]:
            if l == key:
                continue
            if key in comps[l]:
                if (key, l) not in end and (l, key) not in end:
                    end.append((key, l))

    connections = []
    for tpl in end:
        for mid in comps[tpl[0]]:
            if tpl[1] in comps[mid]:
                m = [tpl[0], mid, tpl[1]] 
                m.sort()
                if m not in connections:
                    connections.append(m)    
        
    proc = []
    for conn in connections:
        for e in conn:
            if conn not in proc and e.startswith("t"):
                proc.append(conn)
                res+=1


    return res

'''
PART 2
'''
def part2_process(secrets: list) -> int:

    return 0
'''
Helper
'''


def connect(key, lst):
    if key in lst:
        return True

    return False