import unittest

from util import parse_input
from util import part1_process
from util import part2_process

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

input2 = [
    '.M.S......',
    '..A..MSMS.',
    '.M.S.MAA..',
    '..A.ASMSM.',
    '.M.S.M....',
    '..........',
    'S.S.S.S.S.',
    '.A.A.A.A..',
    'M.M.M.M.M.',
    '..........'
]

class TestDay4(unittest.TestCase):

    def test_parse_input(self):
        self.assertListEqual(input, parse_input("test_input.txt"))

    def test_process_part1(self):
        self.assertEqual(18, part1_process(parse_input("test_input.txt")))
    
    def test_process_part2(self):
        self.assertEqual(9, part2_process(input2))
        

if __name__ == '__main__':
    unittest.main()
