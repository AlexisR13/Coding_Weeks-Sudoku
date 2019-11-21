from random import *
from resolution_optimisée import *
from Resolution.résolution_sous_optimal import *
import numpy as np
def grid_full():
    grid = np.zeros((9,9))
    count = 0
    while count < 21:
        k = randint(1,9)
        x = randint(0,8)
        y = randint(0,8)
        if ligne(grid,x,k) and colonne(grid,y,k) and carré(grid,x,y,k) and grid[x][y]==0:            
            grid[x][y] = k
            count += 1
    
    grid = int_to_string(grid)
    affichage(grid)
    print(grid)
    grid = resolution_hazardeuse(grid)
    print(grid)
    return string_to_int(grid)


def empty_count(grid):
    n = len(grid)
    count = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                count += 1
    return count

def unicité(grid_ref,grid):
    for i in range(5):
        print("try")
        if False in (grid_ref == string_to_int(resolution_hazardeuse(int_to_string(grid)))):
            return False
    return True


def remove_value(grid,v):
    grid2 = np.copy(grid)
    count = 81
    count2 = 0
    while count > v:
        count2 += 1
        if count2 > 500:
            return (False,grid)
        
        print(count)
        x = randint(0,8)
        y = randint(0,8)
        
        if grid2[x][y] != 0:
                     
            grid2[x][y] = 0
            #not (False in (grid == resolve_random(grid2)))
            if unicité(grid,grid2):
                count -= 1
            else:
                grid2[x][y] = grid[x][y]
    return (True,grid2)


#grid = grid_full()
#grid2 = remove_value(grid,22)
#print(grid == resolve(grid2))
#print(grid2)

def generation(diff):
    if diff == "facile":
        v = 30
    elif diff == "moyen":
        v = 25
    else:
        v = 20

    s = False
    while not s:
        grid = grid_full()
        print('ok')
        s,grid = remove_value(grid,v)

    return grid


print(generation("di"))

