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
        if i == 8:
            return (8,8)
        else:        
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

def transform_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]=='':
                grid[i][j]=0
            elif type(grid[i][j])==list: grid[i][j] = grid[i][j][0]
            
    return grid



ex  = [[9,5,0,0,0,0,0,4,8],[0,0,0,0,1,0,0,0,0],[0,6,3,2,0,4,9,1,0],[0,2,5,0,0,0,7,8,0],[3,8,0,5,0,9,0,2,4],[0,9,4,0,0,0,3,6,0],[0,4,9,7,0,3,8,5,0],[0,0,0,0,6,0,0,0,0],[2,1,0,0,0,0,0,7,3]]

ex2 =  [[0,6,0,8,9,3,0,4,0],[2,0,0,0,0,0,0,0,6],[0,0,3,2,0,1,7,0,0],[7,0,0,0,5,0,0,0,8],[3,0,8,1,7,6,5,0,4],[9,0,0,0,3,0,0,0,1],[0,0,5,6,0,9,4,0,0],[6,0,0,0,0,0,0,0,5],[0,9,0,5,2,7,0,1,0]]
sudoku=[['' ,[6],'' ,[8],[9],[3],'' ,[4],'' ],
        [[2],'' ,'' ,'' ,'' ,'' ,'' ,'' ,[6]],
        ['' ,'' ,[3],[2],'' ,[1],[7],'' ,'' ],
        [[7],'' ,'' ,'' ,[5],'' ,'' ,'' ,[8]],
        [[3],'' ,[8],[1],[7],[6],[5],'' ,[4]],
        [[9],'' ,'' ,'' ,[3],'' ,'' ,'' ,[1]],
        ['' ,'' ,[5],[6],'' ,[9],[4],'' ,'' ],
        [[6],'' ,'' ,'' ,'' ,'' ,'' ,'' ,[5]],
        ['' ,[9],'' ,[5],[2],[7],'' ,[1],'' ]]

sudoku2=[['','' ,'' ,'' ,[3],'' ,'' ,'' ,'' ],
        ['' ,'' ,[4],[8],'' ,[7],[6],'' ,'' ],
        [[3],[1],'' ,'' ,[5],'' ,'' ,[2],[7]],
        ['' ,[6],'' ,'' ,'' ,'' ,'' ,[1],'' ],
        ['' ,[7],[1],[9],'' ,[8],[2],[6],'' ],
        ['' ,[2],'' ,'' ,'' ,'' ,'' ,[9],'' ],
        [[1],[4],'' ,'' ,[8],'' ,'' ,[7],[9]],
        ['' ,'' ,[8],[5],'' ,[2],[3],'' ,'' ],
        ['' ,'' ,'' ,'' ,[9],'' ,'' ,'' ,'' ]]


sudoku3=[['' ,'' ,'' ,'' ,[8],'' ,'' ,'' ,'' ],
         [[8],'' ,'' ,'' ,[9],'' ,'' ,'' ,[3]],
         ['' ,'' ,[5],[2],[7],[3],[6],'' ,'' ],
         ['' ,[4],[1],'' ,'' ,'' ,[3],[7],'' ],
         [[7],'' ,'' ,'' ,'' ,'' ,'' ,'' ,[6]],
         ['' ,[6],[2],'' ,'' ,'' ,[8],[5],'' ],
         ['' ,'' ,[9],[8],[1],[7],[2],'' ,'' ],
         [[4],'' ,'' ,'' ,[5],'' ,'' ,'' ,[7]],
         ['' ,'' ,'' ,'' ,[2],'' ,'' ,'' ,'' ]]
#print(resolve(ex2))
#print(resolve(transform_grid(sudoku)))
#print(resolve(transform_grid(sudoku2)))
#print(resolve(transform_grid(sudoku3)))



        

