import sys


def chercher_binome(n, k, niveaux) -> list:
    for i in range(n+k):
        for j in range(n+k-i-1):
            i_debut = i
            i_fin = n+k-1-j

            eleves = [niveaux[i_debut], niveaux[i_fin]]
            binome = niveaux[i_debut] + niveaux[i_fin]

            surplus = 0
            n_eleves = 2

            i_debut += 1
            i_fin -= 1

            while n_eleves < n and i_debut < i_fin:
                nv_binome = niveaux[i_debut]+niveaux[i_fin]

                if nv_binome == binome:
                    eleves.append(niveaux[i_debut])
                    eleves.append(niveaux[i_fin])
                    n_eleves += 2
                    i_debut += 1
                    i_fin -= 1
                elif nv_binome < binome:
                    i_debut += 1
                    surplus += 1
                else:
                    i_fin -= 1
                    surplus += 1

            if n_eleves == n:
                return eleves
    return []


def main():
    n, k = map(int, sys.stdin.readline().split())
    niveaux = list(map(int, sys.stdin.readline().split()))

    eleves = chercher_binome(n, k, niveaux)

    for eleve in eleves:
        print(eleve, end=" ")


main()
