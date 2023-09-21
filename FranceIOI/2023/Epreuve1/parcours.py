
def main():
    n, q = map(int, input().split())
    salles = list(map(int, input().split()))

    niveau = 1
    pos = 0
    mouv = 0

    while niveau < n+1:
        mouv += 1
        if salles[pos] == niveau:
            niveau += 1
        pos = (pos+1) % 4
    print(mouv-1)


main()
