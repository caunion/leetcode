__author__ = 'Daoyuan'

from ..BaseSolution import *

class Node(object):

    def __init__(self, weight =-1):
        self.left = None
        self.right = None
        self.weight = weight
        self.leftdist = -1
        self.rightdist = -1


class UVa839NotSoMobile(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([
                [1],
                [0,2,0,4],
                [0,3,0,1],
                [1,1,1,1],
                [2,4,4,2],
                [1,6,3,2]
                      ],),
            expects = "Yes"
        )
        self.push_test(
            params = ([
                [1],
                [0,5,0,6],
                [0,1,0,1],
                [0,1,0,1],
                [3,4,3,4],
                [4,1,2,2],
                [7,5,5,7],
                [0,2,0,2],
                [5,3,5,3],
                [8,3,2,12]
                      ],),
            expects = "Yes"
        )
        self.push_test(
            params = ([
                [1],
                [0,2,0,4],
                [0,3,0,1],
                [1,2,1,1],
                [2,4,4,2],
                [1,6,3,2]
                      ],),
            expects = "No"
        )

    def solution2(self, params):
        n = params[0][0]
        root = self.buildTree(params,[1])
        weight = self.dfs(root)
        if weight > 0:
            return "Yes"
        else:
            return "No"

    def solution(self, params):
        n = params[0][0]
        weight = self.solve(params, [1])
        if weight > 0:
            return "Yes"
        else:
            return "No"

    def solve(self,matrix, idx):
        WL, DL, WR, DR =  matrix[idx[0]]
        if WL > 0 and WR > 0:
            if WL*DL == WR*DR: return WL+WR
            else: return  -1
        leftweight = 0
        rightweight = 0
        if WL == 0:
            idx[0] = idx[0] + 1
            leftweight = self.solve(matrix, idx)
        if WR == 0:
            idx[0] = idx[0] + 1
            rightweight = self.solve(matrix, idx)

        if leftweight < 0 or\
            rightweight < 0 or\
            leftweight * DL != rightweight * DR:
                return -1
        else: return leftweight + rightweight

    def dfs(self, root):
        if root.left is None and root.right is None:
            return root.weight

        leftweight = self.dfs(root.left)
        rightweight = self.dfs(root.right)
        if leftweight < 0 or rightweight< 0 or root.leftdist * leftweight != root.rightdist * rightweight:
            return -1
        else:
            return leftweight+rightweight



    def buildTree(self, matrix, idx):
        i = idx[0]
        WL, DL, WR, DR = matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3]
        root = Node()
        root.leftdist = DL
        root.rightdist = DR
        if WL == 0 and WR ==0:
            idx[0] = idx[0]+1
            root.left = self.buildTree(matrix, idx)
            idx[0] = idx[0]+1
            root.right= self.buildTree(matrix, idx)
        else:
            root.left = Node(WL)
            root.right = Node(WR)
        return root