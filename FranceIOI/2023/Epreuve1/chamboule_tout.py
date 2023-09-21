import sys


def total(liste):
    tot = 0
    for i in liste:
        tot += i
    return tot


def nouveau_groupe(groupe, liste):
    for i in range(len(liste)):
        if groupe > liste[i]:
            liste[i+1:] = liste[i:-1]
            liste[i] = groupe
            return liste
    return liste


def main():
    nb_jouets, nb_couleurs, nb_groupes = map(int, sys.stdin.readline().split())
    jouets = list(map(int, sys.stdin.readline().split()))
    liste_groupe = [[0]*nb_groupes for _ in range(nb_couleurs)]

    groupe = 1
    for j in range(nb_jouets-1):
        couleur = jouets[j]-1
        if jouets[j] == jouets[j+1]:
            groupe += 1
        else:
            liste_groupe[couleur] = nouveau_groupe(groupe, liste_groupe[couleur])
            groupe = 1

    if jouets[-1] != jouets[-2]:
        liste_groupe[jouets[-1]-1] = nouveau_groupe(1, liste_groupe[jouets[-1]-1])

    lots_max = 0
    for lots_couleur in liste_groupe:
        n_lots = total(lots_couleur)
        if n_lots > lots_max:
            lots_max = n_lots

    print(lots_max)


main()
