__author__ = 'Daoyuan'
from BaseSolution import *
import math
class SortList(BaseSolution):
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

        @staticmethod
        def create_from_arr(arr):
            if len(arr) <= 0 :
                return None
            tmp = head = SortList.ListNode(arr[0])
            for idx, item in enumerate(arr):
                if idx==0: continue
                tmp.next = SortList.ListNode(item)
                tmp = tmp.next
            return head

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params=SortList.ListNode.create_from_arr( [3,1,2]),
            expects=SortList.ListNode.create_from_arr([1,2,3])
        )
        self.push_test(
            params = SortList.ListNode.create_from_arr(range(9,0,-1)),
            expects = SortList.ListNode.create_from_arr(range(1,10))
        )



    def solution(self, head):
        length = 0
        tmp = head
        while tmp is not None:
            tmp = tmp.next
            length = length+ 1

        for i  in range(0,int(math.floor(math.log(length,2)))):
            leng = length
            step = 2 ** i
            newtail = SortList.ListNode(-1)
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


list1=  SortList.ListNode.create_from_arr(range(9,0,-1))
print list1.toString()

list2 =  SortList.ListNode.create_from_arr([6,7,8,9,2,3,4,5,1])
list3 = list2
while list3.val != 2:
    list3 = list3.next
sort = SortList()
newhead, newtail = sort.merge_list(list2,4,list3,4)
head= sort.solution(list1)

print head.toString()
pass