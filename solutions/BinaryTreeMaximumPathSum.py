__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class BinaryTreeMaximumPathSum(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 9
        self.push_test(
            params = (TreeNode.deserialize("[-633,-237,447,-740,149,-264,-314,-484,-938,706,-483,-542,575,132,101,-220,-805,-43,null,371,318,-294,-611,-236,152,-171,398,598,531,null,-181,11,null,-643,577,735,-409,163,178,-879,-929,936,-658,826,461,-55,-579,null,null,null,null,-384,974,426,-899,-476,83,-900,-929,661,null,11,986,null,null,-194,-840,991,75,-662,null,-3,null,null,null,-906,null,716,-479,-895,902,null,null,-507,null,-695,null,null,null,424,33,null,-556,-312,null,-916,null,617,null,-623,110,null,null,null,null,-309,118,null,null,-128,-899,12,561,-163,869,-501,-811,308,979,null,846,-860,7,null,null,-782,null,null,-754,100,null,null,null,null,null,null,null,707,504,800,-59,null,null,null,null,302,null,399,null,null,null,null,null,null,null,-328,null,289,-81,null,-241,-266,null,null,507,-363,null,94,null,-891,null,969,-339,146,null,-520,null,null,null,null,null,null,null,-718,null,206,null,null,null,null,null,-509,-678,null,null,null,-838,null,null,null,null,-398,null,-630,618,-879,620,null,-606,-387,-275,null,129,490,-312,813,650,-296,-970,481,-271,null,-118,null,-822,null,null,null,null,null,null,-369,-453,null,null,490,null,null,-517,131,-264,null,null,null,null,551,978,null,null,532,-181,531,null,638,null,-447,-705,4,-506,null,278,null,null,null,56,null,null,425,237,null,462,39,null,546,766,-164,-102,null,null,-497,267,null,null,-238,483,null,null,773,388,-195,305,null,null,null,null,null,null,null,null,null,null,-742,null,-507,null,null,null,null,null,null,null,null,null,null,null,null,null,197,null,null,-72,null,null,null,null,null,null,null,-933,null,-749,-594,null,null,null,-569,127,-321,null,-391,null,230,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,-341,-527,null,null,122,146,null,null,null,-236,-332,null,null,-812,null,null,114,null,null,-549,null,152,146,null,-842,null,448,977,null,null,null,97]"),),
            expects = 3979
        )
        self.push_test(
            params = (TreeNode.deserialize("{1,-2,-3,1,3,-2,#,-1}"),),
            expects = 3
        )
        self.push_test(
            params = (TreeNode.deserialize("{-3}"),),
            expects= -3
        )
        self.push_test(
            params = (TreeNode.deserialize("{-3,-2,-1,-3,-4,-5,-6}"),),
            expects= -1
        )
        self.push_test(
            params= (TreeNode.deserialize("{-2,-1,-2,1,2,#,#,#,#,-1}"),),
            expects =  2
        )
        self.push_test(
            params = (TreeNode.deserialize("{2,-1}"),),
            expects = 2
        )
        self.push_test(
            params = (TreeNode.deserialize("{1,2,3,4,5,#,#,8,9,500,2000,10,#,11,#,12,13,14,15}"),),
            expects = 2533
        )
        self.push_test(
            params = (TreeNode.deserialize("{1,2,3}"),),
            expects = 6
        )

    def solution(self, root):
        ret = 0
        if root is None: return ret

        self.maxv = -1e9
        self.last = None
        self.addParent(root, None)
        self.dfs_recurssive(root,0, -1e9, None)
        #self.last.left, self.last.right = None, None
        newroot = self.reverse_tree(self.last)
        self.maxv = -1e9
        self.dfs_recurssive(newroot,0, -1e9, None)
        return self.maxv

    def addParent(self, node, parent):
        if node is not None:
            node.parent = parent
        if node.left: self.addParent(node.left, node)
        if node.right: self.addParent(node.right, node)

    def dfs_recurssive(self, root, total, max_local, last_local):
        if root is None: return 0
        temp = total + root.val
        if temp < 0: temp = root.val
        if temp > max_local:
            last_local = root
            max_local = temp
        if not root.left and not root.right and max_local > self.maxv:
            self.last = last_local
            self.maxv = max_local
            return
        if temp < 0: temp = 0
        if root.left:
            self.dfs_recurssive(root.left, temp, max_local, last_local)
        if root.right:
            self.dfs_recurssive(root.right, temp, max_local, last_local)

    def reverse_tree(self, last):
        root = last
        parent = last.parent
        while parent is not None:
            if parent.left == last:
                parent.left = None
            else:
                parent.right = None

            temp = parent.parent
            parent.parent = last
            if not last.left: last.left = parent
            else: last.right = parent
            last = parent
            parent = temp
        return root

    def solution(self, root):
        return self.dfs(root)[1]

    def dfs(self, root):
        l = r = 0
        ls = rs = -1e9
        if not root: return 0
        if root.left:
            l, ls = self.dfs(root.left)
            l = max(0,l)
        if root.right:
            r, rs = self.dfs(root.right)
            r = max(0,r)
        return max(root.val+l, root.val+r), max(root.val + l + r, ls, rs)

    def solution(self, root):
        if not root:
            return 0
        self.maxpathsum = -(1<<31)
        def getmaxsum(node):
            if not node: return 0
            leftmax = max(0, getmaxsum(node.left) )
            rightmax = max(0, getmaxsum(node.right))
            self.maxpathsum = max(self.maxpathsum, node.val + leftmax + rightmax)
            return max(node.val, node.val + leftmax, node.val + rightmax)

        getmaxsum(root)
        return self.maxpathsum
