from BaseSolution import *
class RemoveDuplicateLetters(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 9
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

    def solution(self, s):
        visited = [False] * 26
        stack = []
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in s:
            index = self.char2num(c)
            count[index] -= 1
            if visited[index] : continue
            while len(stack) > 0 and stack[-1] > c and count[self.char2num(stack[-1])] > 0:
                top = stack.pop()
                visited[self.char2num(top)] = False
            stack += c
            visited[index] = True
        return "".join(stack)
    def char2num(self, c):
        return ord(c) - ord('a')