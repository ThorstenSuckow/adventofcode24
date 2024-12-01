from fileinput import input
import re
def parse_input(file_name = "") -> list:

    list = [[], []]

    if not file_name:
        file_name = 'input.txt'


    for line in input(files=(file_name)):
        data = re.split(r'\s+', line.strip())
        list[0].append(int(data[0]))
        list[1].append(int(data[1]))

    return list

def transform_input(input: list) -> list:   
    
    left  = input[0]
    right = input[1]
    
    left.sort()
    right.sort()

    return [left, right]

def process(input: list) -> int:

    diff = 0

    for i in range(0, len(input[0])):
        lft  = input[0][i]
        rgt  = input[1][i]
        diff += abs(lft - rgt)

    return diff


def run():
    print(process(transform_input(parse_input())))


if __name__ == '__main__':
    run()

