import unittest

from util import parse_input
from util import part1_process

input = [
    'MMMSXXMASM',
    'MSAMXMSMSA',
    'AMXSXMAAMM',
    'MSAMASMSMX',
    'XMASAMXAMM',
    'XXAMMXXAMA',
    'SMSMSASXSS',
    'SAXAMASAAA',
    'MAMMMXMMMM',
    'MXMXAXMASX'
]


class TestDay4(unittest.TestCase):

    def test_parse_input(self):
        self.assertListEqual(input, parse_input("test_input.txt"))

    def test_process(self):
        self.assertEqual(18, part1_process(parse_input("test_input.txt")))
        

if __name__ == '__main__':
    unittest.main()
