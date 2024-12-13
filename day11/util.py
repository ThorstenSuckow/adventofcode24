from fileinput import input
import re

node_map = {}

class Node:
    lft = None
    rgt = None
    val = None
    
    def __str__(self):
        return f"{self.val} L:({self.lft}) R:({self.rgt})"

    def __init__(self, val):
        self.val = val

    def left(self) -> "Node":
        return self.lft
    
    def right(self) -> "Node":
        return self.rgt
    

    def append_left(self, lft: int) -> "Node":
        self.lft = Node(lft)

        if node_map.get(lft) is None:
            node_map[lft] = self.lft
        
        return self.lft

    def append_right(self, rgt: int) -> "Node":
        self.rgt = Node(rgt)
        
        if node_map.get(rgt) is None:
            node_map[rgt] = self.rgt

        return self.rgt
    
    def set_value(self, val):
        self.val = val

    def value(self):
        return self.val

    def leaf_count(self) -> int:
        
        if self.left() is None and self.right() is None:
            return 1
        
        return  self.left().leaf_count() + self.right().leaf_count()

    def blink(self) -> "Node":

        if self.left():
            self.left().blink()

        if self.right():
            self.right().blink()

        if self.left() is None and self.right() is None:
            vlen = len(str(self.value()))
            hlf = int(vlen / 2)

            if self.value() == 0:
                self.set_value(1)
            elif vlen % 2 == 0:
                self.append_left(int(str(self.value())[:hlf]))
                self.append_right(int(str(self.value())[hlf:]))
            else:
                self.set_value(self.value() * 2024)
        
        return self       




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
def part1_process(data: list, blink: int) -> int:

    nodes = []
    print("->", blink)
    res = 0
    for i in data:
        
        n = Node(i)
        for j in range(0, blink):
            n.blink()
        
        c = n.leaf_count()
        res += c

    return res

'''
PART 2
'''
def part2_process(data: list) -> int:
    return part1_process(data, 75)
    
    
'''
HELPER
'''
