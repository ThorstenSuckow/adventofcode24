import unittest

from util import parse_input
from util import part1_process
from util import part2_process
from util import Mesh

res = {
    '0': [(8, 1), (5, 2), (7, 3), (4, 4)], 
    'A': [(6, 5), (8, 8), (9, 9)]
}

class TestDay8(unittest.TestCase):

    def test_parse_input(self):

        mesh = parse_input("test_input.txt")
        self.assertDictEqual(res, mesh._data)
        self.assertEqual(11, mesh._max_x)
        self.assertEqual(11, mesh._max_y)
        pass

    def test__process_part1(self):
        self.assertEqual(14, part1_process(parse_input("test_input.txt")))
        pass

    
    def test_process_part2(self):
        
        mesh = part2_process(parse_input("test_input.txt"))
        self.assertEqual(34, part2_process(parse_input("test_input.txt")))
        
        pass







if __name__ == '__main__':
    unittest.main()
