import sys
from util import parse_input
from part1 import process as part1_process
from part2 import process as part2_process


def run(part: str):
    if part == "1":
        print(part1_process(parse_input()))
    if part == "2":
        print(part2_process(parse_input()))



if __name__ == '__main__':
    run(sys.argv[1])