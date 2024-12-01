from fileinput import input
import re

import sys
import os

sys.path.append(os.getcwd() + "/../lib")

from util import parse_input, transform_input


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

