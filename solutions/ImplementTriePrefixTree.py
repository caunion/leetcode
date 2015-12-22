from BaseSolution import *

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = [None] * 26
        self.char = None
        self.end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def char2num(self, c):
        return ord(c) - ord('a')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        top = self.root
        for c in word:
            i = self.char2num(c)
            if not top.child[i]:
                top.child[i] = TrieNode()
                top.child[i].char = c
            top = top.child[i]
        top.end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        top = self.root
        for c in word:
            i = self.char2num(c)
            if not top.child[i]:
                return False
            top = top.child[i]
        return top.end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        top = self.root
        for c in prefix:
            i = self.char2num(c)
            if not top.child[i]:
                return False
            top = top.child[i]
        return True

class ImplementTriePrefixTree(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([(0, "abc"),(1,"ab"),(0, "ab"),(1,"ab"),(2,"ab")],),
            expects= [None, False, None, True, True]
        )
    def solution(self, ops):
        result = []
        tree = Trie()
        for op in ops:
            if op[0] == 0:
                ret = tree.insert(op[1])
            elif op[0] == 1:
                ret = tree.search(op[1])
            elif op[0] == 2:
                ret = tree.startsWith(op[1])
            result.append(ret)
        return result