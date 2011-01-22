#!/bin/python
#please use python 3 to run this , it may not be fully compatible with python 2.x
from math import fabs
from grid import *
import random
from time import sleep
cell_unknown='_'
class navigator:
    def __init__(self,pos,grid):
        self.exgrid=gridclass(3,3,'_')
        self.exgrid.new_grid()
        self.exgridpos=[1,1]
        self.position=pos
        self.vec=[]
        self.virtualvec=[]
        self.action=3
        self.count=0
        self.ruleswitch=0
        self.steps=[0,0]
        self.prevexpos=[1,1]
        self.complete=0
        self.flag=[0,0]
        while (self.complete==0):
        	self.vec=[]
        	self.virtualvec=[]
        	self.sense(self.position,grid,self.vec)
        	self.sense(self.exgridpos,self.exgrid,self.virtualvec)
        	self.explore()
        	self.action=self.findrule()
        	self.exgrid.grid[self.exgridpos[0]][self.exgridpos[1]]=' '
        	self.exgrid.print_grid()
        	self.exgrid.grid[self.exgridpos[0]][self.exgridpos[1]]=0
        	print()
        	input("\nEnter to continue")
        	self.move()
        print("Number of Objects including the boundary = ",self.count)

    def explore(self):
        if(self.flag[0]==1):
        	self.prevexpos[0]+=1
        if(self.flag[1]==1):
        	self.prevexpos[1]+=1
        for i in range(self.prevexpos[0]-1,self.prevexpos[0]+2):
            for j in range(self.prevexpos[1]-1,self.prevexpos[1]+2):
                if(self.exgrid.grid[i][j]==1):
                    self.exgrid.grid[i][j]=2
        self.flag=[0,0]
        vector=self.vec
        for i in range(3):
            if(self.exgrid.grid[self.exgridpos[0]-1][self.exgridpos[1]-1+i]==cell_unknown):
                self.exgrid.grid[self.exgridpos[0]-1][self.exgridpos[1]-1+i]=vector[i]
    
        if(self.exgrid.grid[self.exgridpos[0]][self.exgridpos[1]+1]==cell_unknown):
            self.exgrid.grid[self.exgridpos[0]][self.exgridpos[1]+1]=vector[3]
        for i in range(3):
            if(self.exgrid.grid[self.exgridpos[0]+1][self.exgridpos[1]+1-i]==cell_unknown):
                self.exgrid.grid[self.exgridpos[0]+1][self.exgridpos[1]+1-i]=vector[i+4]
            if(self.exgrid.grid[self.exgridpos[0]][self.exgridpos[1]-1]==cell_unknown):
                self.exgrid.grid[self.exgridpos[0]][self.exgridpos[1]-1]=vector[7]

    def sense(self,pos,grid,vec):
        i=pos[0]
        j=pos[1]
        for x in range(3):
            self.assign(grid,i-1,j-1+x,vec)
        self.assign(grid,i,j+1,vec)
        for x in range(3):
            self.assign(grid,i+1,j+1-x,vec)
        self.assign(grid,i,j-1,vec)

    def assign(self,grid,x,y,vec):
        if (x<0 or y<0 or y>=grid.width or x>=grid.height):                  #Before the boundary of the grid
        	vec.append(1)
        else:
        	vec.append(grid.grid[x][y])

    def findrule(self):
        if(self.steps==[0,0] ):
            if (self.ruleswitch==1):
            	self.count+=1
            try:
            	self.virtualvec.index(cell_unknown)
            except ValueError:
            	self.ruleswitch=2
        for i in range(8):
            if (self.virtualvec[i]==1 or (self.virtualvec[i]==cell_unknown and self.vec[i]==1)):
                if(self.ruleswitch==3):
                    self.steps=[0,0]
                self.ruleswitch=1
        if (self.ruleswitch==1):
        	i=self.vec.index(1)
        	j=i
        	while self.vec[j]==1:
        		if (i%2 ==0):
        			j=(i+1)%8
        		else:
        			j=(i+2)%8
        		if(self.vec[j]==1):
        			i=j
        			continue
        	self.modifysteps(j)
        	return j
        for i in list_nearest(self.exgridpos[0],self.exgrid.height):
            for j in list_nearest(self.exgridpos[1],self.exgrid.width):
                if(self.exgrid.grid[i][j]==cell_unknown):
                    self.steps=[self.exgridpos[0]-i,self.exgridpos[1]-j]
                    break
            else:
                continue
            break
        else:
            if(self.exgrid.height==self.exgrid.width and self.exgrid.grid[0][0]==2):
                self.complete=1
        self.ruleswitch=3
        if(fabs((self.steps[0])<fabs(self.steps[1]) and self.steps[0] !=0) or self.steps[1]==0):
        	if (self.steps[1]>0 ):
        		j=7
        	elif (self.steps[1]<0):
        		j=3
        	elif (self.steps[0]>0 ):
        		j=1
        	else:
        		j=5
        else:
            if (self.steps[0]>0 ):
                j=1
            elif(self.steps[0]<0):
                j=5
            elif (self.steps[1]>0):
                j=7
            else:
                j=3
        for i in [1,3,5,7]:
            if(self.virtualvec[i]==2 and self.virtualvec[(i+2)%8]==2):
                if(i==1 or i==7):
                    j=5
                else:
                    j=1
                self.rule=2

        j=self.check(self.vec,j)
        if(self.steps!=[0,0]):
            self.modifysteps(j)
        return j
    def modifysteps(self,j):
        if(j==1):
        	self.steps[0]-=1
        elif(j==3):
        	self.steps[1]+=1
        elif(j==5):
        	self.steps[0]+=1
        else:
        	self.steps[1]-=1
    def move(self):
        self.prevexpos=[]
        self.prevexpos.append(self.exgridpos[0])
        self.prevexpos.append(self.exgridpos[1])
        if (self.action==1):
        	self.position[0]-=1
        	if (self.exgridpos[0]-1==0):
        		self.exgrid.insertrow(0)
        		self.flag[0]=1
        	else:
        		self.exgridpos[0]-=1
        elif (self.action==3):
        	self.position[1]+=1
        	if (self.exgrid.width-1==self.exgridpos[1]+1):
        		self.exgrid.insertcolumn(self.exgrid.width)
        	self.exgridpos[1]+=1
        elif (self.action==5):
        	self.position[0]+=1
        	if (self.exgrid.height-1==self.exgridpos[0]+1):
        		self.exgrid.insertrow(self.exgrid.height)
        	self.exgridpos[0]+=1
        else: 
        	self.position[1]-=1
        	if (self.exgridpos[1]-1==0):
        		self.exgrid.insertcolumn(0)
        		self.flag[1]=1
        	else:
        		self.exgridpos[1]-=1
    def check(self,vector,action):
            if(vector[action]!=1 ):
                return action
            return self.check(vector,random.randrange(0,4)*2 +1)

def list_nearest(objective,max):
    list=[objective]
    for i in range(1,max+1):
        j=objective-i
        if(j>=0):
            list.append(j)
        j=objective+i
        if(j<max):
        	list.append(j)
    return list


grid=gridclass(20,20)
grid.new_grid()
choice=input("want to enter objects or continue with predefined objects(y/n)")
#choice=0
if(choice=='y'):
	while(True):
		try:
			x=int(input("\nenter x of object(n to stop) "))
			y=int(input("enter y of object(n to stop) "))
			grid.grid[x][y]=1
			grid.print_grid()
		except:
			break
else:                                    #Enter objects here
     T = [(3,3),(3,4),(3,5),(3,6),(6,6,),(6,5),(6,4),(6,3),(6,2),(6,7),(10,6)]
     for (i,j) in T:
     	 grid.grid[i][j]=1
x=int(input("\nenter x of agent "))
y=int(input("enter y of agent "))

if(grid.grid[x][y]==1):
	  print("agent on object")
else:
	 object =navigator([x,y],grid)

