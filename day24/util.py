from fileinput import input
from operator import xor
import re
import time
import copy

class Eq:
    op: None
    o1: None
    o2: None
    res : None
    valuemap: None
    solved: None

    def reset(self):
        self.o1 = self.o1org
        self.o2 = self.o2org
        self.res = self.resorg
        
        self.solved = False
        
    def wire(self):
        return self.resorg

    def has_z(self):
        return self.resorg[0] == 'z'
    
    def is_x_and_y(self):
        return self.x_and_y() != -1

    def x_and_y(self):
        is_xl = self.o1org[0] == 'x'
        is_yr = self.o2org[0] == 'y'
        is_yl = self.o1org[0] == 'y'
        is_xr = self.o2org[0] == 'x'

        if (is_xl and is_yr) or (is_xr and is_yl):
            return int(self.o1org[1:])
        
        return -1

    def __init__(self, op, o1, o2, res):
        self.op = op
        self.o1 = o1
        self.o2 = o2
        self.res = res
        
        self.o1org = o1
        self.o2org = o2
        self.resorg = res
        
        self.solved = False

    def __str__(self):
        return f"{self.op} {self.o1} {self.o2} = {self.res} ({self.solved}) [{self.o1org} {self.o2org} {self.resorg}]"

    def solve(self, valuemap: map):
        if self.solved == True:
            return self.solved
        
        self.valuemap = valuemap
        
        if self.o1 not in [0,1] and self.valuemap.get(self.o1) is not None:
            self.o1 = self.valuemap.get(self.o1)
        if self.o2 not in [0,1] and self.valuemap.get(self.o2) is not None:
            self.o2 = self.valuemap.get(self.o2)
        if self.res not in [0,1] and self.valuemap.get(self.res) is not None:
            self.res = self.valuemap.get(self.res)
        
        res = self.eval() 
        self.valuemap = None
        return res   

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
            eq = Eq(os[1], os[0], os[2], res)
            eqs.append(eq)


    return [vals, eqs]

'''
PART 1
'''
def part1_process(vals: map, eqs: list) -> int:

    solve(vals, eqs)

    zs = get_zs(vals)        

    zs = list(map(lambda x: str(x), reversed(list(dict(sorted(zs.items())).values()))))
    
    return int(''.join(zs), 2)

'''
PART 2
'''
def part2_process(vals: map, eqs: list) -> int:
   
    valcopy = copy.deepcopy(vals)
    last_wire = f"z{int(len(valcopy)/2)}" 
   
    solve(valcopy, eqs)

    andxored = []
    faulty = []
    for eq in eqs:
        x_and_y = eq.x_and_y()
        if x_and_y != -1:
            if eq.op == 'AND' or eq.op == 'XOR':
                if x_and_y in andxored:
                    raise Exception(str(eq)) 
                andxored.append(eq.x_and_y)
        # for the adder the last z-wired output will be an OR-Gate
        if eq.has_z() and eq.op != 'XOR' and eq.resorg != last_wire:
            faulty.append(eq.resorg)
        elif eq.is_x_and_y() == False and eq.has_z() == False and eq.op == 'XOR':
            faulty.append(eq.resorg) 
        elif eq.x_and_y() not in [0, -1] and eq.op in ['AND', 'XOR']:
            # if there is an anded or xored output, this
            # output must be the input for an OR-Gate (for AND) respective
            # for another XOR-Gate
            match = 'OR' if eq.op == 'AND' else 'XOR'
            found = False
            for tmp in eqs:
                if tmp == eq:
                    continue
                if (tmp.op == match and eq.resorg in [tmp.o1org, tmp.o2org]): 
                    found = True
                    break
            if found == False:
                faulty.append(eq.resorg)
                pass


    return ','.join(sorted(faulty))
    
'''
Helper
'''

def reset_all(eqs: list):
    for e in eqs:
        e.reset()


def get_wires(eqs:list):

    wires = []
    for e in eqs:
        wires.append(e.resorg)

    return wires

def get_sum(eqs: list, xycount):

    length = int(xycount/2)

    bs = {
        'x': list(range(0, length)),
        'y': list(range(0, length)),
        'sum': [] 
    }

    for eq in eqs:
        if eq.o1org[0] in ['x', 'y']:
            idx = int(eq.o1org[1:])
            trg = eq.o1org[0]
            bs[trg][idx] = eq.o1
        
        if eq.o2org[0] in ['x', 'y']:
            idx = int(eq.o2org[1:])
            trg = eq.o2org[0]
            bs[trg][idx] = eq.o2

    sum = (int(''.join(list(reversed(list(map(lambda x: str(x), bs['x']))))), 2) +
            int(''.join(list(reversed(list(map(lambda x: str(x), bs['y']))))), 2)
            )
    bs['sum'] = list(reversed(list(map(lambda x: int(x), list("{0:b}".format(sum))))))

    return bs
    
def get_zs(vals, as_bin = False):
    zs = {}
    for v in vals:
        if isinstance(v, str) and v.startswith('z'):
            zs[ int(v[1:])  ] = vals[v]

    res = []
    if as_bin == True:
        for i in range(0, len(zs)):
            res.append(zs[i])
        return res
    
    return zs

def solve(vals, eqs):

    breakme = False
    while (breakme == False):
        breakme = True
        for eq in eqs:
            solved = eq.solve(vals)
            if solved == False:
                breakme = False


