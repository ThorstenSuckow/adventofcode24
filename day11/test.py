import unittest

from util import parse_input
from util import part1_process
from util import part2_process


res = {
}

class TestDay11(unittest.TestCase):

    def test_process_part1(self):
        self.assertEqual(55312 ,part1_process(parse_input("test_input.txt"), 25))
        pass

   






if __name__ == '__main__':
    unittest.main()
