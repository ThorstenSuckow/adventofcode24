from fileinput import input
import re

class Data:
    target_value = None
    values = None
    result = None

    def __init__(self, tv, val):
        self.target_value = tv
        self.values = val
        self.result = 0

    
class Node:
    lft = None
    rgt = None
    val = None
    mid = None
    
    def __str__(self):
        return f"{self.val} L:({self.lft}) M:({self.mid}) L:({self.rgt})"

    def __init__(self, val):
        self.val = val

    def left(self) -> "Node":
        return self.lft
    
    def right(self) -> "Node":
        return self.rgt
    
    def middle(self) -> "Node":
        return self.mid
    

    def append_mid(self, mid: int) -> "Node":
        self.mid = Node(int(str(self.val) + str(mid)))
        return self


    def append_left(self, lft: int) -> "Node":
        self.lft = Node(self.val * lft)
        return self

    def append_right(self, rgt: int) -> "Node":
        self.rgt = Node(self.val + rgt)
        return self
    
    def set_value(self, val):
        self.val = val

    def value(self):
        return self.val



def parse_input(file_name = "") -> list:

    if not file_name:
        file_name = './input.txt'

    res = []
    for line in input(files=(file_name)):
        line = line.strip()

        parts = line.split(r":")
        target_value = int(parts[0].strip());
        values = parts[1].strip().split(r" ")
        values = list(map(int, values))
        res.append(Data(target_value, values))    
       
    return res


'''
PART 1
'''
def part1_process(data_list: list) -> int:
        
    
    res = 0
    for data in data_list:
        node = Node(data.values[0])
        insert(node, 1, data, False)
        res += data.target_value if data.result > 0 else 0

    return res       



'''
PART 2
'''
def part2_process(data_list: list) -> int:


    res = 0
    for data in data_list:
        node = Node(data.values[0])
        insert(node, 1, data, True)
        res += data.target_value if data.result > 0 else 0

    return res       


    
'''
HELPER
'''


def insert(node, index, data, use_middle = True):
    
    if (index >= len(data.values)):
        if node.value() == data.target_value:
            data.result += 1
        return 
    
    el = data.values[index]

    if use_middle is True:
        node.append_mid(el)
        if node.middle().value() <= data.target_value:
            insert(node.middle(), index + 1, data, use_middle)

    node.append_left(el)
    node.append_right(el)

    if node.left().value() <= data.target_value:
        insert(node.left(), index + 1, data, use_middle)
    
    if node.right().value() <= data.target_value:
        insert(node.right(), index + 1, data, use_middle)
