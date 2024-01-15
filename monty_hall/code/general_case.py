from matplotlib import pyplot as plt
import numpy as np
import random as r
import math
import time


def game(n_doors: int, n_winning: int, n_open: int) -> bool:
    """Simulate a variation of the Monty Hall Problem with other parameters
    - n_doors: number of doors possible during the game
    - n_winning: number of winning doors
    - n_open: number of doors opened by the host during the game
    
    For example, the standard game would be `game(3, 1, 1)`"""

    if (n_winning > n_doors) or (n_open > n_doors-n_winning-1):
        print("Wrong parameters value")
        return False

    # setting the doors
    doors = [0] * n_doors
    for i in range(n_winning):
        doors[i] = 1
    r.shuffle(doors)

    choice = r.randint(0, n_doors - 1)

    # the host open the doors (opened door = -1)
    i = 0
    for _ in range(n_open):
        while doors[i%n_doors] != 0 or i%n_doors == choice:
            i += 1
        doors[i%n_doors] = -1

    available_choice = []
    for i in range(n_doors):
        if doors[i] >= 0 and i != choice:
            available_choice.append(i)
    
    # the player switch door
    new_choice = r.choice(available_choice)
    
    return doors[new_choice%n_doors] == 1 # the player choose a winning door


def simulation(n_games: int, n_doors: int, n_winning: int, n_open: int) -> float:
    """Repeat the game to get an approximation of the win probability with certain parameters

    Return the win probability (between 0 and 1)
    
    - n_games: number of games played to approximate probability
    - n_doors: number of doors in the game
    - n_winning: number of winning doors
    - n_open: number of open doors"""

    n_win = 0
    for _ in range(n_games):
        if game(n_doors, n_winning, n_open):
            n_win += 1
    return (n_win/n_games)

def main():
    t = time.time()

    n_simulation = 500
    n_games = np.exp(np.linspace(1, math.log(100_000), num=n_simulation)).astype(int)
    probabilities = np.zeros(n_simulation)
    n_doors = np.ones(n_simulation).astype(int) 
    n_winning = np.ones(n_simulation).astype(int)
    n_open = np.ones(n_simulation).astype(int)

    for i in range(n_simulation):
        n_doors[i] = r.randint(2, 100)
        n_winning[i] = r.randint(1, n_doors[i]-1)
        n_open[i] = r.randint(0, n_doors[i] - n_winning[i] - 1) 
        probabilities[i] = simulation(n_games[i], n_doors[i], n_winning[i], n_open[i])

    conjecture = (n_winning / n_doors) * (n_doors - 1) /(n_doors - n_open - 1)


    # plotting the results
    plt.figure(figsize=(12,6))

    plt.title('Simulation of a variation of Monty Hall Problem')
    plt.xlabel('Win Probability')
    plt.ylabel('Theoric probability')

    plt.scatter(probabilities, conjecture, s=(np.log(n_games) ** 3) // 3, c=(n_winning / n_doors), alpha=.8, cmap='plasma')

    plt.colorbar(label="Proportion of winning doors")

    plt.savefig('result4.png')
    print(f"Executed in {time.time() - t:.2f}s") # around 130s on my PC
    plt.show()


if __name__ == "__main__":
    main()
