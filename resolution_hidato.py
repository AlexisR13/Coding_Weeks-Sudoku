###Résolution hidato###

def chemins(longueur_chemin):  #on construit l'ensemble des chemins possibles de longueur 'longueur_chemin', 
    chemins_possibles=[]       #avant de réaliser un tri et de garder uniquement ceux qui sont possibles
    for i in range(8**longueur_chemin):
        chemins_possibles.append(decomposition_base_8(i,longueur_chemin))
    return chemins_possibles

def decomposition_base_8(i,longueur_chemin): #on décompose i en base 8, afin d'obtenir tous les chemins possibles
    base_8=[0 for k in range(longueur_chemin)]
    for k in range(longueur_chemin):
        base_8[-(1+k)]=i%8
        i=i//8
    return base_8

def direction(dir,case): #à chaque nombre entre 0 et 7, on associe une direction
    i,j=case             #et on renvoie la case sur laquelle on est ensuite
    if dir==0:return((i-1,j-1))
    if dir==1:return((i-1,j))
    if dir==2:return((i-1,j+1))
    if dir==3:return((i,j+1))
    if dir==4:return((i+1,j+1))
    if dir==5:return((i+1,j))
    if dir==6:return((i+1,j-1))
    if dir==7:return((i,j-1))


def chemins_coherents(grille,case1,case2):
    longueur_chemin=grille[case2[0]][case2[1]]-grille[case1[0]][case1[1]] #algorithme qui cherche à calculer quels sont
    chemin=chemins(longueur_chemin) #les chemins existants pouvant relier deux points consécutifs
    chemins_possibles=[]            #de manière cohérente (donc sans passer deux fois par un même point, ne remplir 
    for j in range(len(chemin)):    #que des cases actuellement vides située dans la grille, finissant son chemin sur la 
        liste_cases=[(case1[0],case1[1])] #case d'arrivée 'cible'...)
        for k in range(longueur_chemin):
            nouvelle_case=direction(chemin[j][k],liste_cases[-1])
            liste_cases.append(nouvelle_case)
        if compatible(liste_cases,grille,case2)==True:chemins_possibles.append(liste_cases)
    return chemins_possibles

def compatible(liste_cases,grille,case2): #vérifie que le chemin proposé 
    if liste_cases[-1]!=(case2[0],case2[1]):return False
    elif pas_de_retour(liste_cases)==False:return False
    for i in range(1,len(liste_cases)-1):
        if  liste_cases[i][0]<0 or liste_cases[i][1]<0:return False
        elif  liste_cases[i][0]>=len(grille) or liste_cases[i][1]>=len(grille[0]):return False
        elif grille[liste_cases[i][0]][liste_cases[i][1]]!='':return False
    return True


def pas_de_retour(liste_cases): #fonction qui vérifie que le chemin ne passe pas deux fois sur la même case
    for k in range(len(liste_cases)): #sinon ce chemin n'est pas possible
        for i in range(k+1,len(liste_cases)):
            if liste_cases[k]==liste_cases[i]:return False
    return True

def ensemble_chemins(grille,liste_cases_pleines):#pour tous les points consécutifs, on regarde quels chemins existent et 
    ensemble_chemins_valides=[] #peuvent relier ces points
    avance=False
    for i in range(len(liste_cases_pleines)-1):
        if grille[liste_cases_pleines[i+1][0]][liste_cases_pleines[i+1][1]]-grille[liste_cases_pleines[i][0]][liste_cases_pleines[i][1]]>1:
            ensemble_chemins_valides.append(chemins_coherents(grille,liste_cases_pleines[i],liste_cases_pleines[i+1]))
            avance=True
    if avance==False:return 'Pas avance'
    else:return ensemble_chemins_valides

def resolution(grille): #résolution de la grille de manière récursive
    liste_cases_pleines,liste_des_cases=liste_cases(grille)  #on répère quelles sont les cases sur lesquelles il faut travailler
    ensemble_chemin=ensemble_chemins(grille,liste_cases_pleines) #ainsi que l'ensemble des chemins possibles
    if len(liste_cases_pleines)!=len(liste_des_cases): #si la grille n'est pas encore entièrement résolue
        if ensemble_chemin=='Pas avance':
            if grille[liste_cases_pleines[0][0]][liste_cases_pleines[0][1]]!=1:
                presence_extremum(grille,liste_cases_pleines,liste_des_cases,1)
            elif grille[liste_cases_pleines[-1][0]][liste_cases_pleines[-1][1]]!=len(liste_des_cases):
                presence_extremum(grille,liste_cases_pleines,liste_des_cases,2)
#            pas_avance(grille,liste_cases_pleines,liste_des_cases)
        else:
            i=mini(ensemble_chemin)
            if i!='Probleme':
                for k in range(len(ensemble_chemin[i])):
                    grille_bis=recopie_grille(grille,ensemble_chemin[i][k],grille[ensemble_chemin[i][k][0][0]][ensemble_chemin[i][k][0][1]])
                    resolution(grille_bis)
    else:affichage(grille)

