import unittest

class Trie:
    """
    docstring
    """
    def __init__(self) -> None:
        self.root = {}
        self.endWord = "#"

    def insert(self, word):
        """
        docstring
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})

        node[self.endWord] = self.endWord

    def search(self, word):
        """
        
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]

        return self.endWord in node

    def startWith(self, prefix):
        """
        docstring
        """
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True

class Test(unittest.TestCase):
    def testTrieSearch(self):
        """
        docstring
        """
        trie = Trie()
        trie.insert("Trieee")
        self.assertEqual(trie.search("Triee"), False)

    def testTrieStartWith(self):
        """
        docstring
        """
        trie = Trie()
        trie.insert("Trieee")
        self.assertEqual(trie.startWith("Tri"), True)


if __name__ == "__main__":
    unittest.main()
