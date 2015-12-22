from BaseSolution import *
class ImplementstrStr(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ("abcdededefgdeddfg", "dedefg"),
            expects= 5
        )
        self.push_test(
            params = ("abcdededefgdededdfgabcdededefgdefdeddfg", "dedefgdef"),
            expects= len("abcdededefgdededdfgabcde")
        )
    def solution(self, haystack, needle):
        if len(needle) == 0: return 0
        n = len(haystack)
        m = len(needle)
        for i in range(0, n):
            if n - i < m: return -1
            if haystack[i] == needle[0]:
                match =  True
                for j in range(1, m):
                    if haystack[i+j] != needle[j]:
                        match = False
                        break
                if match:
                    return i
        return -1

    ## KMP method
    ## it's odd as the KMP method is slower than brutal method (previous one)
    ## in leet code test cases
    def solution(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)==0: return 0
        haystack = " " + haystack
        m = len(needle)
        n = len(haystack)
        needle = " " + needle
        f = self.prefixFunc(needle)
        j = 0
        for i in range(1, n):
            while j > 0 and haystack[i] != needle[j+1]:
                j = f[j]
            if haystack[i] == needle[j+1]:
                j += 1
            if j == m:
                return i-m
        return -1
    def prefixFunc(self, pattern):
        n = len(pattern)
        f = [0] * n
        f[1] = 0
        j = 0
        for i in range(2, n):
            while j > 0 and pattern[j+1] != pattern[i]:
                j = f[j]
            if pattern[j+1] == pattern[i]:
                j += 1
            f[i] = j
        return f