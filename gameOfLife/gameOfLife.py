# Importing things
import sys
import numpy as np
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Stops numpy from shortening the array when printing
np.set_printoptions(threshold=sys.maxsize)

grid = []
tempGrid = []

gridSize = 100 # Change grid size, gridSize^2 == amount of total cells
ON = 255 # 255 beacuse of matplotlib animation, change to something smaller like 1 when running without the graph
OFF = 0
vals = [ON, OFF]

# Creates the grid
def CreateGrid(size):
    global grid
    grid = np.random.choice(vals, size*size, p=[0.2, 0.8]).reshape(size, size) # Randomly generates the grid with a 20% chance of a cell being on

# This is ran for each cell
def SimulateCell(cell, neighbours):
    global grid
    global tempGrid

    # Counting live neighbours to see what the cell should do
    liveNeighbours = 0
    for i in neighbours:
        if grid[i[0]][i[1]] == ON:
            liveNeighbours += 1
    
    # Changes a temp grid in accordance to the neighbour cells
    if liveNeighbours < 2:
        tempGrid[cell[0]][cell[1]] = OFF
    elif (liveNeighbours == 2 or liveNeighbours == 3) and grid[cell[0]][cell[1]] == ON:
        tempGrid[cell[0]][cell[1]] = ON
    elif liveNeighbours > 3 and grid[cell[0]][cell[1]] == ON:
        tempGrid[cell[0]][cell[1]] = OFF
    elif liveNeighbours == 3 and grid[cell[0]][cell[1]] == OFF:
        tempGrid[cell[0]][cell[1]] = ON

def Tick():
    xCord = 0
    yCord = 0
    for x in grid:
        for y in x:
            # If on an edge, make sure that it doesn't crash as that would be no good

            # -1, -1   -1, 0   -1, +1
            # 0, -1   0, 0   0, +1
            # +1, -1   +1, 0   +1, +1

            if xCord == 0: # Top row
                if yCord == 0: # Top left corner
                    SimulateCell([xCord, yCord], [[xCord, yCord+1], [xCord+1, yCord+1], [xCord+1, yCord]])
                elif yCord == gridSize-1: # Top right corner
                    SimulateCell([xCord, yCord], [[xCord+1, yCord], [xCord+1, yCord-1], [xCord, yCord-1]])
                else: # Top row
                    SimulateCell([xCord, yCord], [[xCord, yCord-1], [xCord+1, yCord-1], [xCord+1, yCord], [xCord+1, yCord+1], [xCord, yCord+1]])
            elif xCord == gridSize-1: # Bottom row
                if yCord == 0: # Bottom left corner
                    SimulateCell([xCord, yCord], [[xCord-1, yCord], [xCord-1, yCord+1], [xCord, yCord+1]])
                elif yCord == gridSize-1: # Bottom right corner
                    SimulateCell([xCord, yCord], [[xCord, yCord-1], [xCord-1, yCord-1], [xCord-1, yCord]])
                else: # Bottom row
                    SimulateCell([xCord, yCord], [[xCord, yCord-1], [xCord-1, yCord-1], [xCord-1, yCord], [xCord-1, yCord+1], [xCord, yCord+1]])
            elif yCord == 0: # Left row
                SimulateCell([xCord, yCord], [[xCord-1, yCord], [xCord-1, yCord+1], [xCord, yCord+1], [xCord+1, yCord+1], [xCord+1, yCord]])
            elif yCord == gridSize-1: # Right row
                SimulateCell([xCord, yCord], [[xCord+1, yCord], [xCord+1, yCord-1], [xCord, yCord-1], [xCord-1, yCord-1], [xCord-1, yCord]])
            else: # Middle
                SimulateCell([xCord, yCord], [[xCord-1, yCord], [xCord-1, yCord+1], [xCord, yCord+1], [xCord+1, yCord+1], [xCord+1, yCord], [xCord+1, yCord-1], [xCord, yCord-1], [xCord-1, yCord-1]])


            yCord += 1
            if yCord == gridSize:
                yCord = 0
        xCord += 1

## Uncomment to run without matplotlib
'''
def main():
    global grid
    global tempGrid
    CreateGrid(gridSize)
    while True:
        tempGrid = np.copy(grid, order='K')
        print(grid)
        #a = input("Step")
        time.sleep(0.2)
        Tick()
        grid = np.copy(tempGrid, order='K')
'''

# Main loop
def update(data):
    global grid
    global tempGrid
    # Creates a temp grid to make changes to so that the actual grid is unnafected by the ticks
    tempGrid = np.copy(grid, order='K')
    print(grid)
    Tick() # Runs the tick
    # Updates the grid with the changes in temp grid
    grid = np.copy(tempGrid, order='K')
    mat.set_data(grid)
    return [mat]

# matplotlib setup
CreateGrid(gridSize)
fig, ax = plt.subplots()
mat = ax.matshow(grid)

# Main loop function
ani = animation.FuncAnimation(fig, update, interval=200, save_count=200) # Change these numbers to change speed
plt.show()