from puzzle import *
from hillclimbing import *
#from localsearch import initial_states
counter = 0
def random_restart_hillclimbing(init,goal,heuristic):
    global counter
    counter += 1
    initial = init
    result = hillclimbing(init,goal,heuristic)
    while counter < 1000:
        if(result[0] == False):
            initial.randomize()
            	
#        print(initial)
            result1 = hillclimbing(initial,goal,heuristic,result[1])
            result = result1
        else:
            return result
    return result