def presence_extremum(grille,liste_cases_pleines,liste_des_cases,k):
    if k==1:
        for (i,j) in liste_des_cases:
            if (i,j) not in liste_cases_pleines:
                grille_bis=recopie_grille(grille,[],0)
                grille_bis[i][j]=1
                resolution(grille_bis)
    else:
        for (i,j) in liste_des_cases:
            if (i,j) not in liste_cases_pleines:
                grille_bis=recopie_grille(grille,[],0)
                grille_bis[i][j]=len(liste_des_cases)
                resolution(grille_bis)
    

"""def pas_avance(grille,liste_cases_pleines,liste_des_cases):
    connus=[grille[liste_cases_pleines[i][0]][liste_cases_pleines[i][1] for i in range(len(liste_cases_pleines))]
    ecarts=[connu[0]]
    for i in range(len(connus)-1):
        ecarts.append(connu[i+1]-connu[i])
    mini=min(ecarts)
    ecart.index(mini)"""

def mini(liste): #renvoie l'indice ayant le moins de chemins possibles
    i=0
    for k in range(1,len(liste)):
        if len(liste[k])==0:return 'Probleme'
        elif len(liste[k])<len(liste[i]):
            i=k
    return i


def recopie_grille(grille,nouveau_chemin,l): #fonction qui recopie la grille en appliquant le nouveau chemin
    grille_bis=[[] for i in range(len(grille))] #en même temps
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            grille_bis[i].append(grille[i][j])
    for k in range(len(nouveau_chemin)-1):
        grille_bis[nouveau_chemin[k][0]][nouveau_chemin[k][1]]=l+k
    return grille_bis
    

def liste_cases(grille): #fonction qui renvoie la liste des cases pleines (mais ne renvoie pas leurs valeurs), ainsi que la 
    liste_cases_pleines=[] #liste des cases
    liste_des_cases=[]
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j]!='/':
                liste_des_cases.append((i,j))
                if grille[i][j]!='':liste_cases_pleines.append((i,j))
    liste_cases_pleines_triees=tri(liste_cases_pleines,grille)
    return(liste_cases_pleines_triees,liste_des_cases)

def tri(liste_cases_pleines,grille):
    valeurs=[(grille[liste_cases_pleines[k][0]][liste_cases_pleines[k][1]],liste_cases_pleines[k]) for k in range(len(liste_cases_pleines))]
    for i in range(len(valeurs)):
        for j in range(0, len(valeurs)-i-1):
            if valeurs[j][0] >valeurs[j+1][0]:
                valeurs[j], valeurs[j+1] = valeurs[j+1],valeurs[j]
    liste_cases_pleines_triees=[valeurs[k][1] for k in range(len(valeurs))]
    return liste_cases_pleines_triees


def affichage(grille): 
    """permet d'afficher la grille de manière lisible pour un humain"""
    A='La solution de la grille est : \n'
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j]=='':A+='   '
            elif grille[i][j]=='/':A+=' / '
            else:A+=str(grille[i][j])+' '
        A+= '\n'
    print(A)


hidato1=[['', 33, 35, '', '', '/', '/', '/'],
        [ '', '', 24, 22, '', '/', '/', '/'],
        [ '', '', '', 21, '', '', '/', '/'],
        [ '', 26, '', 13, 40, 11, '/', '/'],
        [ 27, '', '', '', 9 , '',  1,  '/'],
        [ '/','/','', '', 18, '',  '', '/'],
        [ '/','/','/','/','',  7,  '', ''],
        [ '/','/','/','/','/','/',  5, '']]

hidato2=[[ '', '', 77, 81, '', 45, '', 43, '', ''],
         [ 74, '', '', 79, '', 83, '', '', '', 40],
         [ 72, '', '/', 52, '','', '', '', 37, ''],
         [ '', '', 55, '', '', '', 49, 90, '', ''],
         [ 70, '', '', '', '','/', 86, '', '', 93],
         ['', 59, '', '','/' , '', '', 33, '', ''],
         ['', '', '', '', '',  1, '', '', '', ''],
         [ '', 67, '','', 14, '', 17, '/', 30, 96],
         [ '', '', '', 11, '',20, '', '', 26, ''],
         [65, '', 63, '', '', 23, '', '',  '', '']]

hidato3=[['', '', '' ,'/', 5],
         ['/','', '', '', ''],
         ['', 16, 19, '', ''],
         [14, '', '', '','/'],
         ['', '/',11, '', 9]]

hidato4=[['', 27, '/', '', 24],
         ['', 3,  '', '', ''],
         ['', '','',  21 , ''],
         ['', 5 , 12, '' , 17],
         [8, '', '', '', ''],
         ['', '', '/', '', 14]]

resolution(hidato3)