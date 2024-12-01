import sys
import os

sys.path.append(os.getcwd() + "/../lib")

from util import parse_input, transform_input


def count_in(lft: int, input: list) -> int:
    occ = 0
    for i in range(0, len(input)):
        rgt = input[i]
        if rgt > lft:
            return occ
        
        if (rgt == lft):
            occ+=1

    return occ

def process(input: list) -> int:

    values = {}

    sim = 0

    for i in range(0, len(input[0])):
        lft  = input[0][i]

        if not lft in values:
            values[lft] = count_in(lft, input[1])

        if values[lft]:
            sim += lft * values[lft] 

    return sim


def run():
    print(process(transform_input(parse_input())))


if __name__ == '__main__':
    run()

