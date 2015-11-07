from BaseSolution import *
from TreeNode import *
class BinaryTreeZigzagLevelOrderTraversal(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = (TreeNode.deserialize("{3,9,20,#,#,15,7}"),),
            expects = [
                  [3],
                  [20,9],
                  [15,7]
                ]
        )
    def solution(self, root):
        return self.bfs(root)

    def bfs(self, root):
        result = []
        if not root: return result
        childfirst = None
        queue = [ root ]
        ret = []
        reverse = False
        while len(queue) > 0:
            top = queue.pop(0)
            if not top: continue
            if top == childfirst:
                result.append(ret)
                ret = [ top.val ]
                childfirst = None
            else:
                ret.append(top.val)
            if not childfirst:
                childfirst = top.left or top.right
            queue.append(top.left)
            queue.append(top.right)

        result.append(ret)
        for ret in result:
            if reverse:
                ret.reverse()
            reverse = not reverse

        return result

