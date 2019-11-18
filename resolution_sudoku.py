def moins_possibilites(grille):
    #renvoi les indices de la case de la grille où la liste des possibilités est la moins longue
    imin,jmin = 0,0
    lmin = 9
    for i in range(9):
        for j in range(9):
            if len(grille[i][j])<lmin and len(grille[i][j])!=1 : imin,jmin,lmin = i,j,len(grille[i][j])
    return imin,jmin

def resolution_avec_suppositions(historique_grille):
    grille_actuelle = historique_grille[-1][0]
    index_modif = historique_grille[-1][1]
    i,j = moins_possibilites(grille_actuelle)
    if est_complete(grille_actuelle):
        return grille_actuelle
    elif grille_actuelle[i][j]==[]:
        a= historique_grille.pop()
        while len(historique_grille[-1][0][index_modif[0]][index_modif[1]])==1:
            b = historique_grille.pop()
            index_modif = historique_grille[-1][1]
        c = historique_grille[-1][0][index_modif[0]][index_modif[1]].pop()
        return resolution_avec_suppositions(historique_grille)
    else:
        index_modif = (i,j)
        grille_actuelle[i][j] = grille_actuelle[i][j][-1]
        historique_grille.append((resolution_naive(grille_actuelle),index_modif))
        return resolution_avec_suppositions(historique_grille)

        



        
    

