__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *


class Codec:
    def serialize(self, root):
        null = "null"
        ret = []
        queue = [root]
        while len(queue) > 0:
            top= queue.pop(0)
            if top is None:
                ret += [null,]
                continue
            else:
                ret += [str(top.val),]
            queue.append(top.left)
            queue.append(top.right)
        while len(ret) > 0 and ret[-1] == null:
            ret.pop()
        return "["+ ",".join(ret) + "]"

    def deserialize(self, data):
        if data[0] == "[" or data[0] == "{":
            data = data[1:-1]
        data = data.split(",")
        if len(data) == 0 or data[0] == "": return None
        root = TreeNode( int(data[0]) )
        queue = [root]
        i = 1
        while len(queue) > 0 and i < len(data):
            top =queue.pop(0)
            if data[i] != "null" and data[i] != "#":
                node = TreeNode(int(data[i]))
                queue.append(node)
            else:
                node = None
            top.left = node
            i += 1
            if len(data) == i: break
            if data[i] != "null" and data[i] != "#":
                node = TreeNode(int(data[i]))
                queue.append(node)
            else:
                node = None
            top.right = node
            i+=1
        return root
class SerializeAndDeserializeBinaryTree(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        tree = TreeNode.deserialize("[]")
        data = "[]"
        self.push_test(
            params = (tree,data),
            expects = (data, tree)
        )

    def solution(self, tree, data):
        c = Codec()
        t = c.deserialize(data)
        return (c.serialize(tree), c.deserialize(data))
