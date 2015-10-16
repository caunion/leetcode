__author__ = 'Daoyuan'

from BaseSolution import *

class CourseScheduleI(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test((2,[[1,0]]), True )
        self.push_test((2, [[1,0],[0,1]]), False)

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

        return sum(prev) == 0