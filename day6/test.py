import unittest

from util import parse_input
from util import part1_process
from util import part2_process
import util

result_Y = [[4], [9], [], [2], [7], [],[1], [8], [0], [6]]
result_X = [[8], [6], [3], [], [0], [],[9], [4], [7], [1]]

pos = [[4, 6], (0,-1)]

class TestDay5(unittest.TestCase):

    def test_parse_input(self):
        guard_pos = parse_input("test_input.txt")
        self.assertListEqual(pos, guard_pos)
        self.assertListEqual(result_X, util.X)
        self.assertListEqual(result_Y, util.Y)
        self.assertEqual(9, util.MAX_X)
        self.assertEqual(9, util.MAX_Y)
        self.assertTupleEqual(util.V[2], util.next_dir(util.V[0]))
        self.assertTupleEqual(util.V[0], util.next_dir(util.V[1]))
        self.assertTupleEqual(util.V[3], util.next_dir(util.V[2]))
        self.assertTupleEqual(util.V[1], util.next_dir(util.V[3]))
        

    def test_process_part1(self):
        self.assertEqual(41, part1_process(parse_input("test_input.txt")))
        pass

    def test_process_part2(self):
        self.assertEqual(6, part2_process(parse_input("test_input.txt")))
        pass    

if __name__ == '__main__':
    unittest.main()
