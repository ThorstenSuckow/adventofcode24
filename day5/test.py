import unittest

from util import parse_input
from util import part1_process
from util import part2_process

sets = {47: [13, 29, 53, 61], 97: [13, 29, 47, 53, 61, 75], 75: [13, 29, 47, 53, 61], 61: [13, 29, 53], 29: [13], 53: [13, 29]} 

pages = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47]
]

class TestDay5(unittest.TestCase):

    def test_parse_input(self):
        [sets_res, pages_res] = parse_input("test_input.txt")
        self.assertDictEqual(sets, sets_res)
        self.assertListEqual(pages, pages_res)

    def test_process_part1(self):
        self.assertEqual(143, part1_process(parse_input("test_input.txt")))
    
    def test_process_part2(self):
        self.assertEqual(123, part2_process(parse_input("test_input.txt")))
        

if __name__ == '__main__':
    unittest.main()
