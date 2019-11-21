import sys

def affichage(grille): #permet d'afficher la grille de manière lisible pour un humain
    A='La solution de la grille est : \n'
    ligne='  -   -   -   -   -   -   -   -   -'
    A+=ligne
    A+='\n'
    for i in range(len(grille)):
        A+='!  '
        for j in range(len(grille)):
            if len(grille[i][j])==1:
                A+=str(grille[i][j][0])
            else:
                A+='0'
            if (j+1)%3==0: A+='  !  '
            else: A+='  '
        if (i+1)%3==0: A+='\n' + ligne + '\n'
        else: A+='\n'
    print(A)
def moins_possibilites(grille):
    #renvoi les indices de la case de la grille où la liste des possibilités est la moins longue
    imin,jmin = 0,0
    lmin = 9
    for i in range(9):
        for j in range(9):
            if len(grille[i][j])<lmin and len(grille[i][j])!=1 :
                 imin = i
                 jmin = j
                 lmin = len(grille[i][j])
    return imin,jmin

def complete_grille(grille):
    """compléte toutes les cases vides par [1,2,3,...,len(grille)] et renvoie la listes des coordonnées des inconnues (cases avec plussieurs possibilités)"""
    inconnues=[]      
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j]=='':
                grille[i][j]=[k for k in range(1,len(grille)+1)]
                inconnues.append((i,j))
            elif len(grille[i][j])>1: 
                inconnues.append((i,j))
    return inconnues


def mise_a_jour_grille(grille,inconnues):
    for (i,j) in inconnues:
        mise_a_jour(grille,i,j)

def mise_a_jour(grille,i,j): #permet de mettre à jour à l'état des connaissances la case (i,j) (quelles sont les valeurs 
    colonne(grille,i,j)        #encore possibles pour la case (i,j))
    ligne(grille,i,j)
    carre(grille,i,j)

def colonne(grille,i,j):#on retire les valeurs qui sont déjà attribuées dans la colonne j
    for k in range(len(grille)):
        if len(grille[k][j])==1:
            if grille[k][j][0] in grille[i][j] and (k,j)!=(i,j):
                grille[i][j].remove(grille[k][j][0])

def ligne(grille,i,j):#on retire les valeurs qui sont déjà attribuées dans la ligne i
    for k in range(len(grille)):
        if len(grille[i][k])==1:
            if grille[i][k][0] in grille[i][j] and (i,k)!=(i,j):
                grille[i][j].remove(grille[i][k][0])

