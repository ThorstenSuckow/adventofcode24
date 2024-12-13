from fileinput import input
import re

node_map = {} 

def count_blinks(value, blinks):

    key = (value, blinks)

    if node_map.get(key):
        return node_map.get(key)

    if blinks == -1:
        return 0
    
    vs = blink(value)
    
    res = len(vs) - 1
    
    for val in vs:    
        res += count_blinks(val, blinks - 1)
    
    node_map[key] = res
    return res


def blink(value) -> int:    

    vlen = len(str(value))
    hlf = int(vlen / 2)

    if value == 0:
        return [1]
    elif vlen % 2 == 0:
        return [int(str(value)[:hlf]), int(str(value)[hlf:])]
    else:
        return [value * 2024]
    
def parse_input(file_name = "") -> list:

    if not file_name:
        file_name = './input.txt'

    data = []
    for line in input(files=(file_name)):
        line = line.strip()
        data = list(map(int, re.split(r"\s", line)))

    return data

'''
PART 1
'''
def part1_process(data: list, blink_n: int) -> int:

    res = len(data)
    for d in data:
        res +=  count_blinks(d, blink_n -1)

    return res


'''
PART 2
'''
def part2_process(data: list) -> int:
    return part1_process(data, 75)
    
    
'''
HELPER
'''
