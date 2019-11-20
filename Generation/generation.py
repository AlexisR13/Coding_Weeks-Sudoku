from random import random
from résolution_sous_optimal import *
def grid_full()
    grid = np.zeros((9,9))
    count = 0
    while count < 5:
        k = int(random.random()*8) +1
        x = int(random.random()*8)
        y = int(random.random()*8)
        if ligne(grid,x,k) and colonne(grid,y,k) and carré(grid,x,y,k):