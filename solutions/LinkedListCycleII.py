from BaseSolution import *
from ListNode import *
class LinkedListCycleII(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)

        head = ListNode.create_from_arr([0,1,2,3,4])
        top = head
        start = head
        k = 2
        for i in range(0, k+1):
            top = top.next
            start = start.next
        while top.next:
            top = top.next
        top.next = start

        self.push_test(
            params = (head,),
            expects = start
        )

    def solution(self, head):
        visited = set()
        if not self.hasCycle(head): return None
        newHead = ListNode(-1)
        newHead.next =head
        while newHead is not None:
            key = hash(newHead)
            if key in visited:
                break
            else:
                visited.add(key)
            newHead = newHead.next
        return newHead

    def hasCycle(self, head):
        if not head: return False
        newHead = ListNode(-1)
        newHead.next = head
        slow = newHead
        fast = newHead.next
        while slow and fast and fast.next:
            if hash(slow) == hash(fast): return slow
            slow = slow.next
            fast = fast.next.next
        return False

    def solution(self, head):
        headB = self.hasCycle(head)
        if not headB: return None
        headA = head
        stop = headB
        l1, l2 = 1,1
        h1, h2 = headA, headB

        while not hash(h1) == hash(stop):
            h1 =h1.next
            l1 += 1
        h2 = h2.next
        l2 = 2
        while not hash(h2) == hash(stop):
            h2 = h2.next
            l2 += 1
        if l1 < l2:
            l1, l2 = l2, l1
            headA, headB = headB, headA
        for i in xrange(l1-l2):
            headA =headA.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA