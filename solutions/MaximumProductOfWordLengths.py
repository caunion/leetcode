from BaseSolution import *
class MaximumProductOfWordLengths(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (["a","ab","abc","d","cd","bcd","abcd"],),
            expects = 4
        )
        self.push_test(
            params = (["a","aaa","aaaaaa",],),
            expects = 0
        )
        self.push_test(
            params = (["abcw", "baz", "foo", "bar", "xtfn", "abcdef"],),
            expects = 16
        )
    def solution(self, words):
        vecs = [ self.word2vec(word) for word in words]
        vecs = sorted(vecs, key = lambda x : -x[1]) #sort to make early truncate
        n = len(vecs)
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
               if not (vecs[i][0] & vecs[j][0]):
                   ret = max(ret, vecs[i][1] * vecs[j][1])
                   break
        return ret
    def word2vec(self, w):
        vec = 0
        i = 0
        for c in w:
            vec |=  (1 <<(ord(c) - ord('a')))
            i += 1
        return (vec, i)

    # use lambda to make code concise
    def solution(self, words):
        vecs = sorted(map(lambda w: (reduce(lambda x,y : x | 1<< (ord(y) - ord('a')), w, 0 ), len(w)), words), key= lambda item : -item[1])
        n = len(vecs)
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (vecs[i][0] & vecs[j][0]):
                    ret = max(ret, vecs[i][1] * vecs[j][1] )
                    break
        return ret

