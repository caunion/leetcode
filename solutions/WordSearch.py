from BaseSolution import *
class WordSearch(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params =(["ABCE","SFCS","ADEE"], "ABCCED",),
            expects = True
        )
    def solution(self, board, word):
        if not board or len(board) == 0 or not word or len(word) == 0: return False
        n = len(board)
        m = len(board[0])
        length = len(word)
        self.m = m
        self.n = n
        self.length = length
        for i in xrange(n):
            for j in xrange(m):
                if self.search(board, i,j, word, 0):
                    return True
        return False

    def search(self, board, i, j, word, p):
        if i >= self.n or i < 0 or j >= self.m or j < 0: return False
        if board[i][j] != word[p]:
            return False
        else:
            p +=1
            if p == self.length:
                return True
            ret = False
            back = board[i][j]
            board[i][j] = "#"
            if self.search(board, i+1, j, word, p): return True
            if self.search(board, i-1, j, word, p): return True
            if self.search(board, i, j+1, word, p): return True
            if self.search(board, i, j-1, word, p): return True
            board[i][j] = back