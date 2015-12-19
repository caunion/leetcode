from BaseSolution import *
class RemoveDuplicateLetters(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("cbacdcbc",),
            expects = "acdb"
        )
    def solution(self, s):
        return self.removeDupe(s, "")

    def removeDupe(self, s, prev):
        if len(s) == 0: return prev
        alpha = [0] * 26
        p = 0
        for i,c in enumerate(s):
            alpha[ ord(c) -ord('a') ] += 1
        for i,c in enumerate(s):
            if c < s[p]: p = i
            alpha[ord(c) - ord('a')] -= 1
            if not alpha[ord(c) - ord('a')]:
                break
        c = s[p]
        prev += c
        s = s[p+1:].replace(c, '')
        return self.removeDupe(s, prev)
