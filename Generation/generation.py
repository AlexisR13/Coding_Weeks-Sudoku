from random import *
from résolution_sous_optimal import *
import numpy as np
from tkinter import *


def grid_full():
    """
    renvoie une grille de sudoku remplie
    """
    grid = np.zeros((9,9))
    count = 0
    while count < 15:
        value = randint(1,9)
        x = randint(0,8)
        y = randint(0,8)
        if ligne(grid,x,value) and colonne(grid,y,value) and carré(grid,x,y,value) and grid[x][y]==0:            
            grid[x][y] = value
            count += 1
    grid = resolve_random(grid)
  
    return grid


def empty_count(grid):
    """
    compte le nombre de case vide d'une grille
    """
    n = len(grid)
    count = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                count += 1
    return count

def unicité(grid_ref,grid):
    """
    teste l'unicité d'une grille
    """
    for i in range(5):

        if False in (grid_ref == resolve_random(grid)):
            return False
    return True


def remove_value(grid,v,p_bar):
    """
    enlève des valeurs de la grille grid jusqu'à qu'il n'en reste plus que un nombre v et met à jour la barre de progression p_bar
    """
    def progress(currentValue):
        """
        met à jour la barre de progression
        """
        progressbar["value"]=currentValue
    
    grid2 = np.copy(grid)
    count = 81
    count2 = 0
    while count > v:
        count2 += 1
        if count2 > 500:
            return (False,grid)
        
        p_bar.after(500, progress(81-count)) #mise à jour de la barre de progression
        p_bar.update() 
        x = randint(0,8)
        y = randint(0,8)
        
        if grid2[x][y] != 0:
                     
            grid2[x][y] = 0
            if unicité(grid,grid2):
                count -= 1
            else:
                grid2[x][y] = grid[x][y]
    return (True,grid2)


def generation(diff,p_bar):
    """
    génère une grille de difficulté diff
    """
    if diff == "Facile":
        v = 32
        p_bar[maximum] = 81-32
    elif diff == "Moyen":
        v = 27
        p_bar[maximum] = 81-27
    else:
        v = 23
        p_bar[maximum] = 81-23

    s = False
    while not s:
        grid = grid_full()
        print('ok')
        s,grid = remove_value(grid,v,p_bar)

    return grid

