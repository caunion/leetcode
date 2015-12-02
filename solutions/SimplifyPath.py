__author__ = 'Daoyuan'
from BaseSolution import *

class SimplifyPath(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("/a/./b/../../c/",),
            expects = "/c"
        )
    def solution(self, path):
        stack = []
        segs = path.split("/")
        for seg in segs:
            if seg == ".":
                continue
            elif seg == "..":
                if len(stack) > 0:
                    stack.pop()
            elif len(seg)>0:
                stack.append(seg)

        return "/"+ "/".join(stack)