#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie:
    class TrieNode(object):
        def __init__(self):
            self.is_word = False
            self.children = [None] * 26
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not p.children[index]:
                p.children[index] = Trie.TrieNode()
            p = p.children[index]
        p.is_word = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.find(word)
        return node is not None and node.is_word


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.find(prefix)

    def find(self, prefix):
        p = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not p.children[index]:
                return None
            p = p.children[index]
        return p



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
