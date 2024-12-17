import unittest

from util import parse_input
from util import part1_process
from util import part2_process


res = {
}

class Test(unittest.TestCase):

    def test_process_part1(self):
        self.assertEqual(7036 ,part1_process(parse_input("test_input.txt")))
        pass

    
    def test_process_part2(self):
        #[mesh, directions] = parse_input("test_input.txt", True)
        #self.assertEqual(9021 ,part2_process(mesh, directions))
        pass







if __name__ == '__main__':
    unittest.main()
