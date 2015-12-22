from BaseSolution import *
class Heap():
    def __init__(self, type=0):
        self.type = type
        self.count = 0
        self.data = [ -1 ]
        self.inf = 1<<30
    def insert(self, x):
        self.count += 1
        if self.count < len(self.data):
            self.data[self.count] = x
        else:
            self.data.append(x)
        i = self.count
        while i >1:
            if self.type == 0:
                if self.data[i] < self.data[i/2]:
                    self.data[i], self.data[i/2] = self.data[i/2], self.data[i]
                else:
                    break
            else:
                if self.data[i] > self.data[i/2]:
                    self.data[i], self.data[i/2] = self.data[i/2], self.data[i]
                else:
                    break
            i = i/2
    def delete(self, index):
        if self.count == 0 or index > self.count:
            return None
        ret = self.data[index]
        self.data[index]  = self.data[self.count]
        self.data[self.count] = -1
        self.count -= 1
        i = index
        while i * 2 <= self.count and i*2+1 <= self.count:
            if self.type == 0:
                if self.data[i] > min(self.data[i*2], self.data[i*2+1]):
                    if self.data[i*2] < self.data[i*2+1]:
                        self.data[i],self.data[i*2] = self.data[i*2], self.data[i]
                        i= i*2
                    else:
                        self.data[i], self.data[i*2+1] = self.data[i*2+1], self.data[i]
                        i = i*2 + 1
                else:
                    break
            else:
                if self.data[i] < max(self.data[i*2], self.data[i*2+1]):
                    if self.data[i*2] > self.data[i*2+1]:
                        self.data[i], self.data[i*2] = self.data[i*2], self.data[i]
                        i = i*2
                    else:
                        self.data[i], self.data[i*2+1] = self.data[i*2+1], self.data[i]
                        i = i*2+1
                else:
                    break

        if i*2 <= self.count:
            if self.type ==0 and self.data[i] > self.data[i*2] or \
               self.type == 1 and self.data[i] < self.data[i*2]:
                self.data[i], self.data[i*2] = self.data[i*2], self.data[i]
        return ret
    def peek(self):
        if self.count> 0:
            return self.data[1]
        else:
            return None

    def size(self):
        return self.count

    def extract(self):
        if self.count == 0:
            return None
        value = self.peek()
        self.delete(1)
        return value
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxheap = Heap(1)
        self.minheap = Heap(0)
        self.heaps = [self.maxheap, self.minheap]
        self.i = 0
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # if self.minheap.count == 0:
        #     self.minheap.insert(num)
        # elif num > self.minheap.peek():
        #     if self.minheap.count > self.maxheap.count:
        #         top = self.minheap.extract()
        #         self.maxheap.insert(top)
        #     self.minheap.insert(num)
        # else:
        #     if self.minheap.count <= self.maxheap.count:
        #         top = self.maxheap.extract()
        #         self.minheap.insert(top)
        #     self.maxheap.insert(num)
        # if self.minheap.count > 0 and self.maxheap.count>0 and self.minheap.peek() < self.maxheap.peek():
        #     top1, top2 = self.minheap.extract(), self.maxheap.extract()
        #     self.minheap.insert(top2)
        #     self.maxheap.insert(top1)

        # self.minheap.insert(num)
        # self.maxheap.insert( self.minheap.extract() )
        # if self.minheap.count < self.maxheap.count:
        #     self.minheap.insert(self.maxheap.extract())

        i = self.i
        self.heaps[i].insert(num)
        self.heaps[i^1].insert( self.heaps[i].extract() )
        self.i ^= 1
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.minheap.count == self.maxheap.count and self.minheap.count > 0:
            maxv = self.minheap.peek()
            minv = self.maxheap.peek()
            return (maxv+minv)/2.0
        elif self.minheap.count > self.maxheap.count and self.minheap.count > 0:
            return self.minheap.peek() * 1.0
        else:
            return None

import bisect
## The second solution, utilize bisect
## with O(n) addNum and O(1) findMedian operation.
## despite the worse therotical complexity than previous one (using max and min heaps, O(logn)
# addNum and O(1) findMedian), the run-time on leetcode is much better. i.e. faster than 80%
## submissions. The two-heap methods only faster than 3% submissions...
## BISECT is essentially a binary search.
class MedianFinder2():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def addNum(self, num):
        bisect.insort(self.data, num)

    def findMedian(self):
        n = len(self.data)
        if n == 0: return None
        n = n/ 2
        return (self.data[n] + self.data[~n]) /2.0

class FindMedianFromDataStream(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([(0,12),(1, None),(0,10),(1, None),(0,13),(1, None),],),
            expects=[12.00000,11.00000,12.00000]
        )
        self.push_test(
            params = ([(0,6),(1, None),(0,10),(1, None),(0,2),(1, None),(0,6),(1, None),(0,5),(1, None),(0,0),(1, None),(0,6),(1, None),(0,3),(1, None),(0,1),(1, None),(0,0),(1, None),(0,0),(1, None)],),
            expects= [6.00000,8.00000,6.00000,6.00000,6.00000,5.50000,6.00000,5.50000,5.00000,4.00000,3.00000]
        )
        self.push_test(
            params = ([(0,1),(0,2),(0,2),(0,2),(0,4),(0,3),(0,5),(0,6),(0,7),(1,None),(0,3),(1,None),(0,1),(0,1), (1, None)],),
            expects = [3, 3.0, 2.5]
        )
        self.push_test(
            params = ([(0,1),(0,2),(1,None),(0,3),(1,None)],),
            expects = [1.5,2]
        )

    def solution(self, ops):
        minheap = Heap(0)
        for i in [9,5,4,3,4,3,8,3,2,2,1]:
            minheap.insert(i)
        a=[]
        for i in range(0,minheap.count+1):
            a+= minheap.delete(1),
        result = []
        med = MedianFinder()
        for op in ops:
            if op[0] == 0:
                med.addNum(op[1])
            elif op[0] == 1:
                result.append(med.findMedian())
        return result
