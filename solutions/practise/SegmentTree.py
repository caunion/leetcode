__author__ = 'Daoyuan'
from ..BaseSolution import *
class SegmentTree(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([9,6,7,8,5,4,3,2],[(0,3),(1,5),(1,7),(-1<<30, 2, 0),(-1<<30, 7, 5),(0,3),(1,5),(3,7)]),
            expects = [6,4,2,0,0,3]
        )

    def solution(self, nums, query):
        self.buildTree(nums)
        result = []
        for q in query:
            if len(q) == 2:
                l, r = q
                ret = self.query(l,r,1)
                result.append(ret)
            else:
                _, p, v = q
                self.update(p, v, 1)
        return result


    def buildTree(self, nums):
        n = len(nums)
        minv = [0] * (2*n)
        maxv = [0] * (2*n)
        sumv = [0] * (2*n)
        left = [0] * (2*n)
        right= [0] * (2*n)
        addv = [0] * (2*n)

        for i in xrange(n, 2*n):
            minv[i] = nums[i-n]
            maxv[i] = nums[i-n]
            sumv[i] = nums[i-n]
            left[i] = right[i] = i - n

        height = 0
        while 1<<(height+1) <= n: height += 1
        for h in range(height -1, -1, -1):
            l = 1<<h
            r = 1<<(h+1)
            for i in xrange(l, r):
                if i * 2 < 2*n and i * 2 + 1 < 2*n:
                    minv[i] = min(minv[i*2], minv[i*2+1])
                    maxv[i] = max(maxv[i*2], maxv[i*2+1])
                    sumv[i] = sumv[i*2] + sumv[i*2+1]
                    left[i] = (i - l) * (1<<(height- h))
                    right[i] = (i- l) * (1<<(height- h)) + (1<< (height -h)) -1
        self.maxv = maxv
        self.minv = minv
        self.sumv = sumv
        self.left = left
        self.right = right
        self.addv = addv
        return
    def query(self, L, R, node):
        l = self.left[node]
        r = self.right[node]
        m = ( r - l ) / 2 + l
        ret = 1<<30
        if L <= l and r <= R: return self.minv[node]
        if L <= m:  ret = min(self.query(L, R, node * 2), ret)
        if m+1 <= R: ret = min(self.query(L, R,node*2 + 1), ret)
        return ret

    def update(self, idx, v, node):
        if self.left[node] == self.right[node]:
            self.minv[node] = v
        else:
            m = ( self.right[node] -self.left[node]) / 2 + self.left[node]
            if idx > m:
                self.update(idx, v, node*2+1)
            else:
                self.update(idx, v, node*2)
            self.minv[node] = min(self.minv[node*2], self.minv[node*2+1])

    def updateRange(self, left, right, v, o):
        lc = o * 2
        rc = o*2 +1
        l ,r = self.left[o], self.right[o]
        if (left <= l and r <= right):
            self.addv[o] += v
        else:
            m = (r-l) /2 + l
            if right <= m:
                self.update(left, right, v, lc)
            if left >= m+1:
                self.update(left, right, v, rc)
        self.maintain(o)

    def maintain(self, o):
        l,r = self.left[o], self.right[o]
        lc, rc = o*2, o*2+1
        self.sumv[o] = self.minv[o] = self.max[o] = 0
        if r > l:
            self.sumv[o] = self.sumv[lc] + self.sumv[rc]
            self.minv[o] = min(self.minv[lc], self.minv[rc])
            self.maxv[o] = max(self.maxv[lc], self.maxv[rc])
        self.maxv[o]+= self.addv[o]
        self.minv[o]+= self.addv[o]
        self.sumv[o]+= self.addv[o] * (r-l+1)

    def queryRange(self, left, right, o, add):
        l, r = self.left[o], self.right[o]
        lc, rc = o*2, o*2+1
        if left <= l and r<=right:
            return (self.minv[o] + add, self.maxv[o] + add, self.sumv[o] + add)
        else:
            m = (r-l)/ 2 + l
            maxv = -1<<30
            minv = 1<<30
            sumv = 0
            add += self.addv[o]
            if right <= m:
                a,b,c= self.query(left, right, lc, add)
                maxv = max(maxv, a)
                minv = min(minv, b)
                sumv += c
            if left >= m+1:
                a,b,c= self.query(left, right, rc, add)
                maxv = max(maxv, a)
                minv = min(minv, b)
                sumv += c
            return maxv, minv, sumv