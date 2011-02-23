from puzzle import *
#read initial states from tests and store in init
def hillclimbing(init,goal,heuristic,c=0):
    current = init
    count = c
    while True:
        bs = current
        for c in current.children():
            if heuristic(c) < heuristic(bs):
            	bs = c
        count += 1
        if goal.string() == bs.string():
        	return [True,count]
        else:
            if bs == current:
            	return [False,count]
            else:
        	    current = bs
    
