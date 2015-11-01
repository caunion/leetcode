__author__ = 'Daoyuan'
from BaseSolution import *
class LetterCombinationsOfAPhoneNumber(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("23",),
            expects = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
            expect_unordered= True
        )
        self.push_test(
            params = ("2",),
            expects = ["a","b","c"],
            expect_unordered= True
        )
        self.push_test(
            params = ("",),
            expects = [],
            expect_unordered= True
        )
        self.push_test(
            params = ("223",)
        )

    def solution(self, digits):
        self.letters = [
            ' ',
            '',
            'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz'
        ]
        prev = [ self.letters[int(i)] for i in digits]
        length = len(prev)
        if length == 0: return []
        if length == 1: return [c for c in prev[0]]
        while length > 1:
            next=[]
            for i in xrange( length / 2 ):
                temp =  list(self.join( prev[i*2], prev[i*2+1] ))
                next.append( temp )
            if i*2+1 != length - 1:
                next.append( prev[length-1])
            length = len(next)
            prev =next
        return prev[0]

    def join(self, left, right):
        for i in left:
            for j in right:
                yield i+j