import unittest
from lab5 import find_min_depth, read_input, write_output

class TestMinDepth(unittest.TestCase):

    def test_tree_from_task(self):
        edges = {
            1: [2, 3],
            2: [4, 5],
            3: [6, 7],
            4: [8],
            5: [9],
            7: [10, 11],
            8: [12]
        }
        result = find_min_depth(1, edges)
        self.assertEqual(result, 3)

    def test_single_node(self):
        edges = {}
        result = find_min_depth(1, edges)
        self.assertEqual(result, 1)

    def test_linear_chain(self):
        edges = {
            1: [2],
            2: [3],
            3: [4]
        }
        result = find_min_depth(1, edges)
        self.assertEqual(result, 4)

    def test_balanced_tree_depth_2(self):
        edges = {
            1: [2, 3]
        }
        result = find_min_depth(1, edges)
        self.assertEqual(result, 2)

    def test_left_skewed_with_right_leaf(self):
        edges = {
            1: [2, 3],
            2: [4],
            4: [5]
        }
        result = find_min_depth(1, edges)
        self.assertEqual(result, 2)

    def test_all_leaves_at_same_depth(self):
        edges = {
            10: [20, 30],
            20: [40, 50],
            30: [60, 70]
        }
        result = find_min_depth(10, edges)
        self.assertEqual(result, 3)

    def test_two_level_tree_one_branch_deeper(self):
        edges = {
            1: [2, 3],
            2: [4, 5],
            4: [8]
        }
        result = find_min_depth(1, edges)
        self.assertEqual(result, 2)

    def test_root_is_none(self):
        result = find_min_depth(None, {})
        self.assertEqual(result, 0)

    def test_deep_right_shallow_left(self):
        edges = {
            1: [2, 3],
            3: [6],
            6: [12],
            12: [24]
        }
        result = find_min_depth(1, edges)
        self.assertEqual(result, 2)

    def test_read_input_with_comments(self):
        tmp = 'tmp_test_input.txt'
        f = open(tmp, 'w')
        f.write('1   # tree root\n')
        f.write('1,2 # edge from 1 to 2\n')
        f.write('2,4\n')
        f.close()
        
        root, edges = read_input(tmp)
        result = find_min_depth(root, edges)
        # We don't use os.remove here to avoid extra imports
        self.assertEqual(result, 2)

    def test_write_output(self):
        tmp = 'tmp_test_output.txt'
        write_output(tmp, 5)
        f = open(tmp, 'r')
        content = f.read().strip()
        f.close()
        self.assertEqual(content, '5')

if __name__ == '__main__':
    unittest.main()