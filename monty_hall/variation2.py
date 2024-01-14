import random as r
from matplotlib import pyplot as plt
import numpy as np
import math
import time


def game(n_doors: int) -> bool:
    """
    Simulate a variation of the Monty Hall problem
    Rules : You have the choice of five doors: two of them are winning (True) and the others are losing (False).
    You pick a door, the host opens another losing door and give you the choice to switch door.

    - Returns True if you win the game, False otherwise
    - n_doors: Number of doors opened by the host
    """

    doors = [True, True, False, False, False] # two winning doors and three losing doors
    choice = r.randint(0,4) # picking a door

    choice += 1 # the choice switch to the next door
    for _ in range(n_doors):
        if doors[choice % 5] == False: # the next door is losing, the choice switch to the next one
            choice += 1
    
    return doors[choice % 5] # you picked a winning/losing door


def simulation(n_games: int, n_doors: int):
    """Returns the probability to win the game after played a certain amount of times

    - n_games: Number of games played to approximate the win probability
    - n_doors: Number of doors opened during the game"""

    n_win = 0
    for _ in range(n_games):
        if game(n_doors):
            n_win += 1
    return n_win / n_games


t = time.time()

n_simulations = 1000

probabilities = np.zeros((3, n_simulations))
n_games = np.array([int(math.exp(i)) for i in np.linspace(1, math.log(100_000), num=n_simulations)]) # goes exponentially from 1 to 100_000

for i in range(n_simulations):
    for n_doors in range(3):
        probabilities[n_doors][i] = simulation(n_games[i], n_doors)


# plot the results
colors = ['#D00000', '#E85D04', '#FAA307']
    
plt.figure(figsize=(12, 6))
plt.xscale('log')
plt.ylim(0, 1)

plt.title('Simulation of a variation of Monty Hall Problem')
plt.xlabel('Number of games tried')
plt.ylabel('Win probability')

for i in range(3):
    plt.scatter(n_games, probabilities[i], c=colors[i], alpha=0.8, label=f"{i}")

plt.legend(loc='upper left', title='Doors\nopened')

plt.savefig('result3.png')
print(f"Executed in {time.time() - t}s") # around 80s on my PC
plt.show()