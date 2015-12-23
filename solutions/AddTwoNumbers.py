from BaseSolution import *
from ListNode import *
class AddTwoNumbers(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (ListNode.create_from_arr([2,6,4]), ListNode.create_from_arr([5,4,5])),
            expects = ListNode.create_from_arr([7,0,0,1])
        )

    def solution(self, l1, l2):
        len1 = len2 = 0
        head1, head2 = l1, l2
        while head1:
            len1 += 1
            head1 = head1.next
        while head2:
            len2 += 1
            head2 = head2.next
        if len1 < len2:
            head1, head2 =l2,l1
            len1, len2 = len2, len1
            l1,l2 =l2,l1
        else:
            head1, head2 = l1, l2

        tail = None
        prev = next = 0

        while head1:
            if not head2:
                v2 = 0
            else:
                v2 = head2.val
            next = (head1.val + v2 + prev) / 10
            head1.val = (head1.val + v2 + prev) % 10

            tail = head1
            head1 = head1.next
            if head2:
                head2 = head2.next
            prev = next

        if prev > 0:
            tail.next = ListNode(prev)

        return l1