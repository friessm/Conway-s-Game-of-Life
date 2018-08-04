"""Implementation of Conway's Game of Life.

   Rules:
   
   Infinite, two-dimensional orthogonal grid of square cells. Each of which
   is on one of two possible states, alive or dead. 
   Every cell interacts with its eight neighbours. At each step (tick) the 
   following transitions occur:

   1. Any live cell with fewer than two live neighbors dies, as if by under 
   population
   2. Any live cell with two or three live neighbors lives on to the next 
   generation
   3. Any live cell with more than three live neighbors dies, as if by 
   overpopulation
   4. Any dead cell with exactly three live neighbors becomes a live cell, as 
   if by reporduction. 

   The game is started by an initial seed pattern on which the aformentioned 
   rules are applied.
"""

from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def random_grid():
    height = 30
    width = 30
    grid = [[randint(0, 1) for i in range(width)] for j in range(height)]
    return grid

def get_grid_size(grid):
    height = len(grid)
    width = len(grid[0])
    return height, width

def iterate(i, height, width):
    global grid
    next_ = [[0 for i in range(height)] for j in range(width)]

    for row_i in range(height):
        for col_i in range(width):
            
            state = grid[row_i][col_i]
            neighbors = count_neighbors(grid, row_i, col_i)

            if state == 0 and neighbors == 3:
                next_[row_i][col_i] = 1
            elif state == 1 and (neighbors < 2 or neighbors > 3):
                next_[row_i][col_i] = 0
            else:
                next_[row_i][col_i] = state
    
    grid = next_
    im.set_array(grid)
    return im

def count_neighbors(grid, row_index, col_index):
    count = 0
    for row_neighbor in range(-1, 2):
        for col_neighbor in range(-1, 2):
            
            # wrap around to handle neighbors are outside of the 2D list
            row = (row_index + row_neighbor + height) % height
            col = (col_index + col_neighbor + width) % width  
            count += grid[row][col]
    
    # do not count the selected (state) cell
    count -= grid[row_index][col_index]
    return count

def init():
    init_grid = random_grid()
    return init_grid

if __name__ == "__main__":
    grid = random_grid()
    height, width = get_grid_size(grid)

    fig = plt.figure(dpi=200)
    plt.axis('off')
    im = plt.imshow(grid, cmap='binary')

    ani = animation.FuncAnimation(fig, 
                                  iterate, 
                                  init_func=init, 
                                  fargs=(height, width), 
                                  interval=80)
    plt.show()