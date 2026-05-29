import unittest
from wchain import solve_wchain

class TestWchain(unittest.TestCase):

    def test_example_1(self):
        words = ["crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"]
        self.assertEqual(solve_wchain(words), 6)

    def test_example_2(self):
        words = ["b", "bcad", "bca", "bad", "bd"]
        self.assertEqual(solve_wchain(words), 4)

    def test_example_3(self):
        words = ["word", "anotherword", "yetanotherword"]
        self.assertEqual(solve_wchain(words), 1)
        
    def test_single_letters(self):
        words = ["a", "b", "c"]
        self.assertEqual(solve_wchain(words), 1)

if __name__ == "__main__":
    unittest.main()