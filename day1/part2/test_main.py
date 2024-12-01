import unittest

from main import count_in, process


input = [
    [1, 2, 3, 3, 3, 4],
    [3, 3, 3, 4, 5, 9]
]


class TestDay1(unittest.TestCase):

    def test_count_in(self):
        self.assertEqual(0, count_in(1, input[1]))
        self.assertEqual(3, count_in(3, input[1]))
        self.assertEqual(1, count_in(4, input[1]))
        self.assertEqual(1, count_in(5, input[1]))

    def test_process(self):
        self.assertEqual(31, process(input))


if __name__ == '__main__':
    unittest.main()