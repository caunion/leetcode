__author__ = 'Daoyuan'
from BaseSolution import *
from TreeNode import *
class RemoveInvalidParentheses(BaseSolution):
    def __init__(self):
        BaseSolution.__init__(self)
        self.fuckinglevel = 9
        self.push_test(
            params = (")()m)(((()((()((((",),
            expects =["()m(())","()m()()","(m)(())","(m)()()"],
            expect_unordered= True
        )
        self.push_test(
            params = ("())(((()m)(",),
            expects = ["()(()m)"]
        )
        self.push_test(
            params = ("nf))f)ddd(d(f(",),
            expects = ["nffddddf"]
        )
        self.push_test(
            params = ("()())((())()))",),
            expects = ["()()((())())","()()((()()))","()(((())()))","(())((())())","(())((()()))","(()((())()))"],
            expect_unordered= True
        )
        self.push_test(
            params = ("()())()",),
            expects = ["()()()", "(())()"],
            expect_unordered= True
        )
        self.push_test(
            params = ("(a)())()" ,),
            expects = ["(a)()()", "(a())()"],
            expect_unordered= True
        )
        self.push_test(
            params = (")(",),
            expects = [""]
        )

    def solution(self, s):
        l=count = 0
        parenthess = []
        for i,c in enumerate(s):
            if c == "(":
                l +=1
                parenthess.append(i)
            elif c == ")":
                l -= 1
                parenthess.append(i)
            if l < 0:
                l = 0
                count += 1
        count += l

        ## key for avoid TLE
        ## this is a prune on the first level in BFS Tree
        ## to prune string start with ")"  or end with "("
        ## e.g. a)b)c)d(e(f(g
        self.remove = []
        for p in parenthess[:]:
            if s[p] == ")":
                self.remove += [p,]
                parenthess.remove(p)
                count -= 1
            else: break
        for p in parenthess[::-1]:
            if s[p] == "(":
                self.remove += [p,]
                parenthess.remove(p)
                count -= 1
            else: break

        return self.bfs(s, count, parenthess)

    def isvalid(self, s):
        stack = []
        for c in s:
            if c == "(":
                stack+= 0,
            if c == ")":
                if len(stack) == 0 or stack.pop() != 0:
                    return False

        if len(stack) > 0 : return False
        return True

    def buildstr(self,s, remove):
        ret = ""
        for i, c in enumerate(s):
            if i not in remove:
                ret+=c
        return ret

    def bfs(self, s, count, parenthess):
        if count == 0:
            return [ self.buildstr(s,self.remove) ]

        length = len(parenthess)
        queue = [ (i, count -1, [parenthess[i],]) for i in xrange(length)]
        result = set()
        while len(queue)>0:
            top = queue.pop()
            if top[1] == 0:
                remove = self.remove + top[2]
                ret = self.buildstr(s, remove)
                if self.isvalid(ret):
                    result.add(ret)
            else:
                for i in xrange(1, length - top[0]):
                    queue += [ ( (top[0]+i),top[1] -1, top[2]+[ parenthess[top[0]+i] ,] ) , ]
        return list(result)


    def solution(self, s):
        level = {s}
        while True:
            valid = []
            for s in level:
                try:## use language feature to validate the str....amazing
                    eval('0,' + filter('()'.count, s).replace(')', '),'))
                    valid.append(s)
                except:
                    pass
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}


    #### this one is much quicker than first my dfs... WTF..
    def solution(self, s):
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0
        level = {s}
        while True:
            valid = filter(isvalid, level)
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}