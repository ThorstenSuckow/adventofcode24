import unittest

from util import parse_input
from util import part1_process
from util import part2_process


res = {
}

class Test(unittest.TestCase):

    def test_process_part1(self):
        [patterns, designs] = parse_input("test_input.txt")
        self.assertEqual(6 ,part1_process(patterns, designs))
        pass

    
    def test_process_part2(self):
        
        [patterns, designs] = parse_input("test_input.txt")
        self.assertEqual(16, part2_process(patterns, designs))
        pass







if __name__ == '__main__':
    unittest.main()
