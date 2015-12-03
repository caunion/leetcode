__author__ = 'Daoyuan'
from BaseSolution import *
class DeleteNodeInALinkedList(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)

    def solution(self, node):
        node.val = node.next.val
        node.next = node.next.next