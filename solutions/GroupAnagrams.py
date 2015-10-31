__author__ = 'Daoyuan'
from BaseSolution import *

class GroupAnagrams(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (["cab","pug","pei","nay","ron","rae","ems","ida","mes"],),
            expects = [["ida"],["ems","mes"],["rae"],["ron"],["nay"],["pei"],["pug"],["cab"]],
            expect_unordered=True
        )
        self.push_test(
            params = (["bat"],),
            expects = [["bat"]],
            expect_unordered=True
        )
        self.push_test(
            params = (["eat", "tea", "tan", "ate", "nat", "bat"],),
            expects = [
              ["ate", "eat","tea"],
              ["nat","tan"],
              ["bat"]
            ],
            expect_unordered=True
        )

    def solution(self, strs):
        if len(strs) == 0: return []
        wordhash = []
        for word in strs:
            dic = {}
            for c in word:
                if dic.has_key(c): dic[c] = dic[c]+1
                else: dic[c] = 1
            hash = ""
            for key in sorted(dic.keys()):
                hash = hash+key+str(dic[key])
            wordhash += hash,

        dic = {}
        for idx,word in enumerate(strs):
            if dic.has_key(wordhash[idx]):
                dic[wordhash[idx]] += word,
            else:
                dic[wordhash[idx]]= [word]

        ret = [ sorted(wordlist) for wordlist in dic.values()]
        return ret
