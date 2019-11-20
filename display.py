from tkinter import filedialog
from tkinter import *
from functools import partial
from Reconnaissance.photo_to_grid import *
from résolution_sous_optimal import *



def main_window():
    root = Tk()
    root.title("Résolution de Sudoku")    
    root.resizable(0,0)
    root.geometry('280x200')
    button_frame=Frame(root)
    info_label = Label(root, text="Choisissez comment saisir la grille:")
    scan_button = Button(button_frame,text="Scanner une grille",command=partial(open_scan,root))
    game_grid = []
    for i in range(9):
        game_grid.append([])
        for j in range(9):
            game_grid[i].append('')
    saisir_button = Button(button_frame,text="Saisir la grille",command=partial(saisir_grille,root,game_grid))
    quit_button = Button(root,text="Quitter",command=quit)
    info_label.grid(row=0,column=0)
    saisir_button.grid(row=0,column=0,ipady=15,padx =30)
    scan_button.grid(row=0,column=1,ipady=15,pady=30)
    button_frame.grid(row=1,column=0)
    quit_button.grid(row=2,column=0)
    Grid.rowconfigure(root,0,weight=1)
    Grid.rowconfigure(root,1,weight=1)
    Grid.rowconfigure(root,2,weight=1)
    Grid.columnconfigure(button_frame,0,weight=1)
    Grid.columnconfigure(button_frame,1,weight=1)
    root.mainloop()
def open_scan(root):
    #jpg
    filename = filedialog.askopenfilename(initialdir = "/images",title = "Selectionnez une image",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    grid = photo_to_grid(filename)
    saisir_grille(root,grid)

def affiche_grille(root,grille):
    grid = Toplevel(root)
    grid.title("Sudoku")
    
    main_grid = []
    for i in range(3):
        ligne = []
        for j in range(3):
            f = Frame(grid, bd=2, relief='solid', height =300, width = 300)
            ligne.append(f)
        main_grid.append(ligne)

    


    for i in range(3):
        for j in range(3):
            main_grid[i][j].grid(row=i, column = j, sticky=N+S+E+W)      
    

    for x in range(3):
        Grid.columnconfigure(grid, x, weight=1)

    for y in range(3):
        Grid.rowconfigure(grid, y, weight=1)    
    
    graphical_grid=[]
    for i in range(9):
        ligne = []
        for j in range(9):
            f = Frame(main_grid[i//3][j//3],bg="white", bd=1, relief='solid', height =100, width = 100)
            ligne.append((f,Label(f,font="Arial 20",justify="center",bg="white",bd=0,text=grille[i][j])))
            ligne[j][1].pack(expand = YES)
        graphical_grid.append(ligne)
    for i in range(9):
        for j in range(9):
            graphical_grid[i][j][0].grid(row=i%3, column = j%3, sticky=N+S+E+W) 

    for x in range(3):
        for i in range(3):
            for j in range(3):
                Grid.columnconfigure(main_grid[i][j], x, weight=1)
                Grid.rowconfigure(main_grid[i][j],x,weight=1)

    grid.grid()

def saisir_grille(root,grille):
    def grid_to_list():
        sudoku_grid = []
        for i in range(9):
            sudoku_grid.append([])
            for j in range(9):
                value = graphical_grid[i][j][1].get()
                if value=='':
                    sudoku_grid[i].append('')
                else: sudoku_grid[i].append(int(value))
        affiche_grille(root,resolve(transform_grid(sudoku_grid)))
    window = Toplevel(root)
    window.title("Saisir une grille de Sudoku")
    window.grid()
    grid = Frame(window)
    solve_button = Button(window,text="Résoudre",command=grid_to_list)
    main_grid = []
    for i in range(3):
        ligne = []
        for j in range(3):
            f = Frame(grid, bd=2, relief='solid', height =300, width = 300)
            ligne.append(f)
        main_grid.append(ligne)

    


    for i in range(3):
        for j in range(3):
            main_grid[i][j].grid(row=i, column = j, sticky=N+S+E+W)      
    

    for x in range(3):
        Grid.columnconfigure(grid, x, weight=1)

    for y in range(3):
        Grid.rowconfigure(grid, y, weight=1)    
    
    graphical_grid=[]
    for i in range(9):
        ligne = []
        for j in range(9):
            f = Frame(main_grid[i//3][j//3],bg="white", bd=1, relief='solid', height =100, width = 100)
            e = Entry(f,font="Arial 20",justify="center",bd=0)
            e.insert(0,str(grille[i][j]))
            ligne.append((f,e))
            ligne[j][1].pack(expand = YES)
        graphical_grid.append(ligne)
    for i in range(9):
        for j in range(9):
            graphical_grid[i][j][0].grid(row=i%3, column = j%3, sticky=N+S+E+W) 

    for x in range(3):
        for i in range(3):
            for j in range(3):
                Grid.columnconfigure(main_grid[i][j], x, weight=1)
                Grid.rowconfigure(main_grid[i][j],x,weight=1)

    grid.grid(row=0,column=0,sticky=N+S+E+W)
    solve_button.grid(row=1,column=0,sticky=N+S+E+W)
    Grid.rowconfigure(window,0,weight=1)
    Grid.columnconfigure(window,0,weight=1)
    

main_window()