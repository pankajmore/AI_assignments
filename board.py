import sys
import operator
import random
import time

Empty = ' '
Player_X = 'x'
Player_O = 'o'

class Board():
    def __init__(self,n):
        self.order = n
        self.pieces = [Empty]*n*n
        self.field_names = [str(i) for i in range(1,n*n+1)]

    def display(self):
        for line in [self.pieces[self.order*i:self.order*(i+1)] for i in range(self.order)]:
            print(' '.join(line))

    def winner(self):
        winning_rows = [range(self.order*i,self,self.order*(i+1)) for i in range(self.order)]
        winning_rows.extend = [range(i,self.order*self.order-(self.order-i)+1
