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

class MergeTwoSortedLists(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (
                [],
                None),
            expect_oneof = [[],None]
        )
        self.push_test(
            params = (
                [],
                []
                      ),
            expect_oneof = [[],None]
        )
        self.push_test(
            params = (
                ListNode.create_from_arr([]),
                ListNode.create_from_arr([1,2,3,5,6,7])
                      ),
            expects = ListNode.create_from_arr([1,2,3,5,6,7])
        )
        self.push_test(
            params = (
                ListNode.create_from_arr([1,2,3,5,6,7]),
                ListNode.create_from_arr([])
                      ),
            expects = ListNode.create_from_arr([1,2,3,5,6,7])
        )
        self.push_test(
            params = (
                ListNode.create_from_arr(range(1,20, 2)),
                ListNode.create_from_arr(range(0,20,2))
                      ),
            expects = ListNode.create_from_arr(range(0,20))
        )

    def solution(self, l1, l2):
        head = temp = None
        if l1 is None or l1 == []:
            head = temp = l2
            return head
        if l2 is None or l2 == []:
            head = temp = l1
            return head

        while True:
            if l1 is None or l1 == [] or\
                    l2 is None or l2 == []:
                break
            if l1.val > l2.val:
                l1, l2 = l2, l1
            if head is None:
                head = temp = l1
            else:
                temp.next =l1
                temp = l1
            l1 = l1.next

        while l2 is not None and l2 != []:
            temp.next = l2
            temp = l2
            l2 = l2.next
        return head