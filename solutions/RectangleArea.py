from BaseSolution import *
class RectangleArea(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (0,0,0,0,-1,-1,1,1),
            expects= 4
        )

    def solution(self, A, B, C, D, E, F, G, H):
        s1 = (D-B) * (C-A)
        s2 = (H-F) * (G-E)
        w =  min(C,G) - max(A,E)
        h =  min(D,H) - max(B, F)
        if w <= 0 or h <=0: return 0 + s1 + s2
        else: return s1 + s2 - w * h
