import numpy as np


def ligne(grid,i,k):
    n = len(grid)
    for j in range(n):
        if grid[i][j] == k:
            return False
    return True

def colonne(grid,i,k):
    n = len(grid)
    for j in range(n):
        if grid[j][i] == k:
            return False
    return True

def carré(grid,i,j,k):
    n = len(grid)
    x0 = i - (i % 3)
    y0 = j - (j % 3)
    for x in range(3):
        for y in range(3):
            if grid[x0+x][y0+y] == k:
                return False
    return True

def suivant(i,j):
    if j ==8:
        return (i+1,0)
    else:
        return (i,j+1)


def next_case(grid,i,j):    
    n = len(grid)
    grid2 = np.copy(grid)
    if (grid[i][j] != 0):
        if i == j == 8:
            return (True,grid)
        else:
            i1,j1 = suivant(i,j)
            return next_case(grid,i1,j1)
    else:
        k = 1
        i1,j1 = suivant(i,j)
        s = False       
        while (not s) and k <= 9:            
            if ligne(grid,i,k) and colonne(grid,j,k) and carré(grid,i,j,k):
                grid2 = np.copy(grid)
                grid2[i][j] = k
                print(grid2,i,j)
                s,grid_f = next_case(grid2,i1,j1)               
                if not s:
                    k +=1
            else:
                k += 1        
        if k <= 9 :
            return (True,grid_f)
        else:
            return (False,grid2)


def resolve(grid):
    return next_case(grid,0,0)[1]



ex  = [[9,5,0,0,0,0,0,4,8],[0,0,0,0,1,0,0,0,0],[0,6,3,2,0,4,9,1,0],[0,2,5,0,0,0,7,8,0],[3,8,0,5,0,9,0,2,4],[0,9,4,0,0,0,3,6,0],[0,4,9,7,0,3,8,5,0],[0,0,0,0,6,0,0,0,0],[2,1,0,0,0,0,0,7,3]]
print(resolve(ex))



        

