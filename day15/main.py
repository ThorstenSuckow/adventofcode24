import sys
from util import parse_input
from util import part1_process
from util import part2_process

def run(part: str):
    if part == "1":
        # expected: 1487337
        [mesh, directions] = parse_input()
        print(part1_process(mesh, directions))
    if part == "2":
        # expected: 1521952
        [mesh, directions] = parse_input(widen=True)
        print(part2_process(mesh, directions))
        pass



if __name__ == '__main__':
    run(sys.argv[1])