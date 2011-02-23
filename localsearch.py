from puzzle import *
from hillclimbing import *
from randomhillclimbing import *
from simulated_annealing import *
initial_states = []
f = open('tests' , 'r')
for line in f:
    y = []
    n = list(line)
    del n[-1]
    for i in n:
        y.append(int(i))
    initial_states.append((Node(y)))
f.close()

N = initial_states.__len__()
print(N)
heuristics = [eval_manhatten]
function = input("Enter the function : ")
d = {"hillclimbing":hillclimbing,"randomhillclimbing":random_restart_hillclimbing,"sa":sa}
for heuristic in heuristics:
    success_cost = 0
    success_count = 0
    failure_cost = 0
    for i in initial_states:
        result = d[function](i,final,heuristic)
        if result[0]:
            success_cost += result[1]
            success_count +=1
        else:
    	    failure_cost += result[1]
    print("Heuristic Used =",heuristic)
    print("Percentage of solved problems = ",success_count*100/N)
    try:
        print("Average success cost = ",success_cost/success_count)
    except:
	    pass
    try:
        print("Average failure cost = ",failure_cost/(N-success_count))
    except:
    	pass
