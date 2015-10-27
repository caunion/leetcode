__author__ = 'Daoyuan'

from ..BaseSolution import *

class BrokenKeyboard(BaseSolution):

    """

    Single linked list
    e.g. 6.4, p.229
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ( ["test_[aa]bb]cc]dd]]]]ee[ff]gg",
                        "This_is_a_[Beiju]_text",
                        "[[]][][]]Happy_Birthday_to_Tsinghua_University"],),
            expects = [ "ffaatest_bbccddeegg",
                        "BeijuThis_is_a__text",
                        "Happy_Birthday_to_Tsinghua_University"]
        )

    def solution(self, params):
        ret = []
        for text in params:
            cur = 0
            last = 0
            length = len(text)
            next = range(0, length + 1)
            next[length] = 0
            for idx in range(1, length+1):
                char = text[idx-1]
                if char == "[":
                    cur = 0
                    #last = min(last, idx-1)
                elif char == "]":
                    cur = last
                else:
                    next[idx] = next[cur]
                    next[cur] = idx
                    if cur == last:
                        last = idx
                    cur = idx

            s = ""
            d = 0
            for i in range(0,length):
                d = next[d]
                if d==0: break
                s = s + text[d-1]
            ret.append(s)
        return ret