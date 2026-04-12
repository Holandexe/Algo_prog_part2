import unittest
from lab3 import BinaryTree, invert_binary_tree


class TestInvertBinaryTree(unittest.TestCase):

    def test_example_from_task(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.right.left = BinaryTree(6)
        root.right.right = BinaryTree(7)

        invert_binary_tree(root)

        self.assertEqual(root.value, 1)
        self.assertEqual(root.left.value, 3)
        self.assertEqual(root.right.value, 2)
        self.assertEqual(root.left.left.value, 7)
        self.assertEqual(root.left.right.value, 6)
        self.assertEqual(root.right.left.value, 5)
        self.assertEqual(root.right.right.value, 4)

    def test_single_node(self):
        root = BinaryTree(5)
        result = invert_binary_tree(root)
        self.assertEqual(result.value, 5)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)

    def test_none_tree(self):
        self.assertIsNone(invert_binary_tree(None))

    def test_only_left_child(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        invert_binary_tree(root)
        self.assertIsNone(root.left)
        self.assertEqual(root.right.value, 2)

    def test_only_right_child(self):
        root = BinaryTree(1)
        root.right = BinaryTree(2)
        invert_binary_tree(root)
        self.assertEqual(root.left.value, 2)
        self.assertIsNone(root.right)

    def test_two_levels(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        invert_binary_tree(root)
        self.assertEqual(root.left.value, 20)
        self.assertEqual(root.right.value, 9)

    def test_double_invert(self):
        root = BinaryTree(1, BinaryTree(2, BinaryTree(4)), BinaryTree(3))
        original_left = root.left.value
        invert_binary_tree(root)
        invert_binary_tree(root)
        self.assertEqual(root.left.value, original_left)

    def test_returns_binary_tree_instance(self):
        self.assertIsInstance(invert_binary_tree(BinaryTree(10)), BinaryTree)


if __name__ == "__main__":
    unittest.main()