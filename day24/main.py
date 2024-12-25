import sys
from util import parse_input
from util import part1_process
from util import part2_process

def run(part: str):
    if part == "1":
        # expected: 59619940979346
        print(part1_process(*parse_input()))
    if part == "2":
        # expected: bpt,fkp,krj,mfm,ngr,z06,z11,z31
        print(part2_process(*parse_input()))
        pass



if __name__ == '__main__':
    run(sys.argv[1])