import sys
from util import parse_input
from util import part1_process

def run(part: str):
    if part == "1":
        # expected: 2583
        print(part1_process(parse_input()))
  


if __name__ == '__main__':
    run(sys.argv[1])