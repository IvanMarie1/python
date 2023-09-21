import sys


def chercher_inverse(n, index, liste):
    inverse = n[::-1]
    for i in range(index, len(liste)):
        coureur_inverse = liste[i]
        if coureur_inverse == inverse:
            liste[index] = ""
            liste[i] = ""
            return


def main():

    n_participants = int(sys.stdin.readline())
    participants = list(sys.stdin.readline().split())
    n_solos = n_participants

    for i in range(n_participants):
        coureur = participants[i]
        if coureur != "":
            chercher_inverse(coureur, i, participants)

    for coureur in participants:
        if coureur == "":
            n_solos -= 1

    print(n_solos)


main()
