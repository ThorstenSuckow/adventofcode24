import unittest

from util import parse_input
from util import part1_process
from util import part2_process


res = {
}

class TestDay14(unittest.TestCase):

    def test_process_part1(self):
        [mesh, directions] = parse_input("test_input.txt")
        self.assertEqual(10092 ,part1_process(mesh, directions))
        pass

    
    def test_process_part2(self):
        pass







if __name__ == '__main__':
    unittest.main()
