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
def part2_process(secrets: list) -> int:
    buyers = []

    mp = {}
    for secret in secrets:
        buyers.append(calc_secret(secret, 2000, True))

    for idx, res in enumerate(buyers, 0):	
        
        grps = {}
        for i in range(1, len(res) - 4):
            grpkey = (res[i][1], res[i + 1][1], 
                   res[i + 2][1], res[i + 3][1])
            
            if grps.get(grpkey):
                continue
            
            grps[grpkey] = True
            if mp.get(grpkey) is None:
                # 4 buyers, assume we need at least
                # 3 entries. if idx is 2 and there
                # are no entries, skip this step
                if idx >= 2:
                    continue
                mp[grpkey] = 0
            
            mp[grpkey] += res[i + 3][0]
            
    bananas = 0
    for grp in mp:
        bananas = max(bananas, mp[grp])
                    
    return bananas

'''
Helper
'''
def calc_secret(secret: int, steps: int, as_list = False):

    prev = secret % 10
    l = [(prev, 0)]
    for i in range(0, steps):
        secret = xor(secret, secret * 64) % 16777216
        secret = xor(secret, int(secret / 32)) % 16777216
        secret = xor(secret, secret * 2048) % 16777216

        if as_list:
            last = secret % 10 
            diff = last - prev 
            l.append((last, diff))
            prev = last


    return l if as_list else secret