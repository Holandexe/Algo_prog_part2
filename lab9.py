class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


def build_trie_from_patterns(patterns: list) -> Trie:
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie

if __name__ == "__main__":
    patterns = ["apple", "iot", "banana", "polytechnic"]
    
    trie = build_trie_from_patterns(patterns)
    
    print("--- Результати роботи програми ---")
    print(f"Чи є слово 'apple' в дереві? -> {trie.search('apple')}")
    print(f"Чи є слово 'apricot' в дереві? -> {trie.search('apricot')}")
    print(f"Чи є префікс 'poly' в дереві?  -> {trie.starts_with('poly')}")
    print(f"Чи є префікс 'io' в дереві?   -> {trie.starts_with('io')}")