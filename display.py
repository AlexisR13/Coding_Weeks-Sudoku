from tkinter import filedialog
from tkinter import *
from functools import partial
from Reconnaissance.photo_to_grid import *
<<<<<<< HEAD
from résolution_sous_optimal import *
from resolution_optimisée import *
from generation import *
import numpy as np
=======
from Resolution.résolution_sous_optimal import *

>>>>>>> Thomas


def main_window():
    root = Tk()
    root.title("Résolution de Sudoku")    
    root.resizable(0,0)
    root.geometry('380x200')
    button_frame=Frame(root)
    info_label = Label(root, text="Choisissez comment saisir la grille:")
    scan_button = Button(button_frame,text="Scanner une grille",command=partial(open_scan,root))
    def transform(grille):
        print(grille)
        for i in range(9):
            for j in range(9):
                
                if grille[i][j] == 0.0:
                    grille[i][j] = ''
                else: grille[i][j] = int(grille[i][j])
        return grille
    def generate():
        popup = Tk()
        def destroy():
            diff = choix_difficulte.curselection()
            diff = choix_difficulte.get(diff)
            print(diff)
            saisir_grille(root,transform(generation(diff).tolist()))
            popup.destroy()
            

        popup.wm_title("Générer grille")
        label = Label(popup, text="Veuillez séléctionner la difficulté de la grille")
        label.pack(side="top", fill="x", pady=10)
        radio_frame = Frame(popup)

        choix_difficulte = Listbox(radio_frame,selectmode=SINGLE,width=50)
        choix_difficulte.insert(1,"Facile")
        choix_difficulte.insert(2,"Moyen")
        choix_difficulte.insert(3,"Difficile")
        choix_difficulte.selection_set(first=0)
        choix_difficulte.grid(sticky=N+S+E+W)

        radio_frame.pack(fill="x",pady=10)
        B1 = Button(popup, text="Générer", command = destroy)
        B1.pack(side="bottom")
        popup.mainloop()
        return None
    game_grid = []
    for i in range(9):
        game_grid.append([])
        for j in range(9):
            game_grid[i].append('')
    saisir_button = Button(button_frame,text="Saisir la grille",command=partial(saisir_grille,root,game_grid))
    generer_button = Button(button_frame,text="Générer la grille",command=generate)
    
    quit_button = Button(root,text="Quitter",command=quit)
    info_label.grid(row=0,column=0)
    saisir_button.grid(row=0,column=0,ipady=15,padx=15)
    scan_button.grid(row=0,column=1,ipady=15,pady=30,padx=15)
    generer_button.grid(row=0,column=2,ipady=15,pady=30,padx=15)
    button_frame.grid(row=1,column=0)
    quit_button.grid(row=2,column=0)
    Grid.rowconfigure(root,0,weight=1)
    Grid.rowconfigure(root,1,weight=1)
    Grid.rowconfigure(root,2,weight=1)
    Grid.columnconfigure(button_frame,0,weight=1)
    Grid.columnconfigure(button_frame,2,weight=1)
    Grid.columnconfigure(button_frame,1,weight=1)
    root.mainloop()
def open_scan(root):
    #jpg
    filename = filedialog.askopenfilename(initialdir = "/images",title = "Selectionnez une image",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    grid = photo_to_grid(filename)
    popupmsg(root,grid)

def popupmsg(root,grid):
    """
    Ouvre un popup pour dire à l'utilisateur de vérifier la grille scannée
    """
    popup = Tk()
    def destroy():
        popup.destroy()
        saisir_grille(root,grid)
    popup.wm_title("Verifier la grille")
    label = Label(popup, text="Veuillez verifier que la grille a bien été remplie et corriger les erreurs")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = destroy)
    B1.pack()
    popup.mainloop()

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
def check_grid(root,grille,grille_initiale):
    def transform_grille():
        grille_intermediaire = []
        for i in range(9):
            grille_intermediaire.append([])
            for j in range(9):
                grille_intermediaire[i].append(grille[i][j])
        for i in range(9):
            for j in range(9):
                if grille_intermediaire[i][j] == 0:
                    grille_intermediaire[i][j] = ''
                elif type(grille_intermediaire[i][j]) == int:
                    grille_intermediaire[i][j] = [grille_intermediaire[i][j]]
        return grille_intermediaire
        
    correcte = verification_grille(transform_grille())
    def popupcheck(correcte):
        popup = Tk()
        def destroy():
            popup.destroy()
            if correcte:
                root.destroy
        if correcte:
            popup.wm_title("Sudoku")
            label = Label(popup, text="La grille est correcte vous avez gagné!")
        else:
            popup.wm_title("Sudoku")
            label = Label(popup, text="La grille est incorrecte, veuillez rééssayer")
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(popup, text="Okay", command = destroy)
        B1.pack()
        popup.mainloop()
    popupcheck(correcte)
    


    
