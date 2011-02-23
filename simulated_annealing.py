from puzzle import *
import sys
import random
def exp_schedule(k=100, lam=0.005, limit=10000):
    "One possible schedule function for simulated annealing"
    return lambda t : k*math.exp(-lam*t) if(t < limit) else 0

def sa(init,goal,heuristic,schedule=exp_schedule()):
    count = 0
    current = init
    for t in range(sys.maxsize):
        T = schedule(t)
        if T == 0:
            return [False,count]
        next = random.choice(current.children())
        delta_e = heuristic(current) - heuristic(next)
        if delta_e > 0 or random.random() < math.exp(delta_e/T):
            current = next
        count +=1
        if current.string() == goal.string():
            return [True,count]
