
# game of life

import random
import time
import sys

class Life:
    def __init__(self,grid):
        self.gridsize = grid
        end = self.gridsize -1
        grid_array = [ [ ' ' for y in range( self.gridsize ) ] for x in range( self.gridsize ) ]

        for i in range(self.gridsize):
            for j in range(self.gridsize):
                if (i == 0 and j == 0) or (i == 0 and j == end) or (i == end and j == 0) or (i == end and j == end):
                    grid_array[i][j] = '+'
                elif i == 0 or i == end:
                    grid_array[i][j] = '-'
                elif j == 0 or j == end:
                    grid_array[i][j] = '|'
                else:
                    life = bool(random.getrandbits(1))
                    if life:
                        grid_array[i][j] = 'o'

        self.grid_array = grid_array
        self.pretty_print(grid_array)

    def calculate_comb(self,field):
        counter = 0

        output = [ [ ' ' for y in range( self.gridsize ) ] for x in range( self.gridsize ) ]
        end = self.gridsize - 1

        for i in range(self.gridsize):
            for j in range(self.gridsize):
                if (i == 0 and j == 0) or (i == 0 and j == end) or (i == end and j == 0) or (i == end and j == end):
                    output[i][j] = '+'
                elif i == 0 or i == end:
                    output[i][j] = '-'
                elif j == 0 or j == end:
                    output[i][j] = '|'

        for i in range(1,self.gridsize-1):
            for j in range(1,self.gridsize-1):

                for u in range(i-1,i+2):
                    for v in range(j-1,j+2):
                        if not (u == i and v == j):
                            if field[u][v] == 'o':
                                counter += 1

                if (field[i][j] == 'o' and counter == 2) or counter == 3:
                    output[i][j] = 'o'

                counter = 0

        self.grid_array = output
        self.pretty_print(output)


    def pretty_print(self,grid):
        for i in range(self.gridsize):
            for j in range(self.gridsize):
                print(grid[i][j],end=' ')
                if j == self.gridsize-1:
                    print('\n')

if __name__ == '__main__':
    test = Life(20)
    for i in range(0,20):
        time.sleep(0.4)
        test.calculate_comb(test.grid_array)

