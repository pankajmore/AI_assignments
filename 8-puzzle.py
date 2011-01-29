import collections
from time import sleep
class Node:
    def __init__(self, value=None, parent=None, action=None, path_cost=0):
        "Create a search tree Node, derived from a parent by an action."
        self.value = value
        self.parent = parent
        self.pos = self.value.index(0)
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

def not_equal(n,goal):
    if(n.value == goal.value):
        return False
    else:
        return True

initial = Node([1,2,3,4,5,6,0,7,8])
final = Node([1,2,3,4,0,6,7,5,8])
#print(initial.children())
print(bfs(initial,final))
def depth_limit_dfs(init,goal,n):
    visited = set()
    stack = []
    count = 0
    depth = 0
    stack.append(init)
    while depth <= n and stack.__len__() !=0:
        curr = stack.pop()
        if(not_equal(curr,goal) == False):
            return [True,count]
        if(''.join([str(item) for item in curr.value]) not in visited):
            for c in curr.children():
            	stack.append(c)
            	#visited.add(''.join([str(item) for item in c.value]))
            visited.add(''.join([str(item) for item in curr.value]))
            count=count+1
            depth=depth+1
    return [False,count]

def iddfs(init,goal):
    i = 0
    globalcount = 0
    while True:
        a = depth_limit_dfs(init,goal,i)
        globalcount+=a[1]
        if(a[0]):
            print(globalcount)
            break
        else:
            i+=1



iddfs(initial,final)
