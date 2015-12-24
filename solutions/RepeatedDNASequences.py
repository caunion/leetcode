from BaseSolution import *
class RepeatedDNASequences(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("AAAAAAAAAAAA",),
            expects= ["AAAAAAAAAA"]
        )
        self.push_test(
            params = ("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",),
            expects= ["AAAAACCCCC", "CCCCCAAAAA"]
        )

    def solution(self, s):
        i, n, l = 0, len(s), 10
        result = []
        buf = {}
        map = {'A':0, 'C':1, 'G':2, 'T':3}
        if n <= l : return []
        sect = s[0:l]
        val = 0
        for c in sect:
            val = val * 4 + map[c]
        buf[val] = 1
        for i in range(1, n - l+1):
            val = val - map[sect[0]] * (4**9)
            val = val * 4 + map[s[i+l-1]]
            sect = s[i:i+l]
            if val in buf:
                if buf[val] == 1:
                    result.append(sect)
                buf[val] += 1
            else:
                buf[val] = 1
        return result

    def solution(self, s):
        i, n, l = 0, len(s), 10
        seen, result = set(), set()
        for i in range(n - l + 1):
            sub = s[i:i+l]
            key = hash(sub)
            if key in seen:
                result.add(sub)
            else:
                seen.add(key)
        return result