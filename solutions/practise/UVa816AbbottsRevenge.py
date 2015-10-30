__author__ = 'Daoyuan'

from ..BaseSolution import *

class Node(object):
    def __init__(self, r = -1, c = -1, dir=-1):
        self.c = c
        self.r = r
        self.dir = dir

class UVa816AbbottsRevenge(BaseSolution):

    def __init__(self):
        BaseSolution.__init__(self)
        self.push_test(
            params = ([
                    "SAMPLE",
                    "3 1 N 3 3",
                    "1 1 WL NR *",
                    "1 2 WLF NR ER *",
                    "1 3 NL ER *",
                    "2 1 SL WR NF *",
                    "2 2 SL WF ELF *",
                    "2 3 SFR EL *",
                    "0",
                    "NOSOLUTION",
                    "3 1 N 3 2",
                    "1 1 WL NR *",
                    "1 2 NL ER *",
                    "2 1 SL WR NFR *",
                    "2 2 SR EL *",
                    "0",
                    "END"
                    ],),
            expects = """SAMPLE
(3,1) (2,1) (1,1) (1,2) (2,2) (2,3) (1,3) (1,2) (1,1) (2,1)
(2,2) (1,2) (1,3) (2,3) (3,3)
NOSOLUTION
No Solution Possible"""
        )

    def dir2num(self, dir):
        DIR = "NESW"
        return DIR.find(dir)
    def turn2num(self, turn):
        TURN = "FLR"
        return TURN.find(turn)

    def turn2dir(self, dir, turn):
        if turn == 1: return (dir + 3) % 4
        if turn == 2: return (dir + 1) % 4
        if turn == 0: return dir
        return  -1 # error! should not happen

    def walk(self, node, turn):
        r,c,dir = node.r, node.c, node.dir
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        to = self.turn2dir(dir, turn)
        return Node( r + dr[to], c+dc[to], to)

    def solution(self, params):
        idx = 0
        result = ""
        while True:
            title = params[idx]
            if title == "END":break
            idx = idx + 1
            r0,c0,dir0,r2,c2 =  params[idx].split(' ')
            r0, c0, r2, c2 = (int(item) for item in [r0, c0, r2, c2])
            dir0 = self.dir2num(dir0)
            maxc = 9
            maxr = 9
            self.map = [ [ [ [False] * 4 for i in xrange(4)] for j in xrange(maxc)] for k in xrange(maxr)]
            self.shortest= [ [[-1] * 4 for i in xrange(maxc)] for j in xrange(maxr) ]
            self.parent = [ [ [None]*4 for i in xrange(maxc)] for j in xrange(maxr) ]

            # build map
            while True:
                idx = idx + 1
                segs = params[idx].split(" ")
                if len(segs) == 1 and segs[0] == "0":
                    idx = idx + 1
                    break
                i = 2
                row, col = int(segs[0]),int(segs[1])
                while segs[i] != "*":
                    direction = self.dir2num(segs[i][0])
                    for j in range(1, len(segs[i])):
                        turn = self.turn2num(segs[i][j])
                        to = self.turn2dir(direction, turn)
                        self.map[row][col][direction][to] = True
                    i = i+1

            # init
            dr = [-1, 0, 1, 0]
            dc = [0, 1, 0, -1]
            r1, c1 = r0 + dr[dir0], c0 + dc[dir0]
            self.r0, self.c0, self.r1, self.c1, self.r2, self.c2 = r0, c0, r1, c1, r2, c2

            start = Node(r1,c1,dir0)
            ret = self.bfs(start)
            result = result + title + "\n"
            if ret is None:
                 result = result + "No Solution Possible"
            else:
                result = result + self.stringfy_path(ret) + "\n"
        return result.strip()
    def stringfy_path(self, node):
        path = []
        ret = ""
        while True:
            path.insert(0, node)
            if self.parent[node.r][node.c][node.dir] is not None:
                node = self.parent[node.r][node.c][node.dir]
            else:
                break

        path.insert(0, Node(self.r0, self.c0))

        for i, item in enumerate(path):
            ret = ret + "(%d,%d)" % (item.r, item.c)
            if i > 0 and (i+1) % 10 == 0:
                ret = ret + "\n"
            else:
                ret= ret + " "
        return ret.strip()
    def bfs(self, start):
        queue = []
        queue.append(start)
        self.shortest[start.r][start.c][start.dir] = 0
        while queue.__len__() > 0:
            top = queue.pop(0)
            if top.r == self.r2 and top.c == self.c2:
                return top
            for i in range(0,3):
                to = self.turn2dir(top.dir, i)
                if self.map[top.r][top.c][top.dir][to]:
                    next = self.walk(top, i)
                    if self.shortest[next.r][next.c][next.dir] < 0:
                        self.shortest[next.r][next.c][next.dir] = self.shortest[top.r][top.c][top.dir]+1
                        self.parent[next.r][next.c][next.dir] = top
                        queue.append(next)
        return None