def max_list(liste_entier):
    if len(liste_entier) < 3:
        return None
    j = 0
    temp = liste_entier[0]
    indextemp = 0
    liste_resultat = []
    while j < 3:
        for i in range(0,len(liste_entier)):
            if liste_entier[i] >= temp:
                temp = liste_entier[i]
                indextemp = i
        liste_resultat.append(temp)
        del liste_entier[indextemp]
        temp = liste_entier[0]
        j += 1
    resultat1 = liste_resultat[0]
    resultat2 = liste_resultat[1]
    resultat3 = liste_resultat[2]
    return resultat3, resultat2, resultat1

def min_list(liste_entier, N):
    if N <= 0:
        return None
    if len(liste_entier) < N:
        return None
    temp = liste_entier[0]
    indextemp = 0
    liste_resultat = []
    for j in range(N):
        for i in range(0,len(liste_entier)):
            if liste_entier[i] <= temp:
                temp = liste_entier[i]
                indextemp = i
        liste_resultat.append(temp)
        del(liste_entier[indextemp])
        temp = liste_entier[0]
    return liste_resultat

def first_number(nombre):
    if nombre <=1:
        return None
    for i in range(2, nombre):
        if (nombre % i) == 0:
            return False
    return True

def list_arithm(liste_entier):
    if len(liste_entier) <= 1:
        return False
    temp = liste_entier[1] - liste_entier[0]
    for i in range(0, len(liste_entier)-1):
        if(liste_entier[i+1] - liste_entier[i] != temp):
            return False
    return True

def list_geom(liste_entier):
    if len(liste_entier) <= 1:
        return False
    temp = liste_entier[1] / liste_entier[0]
    for i in range(0, len(liste_entier)-1):
        if(liste_entier[i+1] / liste_entier[i] != temp):
            return False
    return True