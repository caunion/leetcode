from BaseSolution import *
class item(object):
    def __init__(self, key, time = 0):
        self.key = key
        self.time = time
        self.position = -1
    def __gt__(self, other):
        return self.time > other.time

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.heap = []
        self.limit = capacity
    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dic:
            self.heap.remove(key)
            self.heap.append(key)
            return self.dic[key]
        else:
            return None

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if len(self.heap) == self.limit:
            remove = self.heap.pop(0)
            del self.dic[remove]
        self.heap.append(key)
        self.dic[key] = value

class LRUCacheTest(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (3, [(0,'a', 1),(0,'b', 2),(0,'c', 3),(1,'a'),(0,'d', 4),(1,'b'), (1,'c'), (0,'e', 5),(1,'a'),(1,'d')],),
            expects = [1, None, 3, None, 4]
        )
    def solution(self, limit, ops):
        cache = LRUCache(limit)
        result = []
        for op in ops:
            if op[0] == 0:
                cache.set(op[1], op[2])
            elif op[0] == 1:
                result += cache.get(op[1]),
        return result