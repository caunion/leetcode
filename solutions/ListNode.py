__author__ = 'Daoyuan'
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