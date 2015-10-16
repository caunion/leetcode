__author__ = 'Caunion'
from BaseSolution import *

class CourseScheduleII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test((2,[[1,0]]), [0,1] )
        self.push_test((4, [[1,0],[2,0],[3,1],[3,2]]), ([0,2,1,3],[0,1,2,3]), True)

    def solution(self, numCourses, prerequisites):
        next = []
        prev = []
        for item in range(0, numCourses):
            next.append([])
            prev.append(0)

        for item in prerequisites:
            req = item[1]
            suc = item[0]
            next[req].append(suc)
            prev[suc] = prev[suc]+1

        result = []
        iterlist = []
        for i in range(0, numCourses):
            if prev[i] == 0:
                iterlist.append(i)

        while len(iterlist) > 0:
            course = iterlist.pop()
            result.append(course)
            for suc in next[course]:
                prev[suc] = prev[suc]-1
                if prev[suc] == 0:
                    iterlist.append(suc)

        if sum(prev) == 0:
            return result
        else:
            return []