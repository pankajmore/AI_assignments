from grid import *
from time import sleep

class agent:
  def assign(self,grid,x,y,vec):
      if(x<0 or y<0 or y>=20 or x>=20):
        vec.append(1)
      else:
          if(grid.grid[x][y]==1):
            vec.append(grid.grid[x][y])
          else:
            vec.append(0)
  def sense(self,pos,grid,vec):
    i=pos[0]
    j=pos[1]
    for x in range(3):
      self.assign(grid,i-1,j-1+x,vec)
    self.assign(grid,i,j+1,vec)
    for x in range(3):
      self.assign(grid,i+1,j+1-x,vec)
    self.assign(grid,i,j-1,vec)

#print(vec)
  def findrule(self):
    try:
        i=self.vec.index(1)
        j=i
        print(i)
    except ValueError:
    	print("ERROR")
    	return -1 # go up by default
    while(self.vec[j]==1):
      if(i%2==0):
        j=(i+1)%8
      else:
        j=(i+2)%8
      if(self.vec[j]==1):
      	i=j
      	continue
    return j

  def move(self):
    if(self.action==1):
      self.position[0]-=1
    elif(self.action==3):
      self.position[1]+=1
    elif(self.action==5):
      self.position[0]+=1
    elif(self.action==7):
      self.position[1]-=1
    else:
      self.position[0]+=1


  def __init__(self,pos,grid):
    self.position=pos
    self.vec=[]
    self.action=3
    while(True):
      self.vec=[]
      self.sense(self.position,grid,self.vec)
      self.action=self.findrule()
      self.move()
      for i in range(8):
        print(self.vec[i])
      grid.grid[self.position[0]][self.position[1]]='X'
      grid.print_grid()
      input("\nEnter to continue")

#End of agent code

grid = gridclass(20,20)
grid.new_grid()
choice = input("Do you want to enter the objects or continue with the sample data?(y/n)")
if (choice == 'y'):
    while(True):
        try:
            x=int(input("\nEnter the x corrdinate of object(n to stop) "))
            y=int(input("Enter the y coordinate of object(n to stop) "))
            grid.grid[x][y] = 1
            grid.print_grid()
        except:
        	break
else:
	#Sample data 
    T = [(3,3),(3,4),(3,5),(3,6),(6,6,),(6,5),(6,4),(6,3),(6,2),(6,7),(10,6)]
    for (i,j) in T:
        grid.grid[i][j] =1



x = int(input("\nPlease enter the x-coordinate of agent: "))
y = int(input("Please enter the y-coordinate of agent: "))

if(grid.grid[x][y] == 1):
  print("agent on object ... plz try again")
else:
  a=agent([x,y],grid)
