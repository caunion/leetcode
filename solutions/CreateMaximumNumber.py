from BaseSolution import *
class CreateMaximumNumber(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 9
        self.push_test(
            params = ([0, 1, 0, 1, 1, 2],[0, 1, 0, 0, 1, 2],12),
            expects= [0,1,0,1,1,2,0,1,0,0,1,2]
        )
        self.push_test(
            params = ([5,8,2,7,2,3,1,5,9,5,2,1,5,7,0,3,0,4,4,1,0,7,3,7,5,4,5,1,3,3,8,3,3,7,3,0,2,1,8,4,8,1,0,3,1,3,1,5,3,0,8,0,2,5,0,5,6,4,7,2,6,2,4,0,4,4,1,8,1,4,1,8,2,6,7,3,4,1,1,6,0,4,7,1,8,3,0,2,9,1,6,3,8,5,5,5,0,2,2,1,1,2,1,0,9,6,8,1,0,6,4,3,8,0,0,4,8,3,9,1,9,8,7,2,0,7,6,9,1,7,1,0,0,2,0,7,1,6,2,9,0,3,1,5,6,2,4,8,8,4,5,0,9,7,0,1,0,5,8,1,2,3,5,3,7,6,4,4,4,5,6,7,7,0,0,1,3,1,0,5],
                      [1,6,8,2,3,9,0,9,8,2,1,3,6,6,7,6,0,6,7,5,0,9,3,8,1,9,4,6,7,2,3,5,5,1,0,8],
                      180),
            expects=[9,9,9,9,9,7,7,2,3,5,5,1,0,8,0,3,0,4,4,1,0,7,3,7,5,4,5,1,3,3,8,3,3,7,3,0,2,1,8,4,8,1,0,3,1,3,1,5,3,0,8,0,2,5,0,5,6,4,7,2,6,2,4,0,4,4,1,8,1,4,1,8,2,6,7,3,4,1,1,6,0,4,7,1,8,3,0,2,9,1,6,3,8,5,5,5,0,2,2,1,1,2,1,0,9,6,8,1,0,6,4,3,8,0,0,4,8,3,9,1,9,8,7,2,0,7,6,9,1,7,1,0,0,2,0,7,1,6,2,9,0,3,1,5,6,2,4,8,8,4,5,0,9,7,0,1,0,5,8,1,2,3,5,3,7,6,4,4,4,5,6,7,7,0,0,1,3,1,0,5]
        )
        self.push_test(
            params= ([0, 1, 0, 1, 1, 2, 0, 0, 2, 2, 2, 2, 1, 1, 1, 2, 1, 2, 0, 2, 0, 1, 1, 0, 1, 0, 2, 0, 1],[2, 1, 1, 0, 2, 0, 1, 0, 0, 1, 1, 0, 1, 2, 1, 2, 1, 2, 0, 1, 1, 1, 1, 2, 0, 1, 1, 1, 0],58),
            expects= [2,1,1,0,2,0,1,0,1,1,2,0,1,0,0,2,2,2,2,1,1,1,2,1,2,0,2,0,1,1,0,1,0,2,0,1,0,0,1,1,0,1,2,1,2,1,2,0,1,1,1,1,2,0,1,1,1,0]

        )
        self.push_test(
            params = ([2,1,2,1,2,2,1,2,2,1,1,2,1,0,2,0,1,0,1,1,2,0,0,2,2,2,2,1,1,1,2,1,2,0,2,0,1,1,0,1,0,2,0,1,0,2,0,1,1,0,0,2,0,1,1,2,0,2,2,1,2,1,2,1,0,1,2,0,2,1,2,2,2,0,1,1,0,2,0,1,1,0,0,0,2,1,1,1,0,1,1,0,1,2,1,2,0,0,0,2,1,2,2,1,1,0,1,1,0,0,1,0,0,0,2,1,1,0,2,0,2,2,0,2,0,0,2,0,1,2,1,1,1,2,1,0,1,1,0,2,1,2,2,1,0,1,1,1,2,0,2,2,2,0,2,1,1,2,1,1,2,0,2,1,0,2,0,0,2,2,2,0,2,1,2,2,1,2,1,2,2,2,1,1,2,0,2,0,0,2,2,2,0,2,2,1,0,0,2,2,2,1,1,0,2,1,0,1,2,1,1,2,2,1,1,0,2,1,2,2,1,2,1,0,0,0,0,1,1,0,2,2,2,2,2,2,2,2,1,1,0,2,1,0,0,0,0,2,1,1],
                      [1,1,0,2,0,1,1,1,0,2,2,2,1,1,0,1,2,1,2,1,0,1,2,2,2,2,1,1,0,2,0,1,0,0,1,1,0,1,2,1,2,1,2,0,1,1,1,1,2,0,1,1,1,0,0,1,0,1,2,1,1,0,2,2,1,2,0,2,0,1,1,2,0,1,1,2,2,1,0,1,2,2,0,1,1,2,2,0,2,2,0,2,1,0,0,2,1,0,0,2,1,2,1,2,0,2,0,1,1,2,1,1,1,2,0,2,2,0,2,2,0,2,1,2,1,2,0,2,0,0,1,2,2,2,2,1,2,2,0,1,0,0,2,2,2,2,0,1,0,2,1,2,2,2,1,1,1,1,2,0,0,1,0,0,2,2,1,0,0,1,1,0,0,1,1,0,2,2,2,2,2,1,0,2,2,0,0,1,0,0,1,1,1,2,2,0,0,2,0,0,0,1,2,0,2,0,1,2,0,1,2,0,1,1,0,0,1,2,1,0,2,1,0,1,2,0,1,1,2,1,0,2,1,2,1,1,0,2,2,1,0,2,1,1,1,0,0,0,1,0],
                      500),
            expects=[2,1,2,1,2,2,1,2,2,1,1,2,1,1,1,0,2,0,2,0,1,1,1,0,2,2,2,1,1,0,1,2,1,2,1,0,1,2,2,2,2,1,1,0,2,0,1,0,1,1,2,0,1,0,0,2,2,2,2,1,1,1,2,1,2,0,2,0,1,1,0,1,0,2,0,1,0,2,0,1,1,0,0,2,0,1,1,2,0,2,2,1,2,1,2,1,0,1,2,0,2,1,2,2,2,0,1,1,0,2,0,1,1,0,0,1,1,0,1,2,1,2,1,2,0,1,1,1,1,2,0,1,1,1,0,0,1,0,1,2,1,1,0,2,2,1,2,0,2,0,1,1,2,0,1,1,2,2,1,0,1,2,2,0,1,1,2,2,0,2,2,0,2,1,0,0,2,1,0,0,2,1,2,1,2,0,2,0,1,1,2,1,1,1,2,0,2,2,0,2,2,0,2,1,2,1,2,0,2,0,0,1,2,2,2,2,1,2,2,0,1,0,0,2,2,2,2,0,1,0,2,1,2,2,2,1,1,1,1,2,0,0,1,0,0,2,2,1,0,0,1,1,0,0,1,1,0,2,2,2,2,2,1,0,2,2,0,0,1,0,0,1,1,1,2,2,0,0,2,0,0,0,2,1,1,1,0,1,1,0,1,2,1,2,0,0,0,2,1,2,2,1,1,0,1,1,0,0,1,0,0,0,2,1,1,0,2,0,2,2,0,2,0,0,2,0,1,2,1,1,1,2,1,0,1,1,0,2,1,2,2,1,0,1,1,1,2,0,2,2,2,0,2,1,1,2,1,1,2,0,2,1,0,2,0,0,2,2,2,0,2,1,2,2,1,2,1,2,2,2,1,1,2,0,2,0,0,2,2,2,0,2,2,1,0,0,2,2,2,1,1,0,2,1,0,1,2,1,1,2,2,1,1,0,2,1,2,2,1,2,1,0,0,0,1,2,0,2,0,1,2,0,1,2,0,1,1,0,0,1,2,1,0,2,1,0,1,2,0,1,1,2,1,0,2,1,2,1,1,0,2,2,1,0,2,1,1,1,0,0,0,1,0,0,0,0,1,1,0,2,2,2,2,2,2,2,2,1,1,0,2,1,0,0,0,0,2,1,1,0]
        )
        self.push_test(
            params = ([2,1,7,8,0,1,7,3,5,8,9,0,0,7,0,2,2,7,3,5,5], [2,6,2,0,1,0,5,4,5,5,3,3,3,4], 35),
            expects= [2,6,2,2,1,7,8,0,1,7,3,5,8,9,0,1,0,5,4,5,5,3,3,3,4,0,0,7,0,2,2,7,3,5,5]
        )
        self.push_test(
            params = ([4,3,3,0,6], [2,7,3,8,8,4,1,3,2,5,7,1,4,6,3,6,4,4,0],24),
            expects= [4,3,3,2,7,3,8,8,4,1,3,2,5,7,1,4,6,3,6,4,4,0,6,0]
        )
        self.push_test(
            params = ([4,6,9,1,0,6,3,1,5,2,8,3,8,8,4,7,2,0,7,1,9,9,0,1,5,9,3,9,3,9,7,3,0,8,1,0,9,1,6,8,8,4,4,5,7,5,2,8,2,7,7,7,4,8,5,0,9,6,9,2],
                      [9,9,4,5,1,2,0,9,3,4,6,3,0,9,2,8,8,2,4,8,6,5,4,4,2,9,5,0,7,3,7,5,9,6,6,8,8,0,2,4,2,2,1,6,6,5,3,6,2,9,6,4,5,9,7,8,0,7,2,3],
                      60),
            expects= [9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,6,8,8,4,4,5,7,5,2,8,2,7,7,7,4,8,5,0,9,6,9,2,0,2,4,2,2,1,6,6,5,3,6,2,9,6,4,5,9,7,8,0,7,2,3]
        )
        self.push_test(
            params = ([1,6,5,4,7,3,9,5,3,7,8,4,1,1,4] ,[4,3,1,3,5,9],21),
            expects= [4,3,1,6,5,4,7,3,9,5,3,7,8,4,1,3,5,9,1,1,4]
        )
        self.push_test(
            params = ([2,5,6,4,4,0], [7,3,8,0,6,5,7,6,2], 15),
            expects= [7,3,8,2,5,6,4,4,0,6,5,7,6,2,0]
        )
        self.push_test(
            params = ([6,7], [6,0,4], 5),
            expects= [6,7,6,0,4]
        )
        self.push_test(
            params =( [5,6,8], [6,4,0] ,3),
            expects = [8,6,4]
        )
        self.push_test(
            params = ([3,4,6,5], [9,1,2,5,8,3], 5),
            expects = [9,8,6,5,3]
        )
        self.push_test(
            params = ([9,4,6,5], [9,1,2,5,8,3], 5),
            expects = [9, 9, 8, 6, 5]
        )
    def solution(self, nums1, nums2, k):
        n = len(nums1)
        m = len(nums2)
        arr = [0]
        for i in range(0, k+1):
            j = k - i
            if i > n or j > m: continue
            left = self.maxSingleNumber(nums1, i)
            right = self.maxSingleNumber(nums2, j)
            # merge
            num = self.mergeMax(left, right)
            if self.bigger(num, arr):
                arr = num
        return arr

    def mergeMax(self, left, right, a, b):
        i = len(left)
        j = len(right)
        nums = []
        while a < i and b < j:
            if left[a] > right[b]:
                nums.append(left[a])
                a += 1
            elif left[a] < right[b]:
                nums.append(right[b])
                b += 1
            else:
                c,d = a, b
                step = 0
                while c < i and d < j and left[c] == left[a] and right[b] == right[d]:
                    c += 1
                    d += 1
                e,f = a,b
                while e+1 < i and f+1 < j and left[a:e] == right[b:f]:
                    if step == 0:
                        if left[e+1] > right[f+1]:
                            step = 1
                            break
                        elif left[e+1] < right[f+1]:
                            step = -1
                            break
                        else:
                            step = 0
                        e+=1
                        f+=1
                while c <i and d < j and left[c] > left[a] and right[d] > right[b]:
                    if step == 0:
                        if left[c] > right[d]:
                            step = 1
                        elif left[c] < right[d]:
                            step = -1
                        else:
                            step = 0
                    c += 1
                    d += 1
                if step == 1:
                    nums.extend(left[a:c])
                    a = c
                elif step == -1:
                    nums.extend(right[b:d])
                    b = d
                elif c < i and d < j:
                    if left[c] <= left[a]:
                        nums.extend(right[b:d])
                        b = d
                    elif right[d] <= right[b]:
                        nums.extend(left[a:c])
                        a=c
                elif c > i-1:
                    nums.extend(right[b:d])
                    b = d
                elif d > j-1:
                    nums.extend(left[a:c])
                    a = c
                # nums1 = self.mergeMax(left, right, c, d)
                # nums2 = self.mergeMax(left, right, c, d)
                # if self.bigger(nums1, nums2):
                #     nums.extend(left[a:c])
                #     nums.extend(nums1)
                # else:
                #     nums.extend(right[b:d])
                #     nums.extend(nums2)
                # a = i
                # b = j
        if a < i:
            nums.extend(left[a:])
        if b < j:
            nums.extend(right[b:])
        return nums

    def bigger(self, num1, num2):
        n = len(num1)
        m = len(num2)
        i = j = 0
        if n == 0 and m > 0: return False
        elif m == 0: return True
        while  i < n and num1[i] == 0: i+=1
        while j < m and num2[j] == 0 : j+=1
        if n - i > m-j: return True
        elif n-i < m-j: return False
        else:
            for a,b in zip(range(i, n), range(j,m)):
                if num1[a] > num2[b]: return True
                elif num1[a] < num2[b]: return False
            return True

    def maxSingleNumber(self, nums, i):
        n = len(nums)
        if i > n or i==0 : return []
        ret = [ max(range(0, n-i+1), key = nums.__getitem__) ]
        remains = i - 1
        while remains > 0:
            start = ret[-1] + 1
            end = n-remains + 1
            if start < end:
                ret.append( max(range(start, end), key = nums.__getitem__))
                remains -= 1
            else:
                ret.extend(range(start, n))
                remains -= (n-start)
        ret = [nums[item] for item in ret]
        return ret


    def solution(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def getMax(nums, t):
            ans = []
            size = len(nums)
            for x in range(size):
                while ans and len(ans) + size - x > t and ans[-1] < nums[x]:
                    ans.pop()
                if len(ans) < t:
                    ans += nums[x],
            return ans

        def merge(nums1, nums2):
            ans = []
            while nums1 or nums2:
                if nums1 > nums2:
                    ans += nums1[0],
                    nums1 = nums1[1:]
                else:
                    ans += nums2[0],
                    nums2 = nums2[1:]
            return ans

        len1, len2 = len(nums1), len(nums2)
        res = []
        for x in range(max(0, k - len2), min(k, len1) + 1):
            tmp = merge(getMax(nums1, x), getMax(nums2, k - x))
            res = max(tmp, res)
        return res


    def solution(self, nums1, nums2, k):
        n, m= len(nums1),len(nums2)
        ret = [0] * k
        for i in range(0, k+1):
            j = k - i
            if i > n or j > m: continue
            left = self.maxSingleNumber(nums1, i)
            right = self.maxSingleNumber(nums2, j)
            num = self.mergeMax(left, right)
            ret = max(num, ret)
        return ret


    def mergeMax(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            if nums1 > nums2:
                ans += nums1[0],
                nums1 = nums1[1:]
            else:
                ans += nums2[0],
                nums2 = nums2[1:]
        return ans

    def maxSingleNumber(self, nums, selects):
        n = len(nums)
        ret = [-1]
        if selects > n : return ret
        while selects > 0:
            start = ret[-1] + 1 #search start
            end = n-selects + 1 #search end
            ret.append( max(range(start, end), key = nums.__getitem__))
            selects -= 1
        ret = [nums[item] for item in ret[1:]]
        return ret