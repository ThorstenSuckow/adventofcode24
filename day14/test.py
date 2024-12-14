import unittest

from util import parse_input
from util import part1_process
from util import part2_process


res = {
}

class TestDay14(unittest.TestCase):

    def test_process_part1(self):
        self.assertEqual(
            12 ,
            part1_process(
                parse_input("test_input.txt"), 
                11, 7, 100
            ))
        pass

   






if __name__ == '__main__':
    unittest.main()
