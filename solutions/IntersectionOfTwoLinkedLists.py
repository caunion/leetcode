from BaseSolution import *
from ListNode import *
class IntersectionOfTwoLinkedLists(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, headA, headB):
        if not headA or not headB: return None
        h1, h2 = headA, headB
        lenA = 1
        lenB = 1
        while h1:
            h1 = h1.next
            lenA += 1
        while h2:
            h2 = h2.next
            lenB += 1
        if lenB > lenA:
            lenB, lenA = lenA, lenB
            headB, headA = headA, headB
        diff = lenA - lenB
        for i in range(0, diff):
            headA = headA.next
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        return headA

