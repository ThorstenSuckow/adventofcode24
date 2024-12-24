from fileinput import input
from operator import xor
import re
import time

class Eq:
    op: None
    o1: None
    o2: None
    res : None
    valuemap: None
    solved: None

    def __init__(self, op, o1, o2, res, valuemap):
        self.op = op
        self.o1 = o1
        self.o2 = o2
        self.res = res
        self.valuemap = valuemap
        self.solved = False

    def __str__(self):
        return f"{self.op} {self.o1} {self.o2} = {self.res} ({self.solved})"

    def solve(self):
        if self.solved == True:
            return self.solved
        if self.o1 not in [0,1] and self.valuemap.get(self.o1) is not None:
            self.o1 = self.valuemap.get(self.o1)
        if self.o2 not in [0,1] and self.valuemap.get(self.o2) is not None:
            self.o2 = self.valuemap.get(self.o2)
        if self.res not in [0,1] and self.valuemap.get(self.res) is not None:
            self.res = self.valuemap.get(self.res)
        
        return self.eval()    

    def log(self, o1, o2, res):
        if o1 not in [0,1] or o2 not in [0, 1] or res not in [0, 1]:
            self.solved = False
            return False
        
        self.valuemap[self.o1] = o1
        self.valuemap[self.o2] = o2
        self.valuemap[self.res] = res

        self.o1 = self.valuemap[self.o1]
        self.o2 = self.valuemap[self.o2]
        self.res = self.valuemap[self.res]

        self.solved = True
        return True
    
    def andd(self):
        o1 = self.o1
        o2 = self.o2
        res = self.res
        if o1 in[0,1] and o2 in[0,1]:
            res = o1 and o2
        elif o1 == 1 and o2 == 1:
            res = 1
        if o1 == 0 and o2 == 0:
            res = 0
        if o1 == 1 and res == 1:
            o2 = 1
        
        return self.log(o1, o2, res)    

    def orr(self):
        o1 = self.o1
        o2 = self.o2
        res = self.res
        if o1 in[0,1] and o2 in[0,1]:
            res = o1 or o2
        elif o1 == 1 and o2 == 1:
            res = 1
        elif o1 == 0 and o2 == 0:
            res = 0
        
        return self.log(o1, o2, res)    

    def xorr(self):
        o1 = self.o1
        o2 = self.o2
        res = self.res
        if o1 in[0,1] and o2 in[0,1]:
            res = xor(o1, o2)
        elif o1 == 1 and o2 == 1:
            res = 0
        elif o1 == 0 and o2 == 0:
            res = 0
        elif o1 == 1 and res == 0:
            o2 = 1
        elif o1 == 0 and res == 0:
            o2 = 0
        elif o2 == 1 and res == 0:
            o1 = 1
        elif o2 == 0 and res == 0:
            o1 = 0
            
        return self.log(o1, o2, res)    


    def eval(self):

        if self.solved == True:
            return True
        
        if self.op == 'AND':
            return self.andd()
        
        if self.op == 'OR':
            return self.orr()
        
        if self.op == 'XOR':
            return self.xorr()            
                    



def parse_input(file_name = "") -> map:

    if not file_name:
        file_name = './input.txt'

    vals = {}
    eqs = []
    for line in input(files=(file_name)):
        line = line.strip()

        if line == "":
            continue

        if line.find(':') != -1:
            pairs = re.split(r"\:", line)

            lft = pairs[0]
            rgt = pairs[1]
            
            vals[lft] = int(rgt)
        else: 
            pairs = re.split(r"->", line)
            res = pairs[1].strip()
            os = re.split(r"\s", pairs[0])
            eq = Eq(os[1], os[0], os[2], res, vals)
            eqs.append(eq)


    return [vals, eqs]

'''
PART 1
'''
def part1_process(vals: map, eqs: list) -> int:

    breakme = False
    while (breakme == False):
        breakme = True
        for eq in eqs:
            solved = eq.solve()
            if solved == False:
                breakme = False

    zs = {}
    for v in vals:
        if isinstance(v, str) and v.startswith('z'):
            zs[ int(v[1:])  ] = vals[v]
            
    zs = list(map(lambda x: str(x), reversed(list(dict(sorted(zs.items())).values()))))
    
    return int(''.join(zs), 2)

'''
PART 2
'''
def part2_process(comps: map) -> int:
    res = 0
    return 0


'''
Helper
'''
