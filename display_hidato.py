from tkinter import *
from functools import partial
from resolution_hidato import *


def main_window():
    root = Tk()
    root.title("Résolution de Hidato")    
    root.resizable(0,0)
    root.geometry('150x200')
    button_frame=Frame(root)
    grid = [['','','','','','/','/','/'],['','','','','','/','/','/'],['','','','','','','/','/'],['','','','','','','/','/'],['','','','','','','','/'],['/','/','','','','','','/'],['/','/','/','/','','','',''],['/','/','/','/','/','/','','']]
    saisir_button = Button(button_frame,text="Saisir la grille",command=partial(saisir_grille,root,grid))    
    quit_button = Button(root,text="Quitter",command=quit)
    saisir_button.grid(row=0,column=0,sticky=N+S+E+W)
    saisir_button.grid(row=0,column=0,ipady=15,padx=15,sticky=N+S+E+W)
    
    button_frame.grid(row=0,column=0)
    quit_button.grid(row=1,column=0)
    Grid.rowconfigure(root,0,weight=1)
    Grid.rowconfigure(root,1,weight=1)
    Grid.columnconfigure(button_frame,0,weight=1)

    root.mainloop()
def saisir_grille(root,grid):
    def grid_to_list():
        hidato_grid = []
        for i in range(8):
            hidato_grid.append([])
            for j in range(8):
                if len(graphical_grid[i][j])==1:
                    hidato_grid[i].append('/')
                elif graphical_grid[i][j][1].get()=='':
                    hidato_grid[i].append('')
                else:
                    value = graphical_grid[i][j][1].get()
                    hidato_grid[i].append(int(value))
        print(hidato_grid)
        affiche_grille(root,resolution(hidato_grid))
    window = Toplevel(root)
    window.title("Saisir une grille de Hidato")
    window.grid()
    grid_frame = Frame(window)
    solve_button = Button(window,text="Résoudre",command=grid_to_list)
    grid_frame.grid(row=0,column=0,sticky=N+S+E+W)
    solve_button.grid(row=1,column=0,sticky=N+S+E+W,pady=10)
    Grid.rowconfigure(window,0,weight=1)
    Grid.columnconfigure(window,0,weight=1)
    graphical_grid = []
    for i in range(8):
        ligne = []
        for j in range(8):
            if grid[i][j]!='/':
                f = Frame(grid_frame, bd=1, relief='solid',bg="white", height =80, width = 80)
                e = Entry(f, font="Arial 20",justify="center",bd=0)
                e.insert(0,str(grid[i][j]))
                ligne.append((f,e))
                ligne[j][1].pack(expand = YES)
            else:
                f = Frame(grid_frame,bd=0,height=100,width=100)
                ligne.append([f])
        graphical_grid.append(ligne)


    for i in range(8):
        for j in range(8):
            graphical_grid[i][j][0].grid(row=i, column = j, sticky=N+S+E+W)      
    

    for x in range(8):
        Grid.columnconfigure(grid_frame, x, weight=1)

    for y in range(8):
        Grid.rowconfigure(grid_frame, y, weight=1)    
    
def affiche_grille(root,grid):
    print_grid = Toplevel(root)
    print_grid.title("Hidato")
    
    print(grid)
    graphical_grid=[]
    for i in range(9):
        ligne = []
        for j in range(9):
            if grid[i][j] != '/':
                f = Frame(print_grid,bg="white", bd=1, relief='solid', height =100, width = 100)
                ligne.append((f,Label(f,font="Arial 20",justify="center",bg="white",bd=0,text=str(grid[i][j]))))
                ligne[j][1].pack(expand = YES)
            else:ligne.append(Frame(print_grid,bg="white",bd=0,height=100,weight=100))
        graphical_grid.append(ligne)
    for i in range(9):
        for j in range(9):
            graphical_grid[i][j][0].grid(row=i, column = i, sticky=N+S+E+W) 
            
        Grid.columnconfigure(print_grid,i,weight=1)
        Grid.rowconfigure(print_grid,i,weight=1)

main_window()