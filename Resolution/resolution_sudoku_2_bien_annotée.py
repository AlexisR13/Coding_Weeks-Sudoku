def moins_possibilites(grille):
    """renvoi les indices de la case de la grille où la liste des possibilités est la moins longue"""
    imin,jmin = 0,0
    lmin = len(grille)
    for i in range(len(grille)):
        for j in range(len(grille)):
            if len(grille[i][j])<lmin and len(grille[i][j])!=1 :
                 imin = i
                 jmin = j
                 lmin = len(grille[i][j])
    return imin,jmin


def resolution(grille):
    resolution_naive(grille)            
    affichage(grille)
    if est_complete(grille)==True and verification_grille(grille)==True:
        affichage(grille)
        print("La grille est valide")

    else:
        (i_min,j_min)=moins_possibilites(grille)        #choix optimisé de la case sur laquelle faire une hypothèse
        for k in grille[i_min][j_min]:
            grille[i_min][j_min] = [k]          #hypothèse sur la valeur de la case choisie précédemment
            resolution(grille)



def resolution_naive(grille): 
    """prend en argument une grille avec des éléments déjà remplis, et d'autres vides ('')"""
    complete_grille(grille)                 #permet de compléter les éléments vides de la grille (y affecte la liste [1,2,3,...,len(grille)])
    inconnues = coordonnees_inconnues(grille)           #liste des coordonnées des cases inconnues
    changement_etape_1 = reduit_nb_inconnues(grille,inconnues)       #étape 1 de la résolution : application bête et méchante des règles du sudoku

    changement_etape_2 = reduit_nb_inconnues_bis(grille,inconnues)   #étape 2 : stratégie de résolution de sudoku (un peu plus intelligent)

    while changement_etape_1==True or changement_etape_2==True:
        changement_etape_1 = reduit_nb_inconnues(grille,inconnues)          #on repète les deux étapes précédentes
        changement_etape_2 = reduit_nb_inconnues_bis(grille,inconnues)      #jusqu'à ce qu'elles ne puisse plus modifier la grille




################## fonctions utiles à la réolution naive ##################
def complete_grille(grille):
    """compléte toutes les cases vides par [1,2,3,...,len(grille)]"""
    for i in range(len(grille)):
        for j in range(len(grille)):
            if grille[i][j]=='':
                grille[i][j]=[k for k in range(1,len(grille)+1)]

def coordonnees_inconnues(grille):
    """renvoie la liste des coordonnées des inconnues (cases avec plusieurs possibilités)"""
    inconnues=[]      
    for i in range(len(grille)):
        for j in range(len(grille)):
            if len(grille[i][j])>1:
                inconnues.append((i,j))
    return inconnues

def reduit_nb_inconnues(grille,inconnues):
    """étape 1 : enleve les inconnues absurdes de chaque case (selon les règles du sudoku: un chiffre par ligne, par colonne et par carre)"""
    changement=False
    while len(inconnues)>0:
        mise_a_jour_grille(grille,inconnues)        #met à jour les inconnues de la grille en utilisant les règles du sudoku 
        nb_inaction=0
        for (i,j) in inconnues: 
            if len(grille[i][j])==1:            #lorsqu'une case ne possède plus qu'une seule possibilité, ce n'est plus une inconnue      
                inconnues.remove((i,j))
                changement=True
                break           #à chaque changement on recommence à parcourir les cases inconnues depuis le début
            else :
                nb_inaction+=1
        if nb_inaction == len(inconnues):       #la boucle while s'arrete lorsqu'il n'y a plus d'inconnue ou lorsque l'étape 1 ne peut plus en retirer
            break
    return changement           #renvoie un booléen True si la fonction a changé au moins la valeur d'une case

def reduit_nb_inconnues_bis(grille,inconnues):
    """étape 2 : affecte une valeur a une case lorsque cette valeur est présente (en tant qu'inconnue) une unique fois sur une ligne ou  une collonne ou un carré"""
    changement=False
    while len(inconnues)>0:
        nb_inaction=0
        for k in range(len(grille)):
            if unique_ligne(grille,inconnues,k)==False and unique_colonne(grille,inconnues,k)==False and unique_carre(grille,inconnues,k+1)==False:
                nb_inaction+=1
        if nb_inaction==len(grille):
            break
        else:
            changement=True
    return changement           #renvoie un booléen True si la fonction a changé au moins la valeur d'une case




