import unittest

from util import parse_input
from util import part1_process
from util import part2_process
from util import Node, Data
import itertools

res = [
    [190, [10, 19]],
    [3267, [81, 40, 27]],
    [83, [17, 5]],
    [156, [15, 6]],
    [7290, [6, 8, 6, 15]],
    [161011, [16, 10, 13]],
    [192, [17, 8, 14]],
    [21037, [9, 7, 18, 13]],
    [292, [11, 6, 16, 20]]
]

class TestDay7(unittest.TestCase):

    def t_est_node(self):

        n = Node(4)

        self.assertIsNone(n.left())
        self.assertIsNone(n.right())
        self.assertEqual(4, n.value())

        self.assertIs(n, n.append_left(5))
        self.assertIs(n, n.append_right(6))
        
        self.assertEqual(20, n.left().value())
        self.assertEqual(10, n.right().value())

    def test_parse_input(self):
        data = parse_input("test_input.txt")
        for i in range(0, len(res)):
            self.assertEqual(res[i][0], data[i].target_value)
            self.assertListEqual(res[i][1], data[i].values)
            
        pass

    def test_process_part1(self):

        data = Data(3267, [81, 40, 27])    
        self.assertEqual(3267, part1_process([data]))

        res = part1_process(parse_input("test_input.txt"))

        self.assertEqual(3749, res)
        pass


    def test_process_part2(self):



        data = Data(7290, [6, 8, 6, 15])    
        self.assertEqual(7290, part2_process([data]))

        data = Data(156, [15, 6])    
        self.assertEqual(156, part2_process([data]))

        data = Data(192, [17, 8, 14])    
        self.assertEqual(192, part2_process([data]))

        pass

    def scratchpad(self):

        target_value = 7290
        values = [6, 8, 6, 15]

        def partition_n(n):
            res = []
            j = 0
            i = 1
            while (i != n + 1):
                grp = []
            
                grp.append(i)
                for k in range(i, n):
                    grp.append(1)
                i += 1
                j += 1
                res.append(grp)
            return res
        
        partitions = partition_n(len(values))

        perms = []
        for p in partitions:
            #print(": ",p)
            for comb in itertools.permutations(p, len(p)):
                if comb not in perms:
                    perms.append(comb)
                    #print("-> ",comb)
        
        #print(perms)

        fin = []
        for p in perms:
            
            i = 0
            d = Data(target_value, [])
            for len_v in p:
                v = ''
                for j in range(0, len_v):
                    v += str(values[i])
                    i+=1
                d.values.append(int(v))
            fin.append(d)
        
        print(fin[2].values)

        print(part1_process([fin[2]]))

  





if __name__ == '__main__':
    unittest.main()
