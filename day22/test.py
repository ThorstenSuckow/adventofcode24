import unittest

import util
from util import parse_input
from util import part1_process
from util import part2_process


res = {
}

class Test(unittest.TestCase):


    def test_process_part1(self):
        self.assertEqual(37327623, part1_process(parse_input('test_input.txt')))
        pass

    
    def test_process_part2(self):
        self.assertEqual(23, part2_process(parse_input('test_input.txt')))
        pass







if __name__ == '__main__':
    unittest.main()