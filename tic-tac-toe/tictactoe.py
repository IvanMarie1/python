def winner(tab: list) -> bool:
    """Check if there is a winning condition
    Process: check that all the characters of a line/colummn/diagonal are the same and non-default"""

    # LINES
    for iLig in range(3):
        if tab[iLig][0] == tab[iLig][1] == tab[iLig][2] and tab[iLig][0] != ".":
            return True

    # COLUMNS 
    for iCol in range(3):
        if tab[0][iCol] == tab[1][iCol] == tab[2][iCol] and tab[0][iCol] != ".":
            return True
    
    # DIAGONALS
    if tab[0][0] == tab[1][1] == tab[2][2] and tab[0][0] != ".":
        return True
    if tab[0][2] == tab[1][1] == tab[2][0] and tab[0][2] != ".":
        return True
    
    return False


def ask_pos(tab: list, player: str) -> tuple:
    """Ask for the position to play and check if the syntax is correct, else repeat
    Input syntax : "a b" with a and b between 1 and 3 included"""

    try:
        x, y = map(int, input(f"{player}'s turn: ").split())
    except ValueError:
        print("Invalid input, type the position with the syntax \"a b\" with a and bbetween 1 and 3 (included)")
        return ask_pos(tab, player)
    except KeyboardInterrupt:
        print("Goodbye :)")
        exit()

    if not(0<x<=3 or 0<y<=3):
        print("Position out of frame")
        return ask_pos(tab, player)
    
    if tab[x-1][y-1] != ".":
        print("Position already filled")
        return ask_pos(tab, player)
    
    return x, y


def display(tab: list) -> None:
    """Display the game board"""
    for iLig in range(3):
        for iCol in range(3):
            print(tab[iLig][iCol], end=" ")
        print()
    print()


def main():
    # initialize the game board
    tab = [["." for _ in range(3)] for _ in range(3)]
    play_count = 0

    # while no one win and the game board is not filled, play
    while not winner(tab) and play_count<9:
        # Alternate the player
        if play_count%2:
            player = "O"
        else:
            player = "X"

        # ask the position and actualize the game board
        x, y = ask_pos(tab, player)
        tab[x-1][y-1] = player
        
        display(tab)

        play_count += 1

    if winner(tab):
        print("The winner is", player, "!")
    else:
        print("Draw !")


if __name__ == "__main__":
    main()