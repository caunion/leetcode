__author__ = 'Daoyuan'
from ..BaseSolution import *
class UVa10305OrderingTasks(BaseSolution):


    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([
                "5 5",
                "3 5",
                "1 3",
                "5 2",
                "4 5",
                "4 2",
                "0 0"
            ],)
        )

    def solution(self, params):
        idx = 0
        result = []
        while True:
            n, m = (int(item) for item in params[idx].split(' '))
            if n == 0 and m == 0: break
            maxn = 100
            indegree = [0] * n
            graph = [[] for i in xrange(n)]
            dictionary = {}
            reindex = [0] * n
            index = 0
            for i in range(idx+1, idx+m+1):
                left, right = (int(item) for item in params[i].split(' '))
                if not dictionary.has_key(left):
                    dictionary[left] = index
                    reindex[index] = left
                    index = index + 1
                if not dictionary.has_key(right):
                    dictionary[right] = index
                    reindex[index] =right
                    index = index + 1
                left = dictionary[left]
                right = dictionary[right]
                graph[left].append(right)
                indegree[right] = indegree[right] + 1

            queue = []
            for i in range(0, n):
                if indegree[i] == 0:
                    queue.append(i)

            ret = []
            while queue.__len__() > 0:
                top = queue.pop(0)
                ret.append(reindex[top])
                for right in graph[top]:
                    indegree[right] = indegree[right] - 1
                    if indegree[right] == 0:
                        queue.append(right)
            result.append(ret)
            idx = idx + m + 1
        return result