def carre(grille,i,j):#on retire les valeurs qui sont déjà attribuées dans le carré contenant (i,j)
    for k in range(3*int(i//3),3*(int(i//3+1))):
        for l in range(3*int(j//3),3*(int(j//3+1))):
            if len(grille[k][l])==1:
                if grille[k][l][0] in grille[i][j] and (k,l)!=(i,j):
                    grille[i][j].remove(grille[k][l][0])

def unique_ligne(grille,inconnues,i): #fonction qui regarde s'il existe des numéros n'ayant qu'une unique place dans la ligne i
    nb_presences={1:0 ,2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}   #et complète cette place par la valeur si c'est le cas
    cases=[]
    for j in range(len(grille)):
        if len(grille[i][j])>1:
            cases.append((i,j))
            for k in grille[i][j]:
                nb_presences[k]+=1
    return(analyse_unicite(grille,inconnues,nb_presences,cases))

def unique_colonne(grille,inconnues,j):                    #fonction qui regarde s'il existe des numéros n'ayant qu'une unique place dans la colonne j
    nb_presences={1:0 ,2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0} #et complète cette place par la valeur si c'est le cas
    cases=[]
    for i in range(len(grille)):
        if len(grille[i][j])>1:
            cases.append((i,j))
            for k in grille[i][j]:
                nb_presences[k]+=1
    return(analyse_unicite(grille,inconnues,nb_presences,cases))

def unique_carre(grille,inconnues,n): #n => numéro du carré n. Carré 1: en haut à gauche, carré 2: milieu haut etc...
    cases=[] # calcule quelles cases sont dans le carré n
    nb_presences={1:0 ,2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for k in range(3*((n-1)//3),3*((n-1)//3+1)):  #fonction qui regarde s'il existe des numéros n'ayant qu'une unique place dans le carré
        for l in range(3*((n-1)%3),3*((n-1)%3+1)):
            if len(grille[k][l])>1:  #et complète cette place par la valeur si c'est le cas
                cases.append((k,l))
                for p in grille[k][l]:
                    nb_presences[p]+=1
    return(analyse_unicite(grille,inconnues,nb_presences,cases))



def analyse_unicite(grille,inconnues,nb_presences,cases):
    modification = False    #fonction qui regarde s'il existe des élémments n'apparaissant qu'une unique fois
    for k in range(1,len(nb_presences)+1): 
        if nb_presences[k]==1:
            for (i,j) in cases: 
                if k in grille[i][j]:
                    grille[i][j] = [k]          #si c'est le cas, la cases où cette valeur apparait prend automatiquement la valeur k
                    print((i,j))
                    inconnues.remove((i,j))
                    mise_a_jour_grille(grille,inconnues)
                    modification = True
    return modification

def verification_case(grille,i,j):
    pas_de_problemes=True
    if grille[i][j]==[]:
        return False
    for k in range(len(grille)): #on vérifie qu'il n'y a pas de conflits sur la colonne et la ligne
        
        if k!=j and len(grille[i][k])==1 and grille[i][j][0]==grille[i][k][0]:
            pas_de_problemes=False
        if k!=i and len(grille[k][j])==1 and grille[i][j][0]==grille[k][j][0]:
            pas_de_problemes=False
    for k in range(3*int(i//3),3*(int(i//3+1))): ##on vérifie qu'il n'y a pas de conflits dans le carré
        for l in range(3*int(j//3),3*(int(j//3+1))):
            if (k,l)!=(i,j) and len(grille[k][l])==1 and grille[i][j][0]==grille[k][l][0]:
                pas_de_problemes==False
    return(pas_de_problemes)

def verification_grille(grille,inconnues):
    grille_valide=True
    for i in range(len(grille)):
        for j in range(len(grille)):
            if verification_case(grille,i,j) == False:
                grille_valide = False
    if inconnues!=[]: print("la grille est imcomplete")
    elif grille_valide: print("La grille est valide")
    else: print("la grille est fausse")
    return(grille_valide)


def est_complete(grille):
    """renvoie True si la grille est entièrement remplie"""
    complet = True
    for i in range(len(grille)):
        for j in range(len(grille)):
            if len(grille[i][j])>1 or len(grille[i][j])==0:
                complet=False
    return(complet)

CHECKPOINT=[]

def resolve_sudoku(grille):
    global CHECKPOINT
    inconnues = complete_grille(grille)
    full = False
    while not full:
        G = grille.copy()
        mise_a_jour_grille(G,inconnues)
        full = est_complete(grille)
        if grille == G and not full:
            CHECKPOINT.append(grille.copy())
            i,j = moins_possibilites(G)
            if G[i][j]==[]:
                grille = CHECKPOINT.pop(len(CHECKPOINT)-1)
                grille[i][j]=grille[i][j][1::]
                resolve_sudoku(grille)
            REC_G = G.copy()
            REC_G[i][j] = [G[i][j][0]]
            resolve_sudoku(REC_G)
            full = est_complete(REC_G)                
        else:
            grille = G
            inconnues = complete_grille(grille)
    return verification_grille(grille, inconnues)


sudoku3=[['' ,'' ,'' ,'' ,[8],'' ,'' ,'' ,'' ],
         [[8],'' ,'' ,'' ,[9],'' ,'' ,'' ,[3]],
         ['' ,'' ,[5],[2],[7],[3],[6],'' ,'' ],
         ['' ,[4],[1],'' ,'' ,'' ,[3],[7],'' ],
         [[7],'' ,'' ,'' ,'' ,'' ,'' ,'' ,[6]],
         ['' ,[6],[2],'' ,'' ,'' ,[8],[5],'' ],
         ['' ,'' ,[9],[8],[1],[7],[2],'' ,'' ],
         [[4],'' ,'' ,'' ,[5],'' ,'' ,'' ,[7]],
         ['' ,'' ,'' ,'' ,[2],'' ,'' ,'' ,'' ]]
sys.setrecursionlimit(4000)

print(resolve_sudoku(sudoku3))
