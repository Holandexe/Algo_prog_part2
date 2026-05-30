import unittest
from lab9 import Trie, build_trie_from_patterns


class TestTrieStructure(unittest.TestCase):

    def test_insert_and_search_success(self) -> None:
        trie = Trie()
        trie.insert("apple")
        trie.insert("banana")

        self.assertTrue(trie.search("apple"))
        self.assertTrue(trie.search("banana"))

    def test_search_non_existent_word(self) -> None:
        trie = Trie()
        trie.insert("apple")

        self.assertFalse(trie.search("app"))
        self.assertFalse(trie.search("apricot"))
        self.assertFalse(trie.search("orange"))

    def test_starts_with(self) -> None:
        trie = Trie()
        trie.insert("computer")
        trie.insert("communication")

        self.assertTrue(trie.starts_with("comp"))
        self.assertTrue(trie.starts_with("comm"))
        self.assertTrue(trie.starts_with("c"))
        self.assertFalse(trie.starts_with("cat"))

    def test_build_trie_from_patterns(self) -> None:
        patterns = ["iot", "it", "lviv", "polytechnic"]
        trie = build_trie_from_patterns(patterns)

        for word in patterns:
            self.assertTrue(trie.search(word))

        self.assertTrue(trie.starts_with("poly"))
        self.assertFalse(trie.search("poly"))


if __name__ == "__main__":
    unittest.main()