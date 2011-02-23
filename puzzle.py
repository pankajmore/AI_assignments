import collections
import itertools
from time import sleep
from heapq import *
import random
import math
class Node:
    def __init__(self, value=None, parent=None, action=None, path_cost=0):
        "Create a search tree Node, derived from a parent by an action."
        self.value = value
        self.parent = parent
        self.pos = self.value.index(0)
        self.f = 0

    def randomize(self):
    	random.shuffle(self.value)

    def string(self):
        return ''.join([str(item) for item in self.value])

    def new_Child(self):
        return Node(self.value[:], self)

    def move_Top(self):
        if self.pos > 2:
            self.value[self.pos], self.value[self.pos-3] = self.value[self.pos-3], self.value[self.pos]
        return self

    def move_Bottom(self):
        if self.pos < 6:
            self.value[self.pos], self.value[self.pos+3] = self.value[self.pos+3], self.value[self.pos]
        return self

    def move_Left(self):
        if self.pos not in [0,3,6]:
            self.value[self.pos], self.value[self.pos-1] = self.value[self.pos-1], self.value[self.pos]
        return self

    def move_Right(self):
        if self.pos not in [2,5,8]:
            self.value[self.pos], self.value[self.pos+1] = self.value[self.pos+1], self.value[self.pos]
        return self

    def __str__(self):
        s = '|'+'|'.join(map(str, self.value[:3]))+'|\n'
        s+= '|'+'|'.join(map(str, self.value[3:6]))+'|\n'
        s+= '|'+'|'.join(map(str, self.value[6:]))+'|'
        return s

    def __repr__(self):
    	return str(self.value)

    def path(self):
        """Create a list of nodes from the root to this node."""
        # Isn't this backwards???
        x, result = self, [self]
        while x.parent:
            result.append(x.parent)
            x = x.parent
        return result

    def children(self):
        bacche = [self.new_Child().move_Top(),self.new_Child().move_Bottom(),self.new_Child().move_Left(),self.new_Child().move_Right()]
        bacche1 = [item for item in bacche if(self.value != item.value)]
        return bacche1

final = Node([1,2,3,4,5,6,7,8,0])
#______________________________________________________________________________
## Uninformed Search algorithms

def bfs(init,goal):
    visited = []
    count = 1
    notvisited = collections.deque([init])
    n = init
    if(init.string() == goal.string()):
    	return [True,0]
    states = set()
    states.add(init.string())
    while(notvisited.__len__() != 0):
        n = notvisited.popleft()
        visited.append(n)
        for c in n.children():
            if(c.string() not in states):
                if(not_equal(c,goal) == False):
                	return [True,count]
                notvisited.append(c)
                states.add(c.string())
                #sleep(1)
        count=count+1
    return [False,count]

def path(node):
    k = []
    k.append(node)
    while(node.parent != None):
        node = node.parent
        k.append(node)
    return k
	
def path_length(node):
	return path(node).__len__()

def not_equal(n,goal):
    if(n.value == goal.value):
        return False
    else:
        return True
def depth_limit_dfs(init,goal,n):
    visited = set()
    stack = []
    count = 0
    depth = 0  
    stack.append(init)
    if(init.string() == goal.string()):
    	    return [True,0]
    while stack.__len__() !=0:
        curr = stack.pop()
        if(path_length(curr)>n):
        	continue
        if(not_equal(curr,goal) == False):
            return [True,count]
        if(curr.string() not in visited):
            count+=1
            depth+=1
            for c in curr.children():
                if(c.string() not in visited):
                    if(c.string() == goal.string()):
                    	return [True,count]

                    stack.append(c)
            	#visited.add(''.join([str(item) for item in c.value]))
            visited.add(curr.string())
    return [False,count]

def idastar(init,goal,heuristic):
    i = 0    
    globalcount = 0
    while True:
        a = depth_limit_astar(init,goal,i,heuristic)
        globalcount+=a[1]
        if(a[0]):
            return globalcount
        else:
            i+=1
            if(i>181441):
            	return [False,large]

def iddfs(init,goal):
    i = 0    
    globalcount = 0
    while True:
        a = depth_limit_dfs(init,goal,i)
        globalcount+=a[1]
        if(a[0]):
            return globalcount
        else:
            i+=1
            if(i>181441):
                return [False,large]


def misplaced_tiles(node,goal=final):
    count = 0
    for i in range(9):
        if(node.value[i] != goal.value[i]):
            count+=1
    return count+path_length(node)

#table for manhatten distance for default goal-state
md = {1:{1:0,2:1,3:2,4:1,5:2,6:3,7:2,8:3,9:4}, \
      2:{1:1,2:0,3:1,4:2,5:1,6:2,7:3,8:2,9:3}, \
      3:{1:2,2:1,3:0,4:3,5:2,6:1,7:4,8:3,9:2}, \
      4:{1:1,2:2,3:3,4:0,5:1,6:2,7:1,8:2,9:3}, \
      5:{1:2,2:1,3:2,4:1,5:0,6:1,7:2,8:1,9:2}, \
      6:{1:3,2:2,3:1,4:2,5:1,6:0,7:3,8:2,9:1}, \
      7:{1:2,2:3,3:4,4:1,5:2,6:3,7:0,8:1,9:2}, \
      8:{1:3,2:2,3:3,4:2,5:1,6:2,7:1,8:0,9:1}, \
      9:{1:4,2:3,3:2,4:3,5:2,6:1,7:2,8:1,9:0} }

