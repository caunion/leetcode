__author__ = 'Daoyuan'

from BaseSolution import  *

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

class PalindromeLinkedList(BaseSolution):
    """
    Given a singly linked list, determine if it is a palindrome.

    Easy
    """
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (ListNode.create_from_arr([1,2,3,3,3,2,1]),),
            expects = True
        )
        self.push_test(
            params= (ListNode.create_from_arr([1,2,3,3,2,1]),),
            expects  = True
        )
        self.push_test(
            params = (ListNode.create_from_arr([3,2,1]),),
            expects = False
        )
        self.push_test(
            params = (ListNode.create_from_arr([1]),),
            expects = True
        )
        self.push_test(
            params = (ListNode.create_from_arr([3,3,3,3,3,3,3,3,3]),),
            expects = True
        )
        self.push_test(
            params = (ListNode.create_from_arr([3,3,3,3,3,3,2]),),
            expects = False
        )

    def solution(self, head):
        length = 0
        tmp = head
        while tmp is not None:
            tmp = tmp.next
            length = length + 1

        if length == 0:
            return True
        if length == 1:
            return True

        newhead = ListNode(0)
        newhead.next = None
        prev = newhead
        tmp = head
        for i in xrange( length /2 ):
            back  =tmp.next
            tmp.next = prev
            prev =tmp
            tmp = back

        if length % 2 != 0:
            tmp = tmp.next

        head1 = prev
        head2 = tmp
        for i in xrange( length / 2):
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True