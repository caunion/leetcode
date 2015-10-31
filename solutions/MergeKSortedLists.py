__author__ = 'Daoyuan'
from BaseSolution import *

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def toString(self):
        tmp = self
        ret =  ""
        while tmp is not None:
            ret = ret + ' ' + str(tmp.val)
            tmp = tmp.next
        ret.strip()
        return ret
    def __str__(self):
        ret = []
        tmp = self
        while tmp is not None:
            ret.append(tmp.val)
            tmp = tmp.next
        return ret.__str__()

    def __eq__(self, other):
        if self.__str__() == other or type(other) == ListNode and self.__str__() == other.__str__():
            return True
        else:
            return False

    @staticmethod
    def create_from_arr(arr):
        if len(arr) <= 0 :
            return None
        tmp = head = ListNode(arr[0])
        for idx, item in enumerate(arr):
            if idx==0: continue
            tmp.next = ListNode(item)
            tmp = tmp.next
        return head

class MergeKSortedLists(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([
                          [],
                          ListNode.create_from_arr([-1,5,11]),
                          [],
                          ListNode.create_from_arr([6,10])
                      ],),
            expects = ListNode.create_from_arr([-1,5,6,10,11])
        )
        self.push_test(
            params = ([[],[]],),
            expects = []
        )
        self.push_test(
            params = ([ [] ],),
            expects = []
        )
        self.push_test(
            params = ([],),
            expects = []
        )
        self.push_test(
            params = ([
                ListNode.create_from_arr(range(0,10,3)),
                [],
                [],
                [],
                ListNode.create_from_arr(range(2,10,3)),
                [],
                ListNode.create_from_arr(range(1,10,3))
                ],),
            expects = ListNode.create_from_arr(range(0,10))
        )

    def solution(self, lists):
        length = len(lists)
        if length == 0:
            return  []
        ret = lists
        while length > 1:
            ret = []
            lens = []
            length = len(lists)
            for i in range(0, self.ceil(length / 2.0)):
                if i <  length/ 2:
                    left = lists[i]
                    right = lists[length - 1 - i]
                    count, head = self.merge2list(left, right)
                else:
                    count = 0
                    head =temp= lists[i]
                    while temp is not None and temp != []:
                        temp = temp.next
                        count = count + 1
                if count>0:
                        lens.append(count)
                        ret.append(head)
            lists = ret
            length = len(ret)
        if length == 0: return []
        return ret[0]

    def merge2list(self, left, right):
        count = 0
        head = temp = None
        if right is None or right == []:
            left, right = right, left

        while True:
            if left is None or left == [] or \
                            right is None or right == []:
                break
            if left.val > right.val:
                left, right = right, left
            if head is None and count == 0:
                head = temp = left
                count = 1
            else:
                temp.next = left
                temp = temp.next
                count = count + 1
            left = left.next

        while right is not None and right != []:
            if temp is None:
                head = temp = right
            else:
                temp.next = right
                temp = right
            right = right.next
            count = count + 1
        return count, head

    def ceil(self, num):
        epsi = 0.00001
        if abs(num  - int(num)) > epsi:
            return int(num+1)
        else:
            return int(num)
