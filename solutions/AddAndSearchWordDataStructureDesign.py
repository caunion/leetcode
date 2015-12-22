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
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.tree = Trie()

    def char2num(self, c):
        return ord(c) - ord('a')

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.tree.insert(word)


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        stack = [(word, self.tree.root)]
        while len(stack) > 0:
            w, top = stack.pop()
            n = len(w)
            if not top:
                continue
            if n == 0 and top.end:
                return True
            ret = False
            for i in xrange(n):
                c = w[i]
                p = self.char2num(c)
                if c != ".":
                    if top.child[p]:
                        ret = True
                        top = top.child[p]
                    else:
                        ret = False
                        break
                else:
                    ret = False
                    for child in top.child:
                        if child:
                            stack.append( (w[i+1:], child) )
                    break
            if i == n-1 and ret and top.end:
                return True
        return False
class AddAndSearchWordDataStructureDesign(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([(0, 'ran'),(0, 'rune'),(0, 'runner'),(0, 'runs'),(0, 'add'),(0, 'adds'),(0, 'adder'),(1,'r.n')],),
            expects= [None,None,None,None,None,None,None, True]
        )
        self.push_test(
            params = ([(0, 'and'),(0, 'at'),(1,'a.'),(1,'aa'),(1,'.a'),(1,'.'),(1,'a')],),
            expects= [None, None, True, False, False, False, False]
        )
        self.push_test(
            params = ([(0, 'a'),(1,'a.'),(1,'aa'),(1,'.a'),(1,'.'),(1,'a')],),
            expects= [None, False, False, False, True, True]
        )

        self.push_test(
            params = ([(0, 'a'),(1,'.'),(0,'bcd'),(0,'def'),(1,'..d'),(1,'d.f'),(1,'d.g')],),
            expects= [None, True, None, None, True, True, False]
        )

    def solution(self, ops):
        result = []
        dic = WordDictionary()
        for op in ops:
            if op[0] == 0:
                ret = dic.addWord(op[1])
            elif op[0] == 1:
                ret = dic.search(op[1])
            result.append(ret)
        return result