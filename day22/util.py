from fileinput import input
from operator import xor

def parse_input(file_name = "") -> list:

    if not file_name:
        file_name = './input.txt'

    secrets = []
    for line in input(files=(file_name)):
        line = line.strip()

        secrets.append(int(line))
        
    return secrets

'''
PART 1
'''

def part1_process(secrets: list) -> int:
    res = 0

    for secret in secrets:
        res += calc_secret(secret, 2000)
        
    return res

'''
PART 2
'''
def part2_process(cmds: list) -> int:
    res = 0
                       
    return res

'''
Helper
'''


def calc_secret(secret: int, steps: int):
    
    for i in range(0, steps):
        val1 = secret * 64
        val1 = mix(secret, val1)
        val1 = prune(val1)

        secret = val1
        val2 = int(secret / 32)
        val2 = mix(secret, val2)
        val2 = prune(val2)

        secret = val2
        val3 = secret * 2048
        val3 = mix(secret, val3)
        secret = prune(val3)
    
    return secret




def mix(secret: int, value: int):
    return xor(secret, value)

def prune(secret: int):
    return secret % 16777216


