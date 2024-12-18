import sys
from util import parse_input
from util import part1_process
from util import part2_process

def run(part: str):
    size = [71, 71]
    limit = 1023
    if part == "1":
        # expected: 268
        print(part1_process(parse_input(), size=size, limit=limit))
    if part == "2":
        # expected: (64, 11)
        print(part2_process(parse_input(), size=size, limit=limit))
        pass



if __name__ == '__main__':
    run(sys.argv[1])