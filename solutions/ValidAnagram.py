__author__ = 'Daoyuan'
from BaseSolution import *

class ValidAnagram(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("anagram", "nagaram",),
            expects = True
        )
        self.push_test(
            params = ("anadgram", "nagaram",),
            expects = False
        )

    def solution(self, s,t):
        return self.gethash(s) == self.gethash(t)

    def gethash(self, s):
        dic = {}
        for c in s:
            if dic.has_key(c): dic[c] = dic[c]+1
            else: dic[c] = 1
        hash = ""
        for key in sorted(dic):
            hash = hash + key + str(dic[key])
        return hash