def manhatten_distance(node):
    global md
    distance = 0
    for i in range(9):
        if node.value[i] != 0:
            distance += md[i+1][node.value[i]]
    return distance+path_length(node)

def sort_list(nodes,heuristic):
    a = []
    if heuristic == "misplaced":
        for i in range(nodes.__len__()):
            a.append((misplaced_tiles(nodes[i]),i))
        a.sort()
    if heuristic == "manhatten":
        for i in range(nodes.__len__()):
        	a.append((manhatten_distance(nodes[i]),i))
        a.sort()
    b = []
    for i in range(nodes.__len__()):
    	b.append(nodes[a[i][1]])
    return b


    
def astar(init,goal,heuristic):
    visited = []
    count = 1
    hcount = 1
    counter = itertools.count(1)
    notvisited = []
    heappush(notvisited,[heuristic(init),hcount,init])
    hcount = next(counter)

    n = init
    if(init.string() == goal.string()):
    	return [True,0]
    states = set()
    states.add(init.string())
    while(n.string() != goal.string()):
        count+=1
        n = heappop(notvisited)
        n = n[2]
        for c in n.children():
            if(c.string() not in states):
                if(not_equal(c,goal) == False):
                	return [True,count]
                heappush(notvisited,[heuristic(c),hcount,c])
                hcount = next(counter)
                states.add(c.string())
                #print(notvisited)
                #sleep(1)
        visited.append(n)
    return [False,count]

def depth_limit_astar(init,goal,n,heuristic=None):
    visited = set()
    stack = []
    count = 0
    hcount = 1
    counter = itertools.count(1)
    depth = 0  
    stack = []
    heappush(stack,[heuristic(init),hcount,init])
    hcount = next(counter)
    if(init.string() == goal.string()):
            return [True,0]
    while stack.__len__() !=0:
        curr = heappop(stack)
        curr = curr[2]
        if(heuristic(curr)>n):
            continue
        if(not_equal(curr,goal) == False):
            return [True,count]
        if(curr.string() not in visited):
            count+=1
            depth+=1
            for c in curr.children():
                if(c.string() not in visited):
                    if(c.string() == goal.string()):
                        return [True,count]

                    heappush(stack,[heuristic(c),hcount,c])
                    hcount = next(counter)
                #visited.add(''.join([str(item) for item in c.value]))
            visited.add(curr.string())
    return [False,count]

def precheck(init):
    iinversions = 0 
    for i in range(8):
        for j in range(i,8):
            if init.value[i] > init.value[j+1] and init.value[j+1] !=0:
                iinversions += 1
    x = init.value.index(0)
    #iinversions+=math.ceil((x+1)/3)
    #print('inversions',iinversions)
    if(iinversions %2 == 0): 
        return True
    else:
        return False

cbfs = []
ciddfs = []
castar_misplaced = []
castar_manhatten = []
cidastar_misplaced = []
cidastar_manhatten = []


def generate(N):
    i = 0
    f = open('tests', 'w')
#generate feasible test cases and write to file
    while(True):
        final = Node([1,2,3,4,5,6,7,8,0])
        initial = Node([1,2,3,4,5,6,7,8,0])
        initial.randomize()
    #initial = Node([5,4,3,2,7,8,6,1,0])
        if precheck(initial):
            for j in initial.value:
                f.write(str(j))
            f.write('\n')
            i+=1
        else:
            continue
    
        if(i==N):
            break
    f.close()
initial=[]
#read from file
#initial = Node([4,1,2,5,0,3,7,8,6])
#initial = Node([1,2,3,4,0,6,7,5,8])
#initial = Node([8,6,7,2,5,4,3,0,1])
#initial = Node([8,1,5,3,0,6,4,2,7])
"""        print(initial)
        cbfs.append(bfs(initial,final)[1])
        print('bfs',cbfs[i])
        ciddfs.append(iddfs(initial,final))


        print('iddfs',ciddfs[i])

        castar_misplaced.append(astar(initial,final,misplaced_tiles)[1])
        print('astar_misplaced',castar_misplaced[i])

        castar_manhatten.append(astar(initial,final,manhatten_distance)[1])
        print('astar_manhattten',caster_manhatten[i])
        cidastar_misplaced.append(idastar(initial,final,misplaced_tiles))
        print('idastar_misplaced',cidastar_misplaced[i])
        cidastar_manhatten.append(idastar(initial,final,manhatten_distance))
        print('idastar_manhattten',cidastar_manhatten[i])

"""
def eval_manhatten(node):
    global md
    distance = 0
    for i in range(9):
        if node.value[i] !=0:
            distance += md[i+1][node.value[i]]
    return distance
def eval_misplaced(node,goal=final):
    count = 0
    for i in range(9):
        if(node.value[i] != goal.value[i]):
            count+=1
    return count


