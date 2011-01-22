#!/usr/bin/python
class gridclass(object):
    """Grid class with a width, height"""
    def __init__(self, width, height,value=0):
        self.width = width
        self.height = height
        self.value=value
    def new_grid(self):
        """Create an empty grid"""
        self.grid = []
        row_grid = []
        
        for col in range(self.width):
            for row in range(self.height):
                row_grid.append(self.value)
            self.grid.append(row_grid)
            row_grid = []  # reset row
        return self.grid

    def print_grid(self):
        for row in range(self.height):
            for col in range(self.width):
                print(self.grid[row][col],end=" ")
            print()
    def insertrow(self,pos):
        cell_value = '_'
        self.height+=1
        self.grid.insert(pos,[cell_value]*self.width)
    def insertcolumn(self,pos):
        cell_value='_'
        for i in range(self.height):
            self.grid[i].insert(pos,cell_value)
        self.width+=1
    def edit(self,x,y,val):
        self.grid[x][y]=val
#my_grid = grid(10, 10)
#print ("Empty grid ...")
#my_grid.new_grid()
#my_grid.print_grid()
#my_grid.insertrow(3)
#my_grid.insertcolumn(8)
#my_grid.print_grid()
