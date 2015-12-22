from BaseSolution import *
class PeekingIterator():
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.back = None
        self.iter = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.back is not None:
            return self.back
        elif self.iter.hasNext():
            self.back = self.iter.next()
            return self.back
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return False
        if self.back is not None:
            val = self.back
            self.back = None
            return val
        else:
            return self.iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.back is None and not self.iter.hasNext():
            return False
        else:
            return True