def play_grid(root,grille,grille_modif):
    def grid_to_list():
        sudoku_grid = []
        for i in range(9):
            sudoku_grid.append([])
            for j in range(9):
                if type(graphical_grid[i][j][1]) == Entry:
                    value = graphical_grid[i][j][1].get()
                elif type(graphical_grid[i][j][1])==Label:
                    value = graphical_grid[i][j][1].cget("text")
                if value=='':
                    sudoku_grid[i].append('')
                else: sudoku_grid[i].append(int(value))
        check_grid(root,sudoku_grid,grille)
    def suggest():

        return None
    window = Toplevel(root)
    window.title("Sudoku")
    window.grid()
    grid = Frame(window)
    
    frame_tools = Frame(window)
    suggestion_button=Button(frame_tools,text="Suggestion",command=suggest)
    suggestion_button.grid(row=0,column=0)
    frame_button = Frame(window)
    check_button = Button(frame_button,text="Vérifier",command=grid_to_list)
    check_button.grid(row=0,column=0,sticky=N+S+E+W)
    Grid.columnconfigure(frame_button,0,weight=1)
    Grid.rowconfigure(frame_button,0,weight=1)
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
            if grille[i][j] != '':
                ligne.append((f,Label(f,font="Arial 20",justify="center",bg="white",bd=0,text=grille[i][j])))
            elif grille_modif[i][j] != '':
                e = Entry(f,font="Arial 20",justify="center",bd=0)
                e.insert(0,grille_modif[i][j])
                ligne.append((f,e))
            else:
                e = Entry(f,font="Arial 20",justify="center",bd=0)
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
    frame_tools.grid(row=0,column=0,sticky=N+S+E+W)
    grid.grid(row=1,column=0,sticky=N+S+E+W)
    frame_button.grid(row=2,column=0,sticky=N+S+E+W)
    Grid.rowconfigure(window,0,weight=1)
    Grid.columnconfigure(window,0,weight=1)
    


def saisir_grille(root,grille):
    def grid_to_list(action):
        sudoku_grid = []
        for i in range(9):
            sudoku_grid.append([])
            for j in range(9):
                value = graphical_grid[i][j][1].get()
                if value=='':
                    sudoku_grid[i].append('')
                else: sudoku_grid[i].append(int(value))
        if action == 'solve':
            affiche_grille(root,resolve(transform_grid(sudoku_grid)))
        elif action =='play':
            grille_modif = []
            for i in range(9):
                grille_modif.append([])
                for j in range(9):
                    grille_modif[i].append('')
            play_grid(root,sudoku_grid,grille_modif)
    window = Toplevel(root)
    window.title("Saisir une grille de Sudoku")
    window.grid()
    grid = Frame(window)
    frame_button = Frame(window)
    play_button = Button(frame_button,text="Jouer",command=partial(grid_to_list,'play'))
    solve_button = Button(frame_button,text="Résoudre",command=partial(grid_to_list,'solve'))
    play_button.grid(row=0,column=0,sticky=N+S+E+W)
    solve_button.grid(row=0,column=1,sticky=N+S+E+W)
    Grid.columnconfigure(frame_button,0,weight=1)
    Grid.columnconfigure(frame_button,1,weight=1)
    Grid.rowconfigure(frame_button,0,weight=1)
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
    frame_button.grid(row=1,column=0,sticky=N+S+E+W)
    Grid.rowconfigure(window,0,weight=1)
    Grid.columnconfigure(window,0,weight=1)
    

main_window()