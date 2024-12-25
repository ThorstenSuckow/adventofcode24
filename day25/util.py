from fileinput import input
import operator
import time

class Lock:
    height = None
    values = None

    def __str__(self):
        return f"Key: {self.height} {self.values}"


    def __init__(self, height, values):
        self.height = height
        self.values = values

class Key:
    height = None
    values = None

    def __str__(self):
        return f"Key: {self.height} {self.values}"

    def __init__(self, height, values):
        self.height = height
        self.values = values

    def opens(self, lock: "Lock"):
        lpins = lock.values
        kpins = self.values    
          
        addl = list(map(operator.add, lock.values, self.values))
        if len(list(filter(lambda x: x > 7, addl))) > 0:
            return False

        return True
        

def parse_input(file_name = "") -> map:

    if not file_name:
        file_name = './input.txt'

    locks = []
    keys  = []
    tpl = None
    is_lock = False
    initialized = False
    height = 0

    lns =  []

    for line in input(files=(file_name)):
        lns.append(line)
    
    lns.append("")
    
    for line in lns:
        line = line.strip()

        if line == "":
            if tpl != None:
                if is_lock:
                    locks.append(Lock(height, tpl))
                else: 
                    keys.append(Key(height, tpl))
            initialized = False
            is_lock = False
            tpl = None
            height = 0
            continue
        
        if line != "" and initialized == False:
            is_lock = line == ('#' * len(line))
            
            initialized = True
            tpl = [0] * len(line)
            
        
        i = 0
        for c in line:
            tpl[i] += 1 if c == '#' else 0
            i+=1
        
        if line == ('#' * len(line)):
            height += 1

    return [locks, keys]

'''
PART 1
'''
def part1_process(locks: list, keys: list) -> int:
    
    res = 0
    for key in keys:
        for lock in locks:
            if key.opens(lock):
                res += 1


    return res

'''
PART 2
'''
def part2_process(locks: map, keys: list) -> int:
   
   pass

'''
Helper
'''