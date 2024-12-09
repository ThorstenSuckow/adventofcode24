from fileinput import input
import re

class Data:
    target_value = None
    values = None

    def __init__(self, tv, val):
        self.target_value = tv
        self.values = val

    def visit_nodes(self, n: "Node", result) -> int:
        
        if n.left() and n.value() <= self.target_value:
            self.visit_nodes(n.left(), result)
        
        if n.right() and  n.value() <= self.target_value:
            self.visit_nodes(n.right(), result)
        
        if (n.left() is None and n.right() is None):
            result.append(n.value())

    def process(self, n : "Node") -> int:
        self.result = []
        self.visit_nodes(n, self.result)
        res = 0
        
        for val in self.result:
            if val == self.target_value:
                res +=1

        return res        

class Node:
    lft = None
    rgt = None
    val = None
    
    def __str__(self):
        return f"{self.val} {self.lft} {self.rgt}"

    def __init__(self, val):
        self.val = val

    def left(self) -> "Node":
        return self.lft
    
    def right(self) -> "Node":
        return self.rgt

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
        
    
    def insert(node, index):
        if (index >= len(data.values)):
            return 
        
        el = data.values[index]

        node.append_left(el)
        node.append_right(el)

        insert(node.left(), index + 1)
        insert(node.right(), index + 1)

    res = 0
    for data in data_list:
        node = Node(data.values[0])
        insert(node, 1)
        res += data.target_value if data.process(node) > 0 else 0

    return res       



'''
PART 2
'''
def part2_process(data: list) -> int:

    return 0

    
'''
HELPER
'''
