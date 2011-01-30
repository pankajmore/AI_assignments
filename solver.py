from puzzle import *
initialstates = []
f = open('tests' , 'r')
for line in f:
    y = []
    n=list(line)
    del n[-1]
    for i in n:
    	y.append(int(i))
    initialstates.append((Node(y)))
f.close()
x = 1
x = input('choose')
x = int(x)
if x==1:
    for i in range(50):
        initial = initialstates[i]
        print(initial)
        castar_manhatten.append(astar(initial,final,manhatten_distance)[1])
        print('nodes expanded',castar_manhatten[i])
    print('\n')
    print('max', max(castar_manhatten))
    print('min', min(castar_manhatten))  
    print('avg', sum(castar_manhatten)/50)
    print('avg memory',sum(castar_manhatten)/50)
elif x==2:
    for i in range(50):
        initial = initialstates[i]
        print(initial)
        castar_misplaced.append(astar(initial,final,misplaced_tiles)[1])
        print('astar_misplaced',castar_misplaced[i])
    print('\n')
    print('max', max(castar_misplaced))
    print('min', min(castar_misplaced))  
    print('avg', sum(castar_misplaced)/50)
    print('avg memory',sum(castar_misplaced)/50)
elif x==3:
    for i in range(50):
        initial = initialstates[i]
        print(initial)
        cidastar_manhatten.append(idastar(initial,final,manhatten_distance))
        print('idastar_manhattten',cidastar_manhatten[i])
    print('\n')
    print('max', max(cidastar_manhatten))
    print('min', min(cidastar_manhatten))  
    print('avg', sum(cidastar_manhatten)/50)
    print('avg memory',sum(cidastar_manhatten)/50)
elif x==4:
    for i in range(50):
        initial = initialstates[i]
        print(initial)
        cidastar_misplaced.append(idastar(initial,final,misplaced_tiles))
        print('idastar_misplaced',cidastar_misplaced[i])
    print('\n')
    print('max', max(cidastar_misplaced))
    print('min', min(cidastar_misplaced))  
    print('avg', sum(cidastar_misplaced)/50)
    print('avg memory',sum(cidastar_misplaced)/50)
elif x==5:
    for i in range(50):
        initial = initialstates[i]
        print(initial)
        cbfs.append(bfs(initial,final)[1])
        print('bfs',cbfs[i])
    print('\n')
    print('max', max(cbfs))
    print('min', min(cbfs))  
    print('avg', sum(cbfs)/50)
    print('avg memory',sum(cbfs)/50)
elif x==6:
    for i in range(50):
        initial = initialstates[i]
        print(initial)
        ciddfs.append(iddfs(initial,final))
        print('iddfs',ciddfs[i])
        
    print('\n')
    print('max', max(ciddfs))
    print('min', min(ciddfs))  
    print('avg', sum(ciddfs)/50)
    print('avg memory',sum(ciddfs)/50)


