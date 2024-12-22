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

    idx = 0
    for res in buyers:	
        
        for i in range(1, len(res) - 4):
    
            grp = (res[i][1], res[i + 1][1], 
                   res[i + 2][1], res[i + 3][1])
            
            if mp.get(grp) is None:
                # 4 buyers, assume we need at least
                # 3 entries. if idx is 2 and there
                # are no entries, skip this step
                if idx >= 2:
                    continue
                mp[grp] = {}
            
            key = res[i + 3][0]
            if mp[grp].get(key) is None:
                mp[grp][key] = []

            lsts = mp[grp]
            found = False
            for l in lsts:
                if idx in lsts[l]:
                    found = True
                    break
            if (found == False):
                mp[grp][key].append(idx)
            
            
        idx+=1
    
    max = 0
    for grp in mp:
        entries = mp[grp]
        
        if len(entries) < 1:
            continue
        
        s = 0
        for e in entries:
            s += e * len(entries[e])
        
        if s > max:
            max = s
            
    return max

'''
Helper
'''

def find_max(res: list):

    m = 0
    for tpl in res: 
        m = max(m, tpl[1])
    
    return m

def calc_secret(secret: int, steps: int, as_list = False):

    l = [(int(str(secret)[-1]), 0)]
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

        if as_list:
            last = int(str(secret)[-1])
            diff = last - l[-1][0] 
            l.append((last, diff))


    return l if as_list else secret


def mix(secret: int, value: int):
    return xor(secret, value)

def prune(secret: int):
    return secret % 16777216


