import unittest

from main import parse_input, transform_input, process

input = [
    [3, 4, 2, 1, 3, 3],
    [4, 3, 5, 3, 9, 3]
];

result = [
    [1, 2, 3, 3, 3, 4],
    [3, 3, 3, 4, 5, 9]
]


class TestDay1(unittest.TestCase):

    def test_parse_input(self):
        self.assertListEqual(input, parse_input("test_input.txt"))

    def test_transform_input(self):
        self.assertListEqual(result, transform_input(input))

    def test_process(self):
        self.assertEqual(11, process(transform_input(input)))
        

if __name__ == '__main__':
    unittest.main()