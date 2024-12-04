import unittest

from util import parse_input
from part1 import process


input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


class TestDay3Part1(unittest.TestCase):

    def test_parse_input(self):
        self.assertListEqual([[2, 4], [5,5], [11,8], [8,5]], parse_input("test_input.txt"))

    def test_process(self):
        self.assertEqual(161, process(parse_input("test_input.txt")))

        

if __name__ == '__main__':
    unittest.main()
