import sys
from util import parse_input
from util import part1_process
from util import part2_process

def run(part: str):
    if part == "1":
        # expected: 200446
        print(part1_process(parse_input(), 25))
    if part == "2":
        # expected: 
        print(part2_process(parse_input()))
        pass



if __name__ == '__main__':
    run(sys.argv[1])