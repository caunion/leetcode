__author__ = 'Daoyuan'
from BaseSolution import *
import math
import random
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

class SortList(BaseSolution):
    """
    Sort a linked list in O(n log n) time using constant space complexity.
    :url: https://leetcode.com/problems/sort-list/
    :time: +2hours
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params= ( ListNode.create_from_arr( [3,1,2]), ),
            expects= ListNode.create_from_arr([1,2,3])
        )
        self.push_test(
            params = (ListNode.create_from_arr(range(9,0,-1)),),
            expects = ListNode.create_from_arr(range(1,10))
        )
        rand = []
        for i in range(20):
            rand.append(random.randint(0,39))
        self.push_test(
            params = (ListNode.create_from_arr(rand), ),
            expects = sorted(rand)
        )


    def solution(self, head):
        length = 0
        tmp = head
        while tmp is not None:
            tmp = tmp.next
            length = length+ 1

        for i  in range(0,self.log2(length)):
            leng = length
            step = 2 ** i
            newtail = ListNode(-1)
            newtail.next = head
            lasttail = None
            while leng > 0:
                len1 = len2 = step
                if leng - len1 <= 0 : break
                if leng - len1 -len2 < 0: len2 = leng-len1
                head2 = head1 = newtail.next
                for j in range(len1):
                    head2 = head2.next
                newhead, newtail = self.merge_list(head1, len1, head2, len2)
                if lasttail is not None:
                    lasttail.next = newhead

                lasttail = newtail
                if leng == length:
                    head = newhead
                leng = leng -len2 - len1
        return head

    def log2(self, num):
        ret = 0
        while num > 0:
            ret = ret+1
            num = num>>1
        return ret

    def merge_list(self, head1, len1, head2, len2):
        if head1 is None:
            return None, None
        oldtail =  head2
        for i in range(len2):
            oldtail = oldtail.next
        idx1 = idx2 =0
        newhead = ptr1 = head1
        ptr2 = head2
        prev1 = None
        while idx2 < len2:
            while idx1 < len1 and ptr1.val <= ptr2.val:
                idx1 = idx1+1
                prev1 = ptr1
                ptr1 = ptr1.next

            if prev1 is not None:
                prev1.next = ptr2
                ptr2 = ptr2.next
                prev1.next.next=ptr1
                prev1 = prev1.next
            else:
                tmp2 = ptr2.next
                ptr2.next = ptr1
                prev1 = ptr2
                ptr2 = tmp2
                newhead= prev1
            idx2 = idx2+1

        newtail = newhead
        for i in range(len1+len2-1):
            newtail = newtail.next
        newtail.next= oldtail
        return newhead, newtail