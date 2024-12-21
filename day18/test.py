import unittest

from util import parse_input
from util import part1_process
from util import part2_process


res = {
}

class Test(unittest.TestCase):

    def test_process_part1(self):
        self.assertEqual(22 ,part1_process(parse_input("test_input.txt"), size=[7,7], limit=11))
        pass

    
    def test_process_part2(self):
        self.assertEqual((6,1), part2_process(parse_input("test_input.txt"), size=[7,7], limit = 11))
        pass







if __name__ == '__main__':
    unittest.main()