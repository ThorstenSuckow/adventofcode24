import unittest

from util import parse_input
from part1 import process


input = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]


class TestDay2Part1(unittest.TestCase):

    def test_parse_input(self):
        self.assertListEqual(input, parse_input("test_input.txt"))

    def test_process(self):
        self.assertEqual(2, process(input))
        

if __name__ == '__main__':
    unittest.main()
