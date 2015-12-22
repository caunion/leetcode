__author__ = 'Daoyuan'
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def toString(self):
        tmp = self
        ret =  ""
        start = self.findCycleStart(self)
        meet = 0
        while tmp:
            if tmp == start and meet > 0:
                ret += " --cycle--> %d" % tmp.val
                break
            if tmp == start:
                meet += 1
            ret = ret + ' ' + str(tmp.val)
            tmp = tmp.next
        ret.strip()
        return ret
    def __str__(self):
        return ""
        ret = []
        tmp = self
        start = self.findCycleStart(self)
        meet = 0
        while tmp:
            if tmp == start and meet > 0:
                break
            if tmp == start:
                meet += 1
            ret.append(tmp.val)
            tmp = tmp.next
        return ret.__str__()

    def __eq__(self, other):
        if self.__str__() == other or \
            type(other) == ListNode and self.toString() == other.toString():
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

    def hasCycle(self, head):
        if not head: return False
        newHead = ListNode(-1)
        newHead.next = head
        slow = newHead
        fast = newHead.next
        while slow and fast and fast.next:
            if slow == fast: return slow
            slow = slow.next
            fast = fast.next.next
        return False

    def findCycleStart(self, head):
        headB = self.hasCycle(head)
        if not headB: return None
        headA = head
        stop = headB
        l1, l2 = 1,1
        h1, h2 = headA, headB

        while not h1 == stop:
            h1 =h1.next
            l1 += 1
        h2 = h2.next
        l2 = 2
        while not h2 == stop:
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