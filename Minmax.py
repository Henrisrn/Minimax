from copy import deepcopy
def AfficheJeu(table):
    for i in table:
        print(str(i))
def partieGagne(table,gagnant):
    for j in gagnant:
        for i in range(len(table[0])):
            if table[i][0] == table[i][1] == table[i][2] and table[i][i] == j:
                print("Partie gagné colonne "+str(i))
                return j
            if table[0][i] == table[1][i] == table[2][i] and table[i][i] == j:
                print("Partie gagné Ligne "+str(i))
                return j
            if table[0][0] == table[1][1] == table[2][2] and table[0][0] == j:
                print("Partie gagné Diag1 "+str(i))
                return j
            if table[0][2] == table[1][1] == table[2][0] and table[0][0] == j:
                print("Partie gagné Diag2 "+str(i))
                return j
    for i in table:
        for j in i:
            if j == "":
                return 0
        
def Solutionpossible(zone,tour):
    possibilite = []
    for i in range(len(zone)):
        for j in range(len(zone[i])):
            a = deepcopy(zone)
            if  zone[i][j] == "":
                a[i][j] = tour
            possibilite.append(a)
    for i in possibilite:
        AfficheJeu(i)
    return possibilite

zone = [["","",""],["","",""],["","",""]]

joueur = ["X","O"]
while partieGagne(zone,joueur) != None:
    zone = Solutionpossible(zone,joueur[1])
    

"""
sol1 = Solutionpossible(zone,1)
for i in sol1 : 
    sol2 = Solutionpossible(i,2)"""