########## sous-fonctions des fonctions utiles à la résolution naive ##########
###sous fonctions utiles à la focntion reduit_nb_inconnues
def mise_a_jour_grille(grille,inconnues):
    for (i,j) in inconnues:
        mise_a_jour(grille,i,j)

def mise_a_jour(grille,i,j): 
    """permet de mettre à jour à l'état des connaissances la case (i,j) (quelles sont les valeurs encore possibles pour la case (i,j))"""
    colonne(grille,i,j)        
    ligne(grille,i,j)
    carre(grille,i,j)

def colonne(grille,i,j):
    """on retire de la case (i,j) les valeurs qui sont déjà attribuées dans la colonne j"""
    for k in range(len(grille)):
        if len(grille[k][j])==1:
            if grille[k][j][0] in grille[i][j] and (k,j)!=(i,j):
                grille[i][j].remove(grille[k][j][0])

def ligne(grille,i,j):
    """on retire de la case (i,j) les valeurs qui sont déjà attribuées dans la ligne i"""
    for k in range(len(grille)):
        if len(grille[i][k])==1:
            if grille[i][k][0] in grille[i][j] and (i,k)!=(i,j):
                grille[i][j].remove(grille[i][k][0])

def carre(grille,i,j):
    """on retire de la case (i,j) les valeurs qui sont déjà attribuées dans le carré contenant (i,j)"""
    for k in range(3*int(i//3),3*(int(i//3+1))):
        for l in range(3*int(j//3),3*(int(j//3+1))):
            if len(grille[k][l])==1:
                if grille[k][l][0] in grille[i][j] and (k,l)!=(i,j):
                    grille[i][j].remove(grille[k][l][0])


###sous fonctions utiles à la focntion reduit_nb_inconnues
def unique_ligne(grille,inconnues,i): 
    """fonction qui regarde s'il existe des numéros n'ayant qu'une unique place dans la ligne i et complète cette place par la valeur si c'est le cas"""
    cases=[]        #liste des inconnues qui sont dans la ligne i
    nb_presences={1:0 ,2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}          #pour chaque chiffre, compte le nombre d'appararition dans les cases inconnues
    for j in range(len(grille)):
        if len(grille[i][j])>1:
            cases.append((i,j))
            for k in grille[i][j]:
                nb_presences[k]+=1
    return(analyse_unicite(grille,inconnues,nb_presences,cases))

def unique_colonne(grille,inconnues,j):                    
    """fonction qui regarde s'il existe des numéros n'ayant qu'une unique place dans la colonne j et complète cette place par la valeur si c'est le cas"""
    cases=[]        #liste des inconnues qui sont dans la collonne j
    nb_presences={1:0 ,2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}          #pour chaque chiffre, compte le nombre d'appararition dans les cases inconnues
    for i in range(len(grille)):
        if len(grille[i][j])>1:
            cases.append((i,j))
            for k in grille[i][j]:
                nb_presences[k]+=1
    return(analyse_unicite(grille,inconnues,nb_presences,cases))

def unique_carre(grille,inconnues,n): 
    """n => numéro du carré n. Carré 1: en haut à gauche, carré 2: milieu haut etc... 
    fonction qui regarde s'il existe des numéros n'ayant qu'une unique place dans le carré n et complète cette place par la valeur si c'est le cas"""
    cases=[]        #liste des inconnues qui sont dans le carré n
    nb_presences={1:0 ,2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}          #pour chaque chiffre, compte le nombre d'appararition dans les cases inconnues
    for k in range(3*((n-1)//3),3*((n-1)//3+1)):  
        for l in range(3*((n-1)%3),3*((n-1)%3+1)):
            if len(grille[k][l])>1:  
                cases.append((k,l))
                for p in grille[k][l]:
                    nb_presences[p]+=1
    return(analyse_unicite(grille,inconnues,nb_presences,cases))


def analyse_unicite(grille,inconnues,nb_presences,cases):
    """fonction qui regarde si des éléments n'apparaissent qu'une unique fois et affecte cette valeur à l'unique case d'apparition"""
    modification = False 
    for k in range(1,len(nb_presences)+1): 
        if nb_presences[k]==1:                  #test si k n'apparait qu'une fois
            for (i,j) in cases: 
                if k in grille[i][j]:
                    grille[i][j] = [k]          #si c'est le cas, la cases où cette valeur apparait prend la valeur k
                    inconnues.remove((i,j))
                    mise_a_jour_grille(grille,inconnues)
                    modification = True
    return modification



########## phase de vérification de la grille ##########
def verification_case(grille,i,j):
    """vérifie que la case (i,j) respecte les règles du sudoku (et renvoie un booléen True si c'est le cas, False sinon)"""
    pas_de_problemes = True
    if len(grille[i][j])!=1:
        pas_de_problemes=False
    else:
        for k in range(len(grille)):                        #on vérifie qu'il n'y a pas de conflits sur la colonne et la ligne
            if k!=j and len(grille[i][k])==1 and grille[i][j][0]==grille[i][k][0]:
                pas_de_problemes=False
            if k!=i and len(grille[k][j])==1 and grille[i][j][0]==grille[k][j][0]:
                pas_de_problemes=False
        for k in range(3*int(i//3),3*(int(i//3+1))):        #on vérifie qu'il n'y a pas de conflits dans le carré
            for l in range(3*int(j//3),3*(int(j//3+1))):
                if (k,l)!=(i,j) and len(grille[k][l])==1 and grille[i][j][0]==grille[k][l][0]:
                    pas_de_problemes==False
    return(pas_de_problemes)

def verification_grille(grille):
    """teste si la grille respecte les règles du sudoku (et renvoie un booléen True si c'est le cas, False sinon)"""
    grille_valide=True
    for i in range(len(grille)):
        for j in range(len(grille)):
            if verification_case(grille,i,j) == False:
                grille_valide = False
    return(grille_valide)


def est_complete(grille):
    """renvoie True si la grille est entièrement remplie (ie il n'y a plus d'inconnues)"""
    complet = True
    for i in range(len(grille)):
        for j in range(len(grille)):
            if len(grille[i][j])>1 and grille[i][j] != []:         
                complet=False
    return(complet)


########## affichage lisible dans le terminal ##########
def affichage(grille): 
    """permet d'afficher la grille de manière lisible pour un humain"""
    A='La solution de la grille est : \n'
    ligne='  -   -   -   -   -   -   -   -   -'
    A+=ligne
    A+='\n'
    for i in range(len(grille)):
        A+='!  '
        for j in range(len(grille)):
            if len(grille[i][j])==1:
                A+=str(grille[i][j][0])
            elif grille[i][j]==[]:
                A+='/'
            else:
                A+='0'
            if (j+1)%3==0: A+='  !  '
            else: A+='  '
        if (i+1)%3==0: A+='\n' + ligne + '\n'
        else: A+='\n'
    print(A)
    

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

sudoku4=[['' ,'' ,[7],'' ,'' ,'' ,[3],'' ,[2]],
         [[2],'' ,'' ,'' ,'' ,[5],'' ,[1],'' ],
         ['' ,'' ,'' ,[8],'' ,[1],[4],'' ,'' ],
         ['' ,[1],'' ,'' ,[9],[6],'' ,'' ,[8]],
         [[7],[6],'' ,'' ,'' ,'' ,'' ,[4],[9]],
         ['' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ,'' ],
         ['' ,'' ,'' ,[1],'' ,[3],'' ,'' ,'' ],
         [[8],'' ,[1],'' ,[6],'' ,'' ,'' ,'' ],
         ['' ,'' ,'' ,[7],'' ,'' ,'' ,[6],[3]]]

#resolution(sudoku)
#resolution(sudoku2)
resolution(sudoku3)