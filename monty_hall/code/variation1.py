import random as r
from matplotlib import pyplot as plt
import numpy as np
import math
import time


def game(n_opened: int) -> bool:
    """Simulate a Monty Hall like problem
    Return True if you win the game
    
    There is 10 doors, one of them is winning (1) and the others are losing (0)
    You chose a door, then the host open n losing doors and you can change door, do you do it ?
    Here we decide to switch doors"""

    # setting the doors
    doors = [1] + [0] * 9
    r.shuffle(doors)

    choice = r.randint(0, 9)

    # the host open the doors (opened door = -1)
    i = 0
    for _ in range(n_opened):
        while doors[i%10] != 0 or i%10 == choice:
            i += 1
        doors[i%10] = -1
        i += 1

    available_choice = []
    for i in range(10):
        if doors[i] >= 0 and i != choice:
            available_choice.append(i)
    
    # the player switch door
    new_choice = r.choice(available_choice)
    
    return doors[new_choice%10] == 1 # the choice is the winning door


def simulation(n_games, n_doors):
    """Returns the probability to win after played N times
    The games are played by opening n_doors doors"""

    n_win = 0
    for _ in range(n_games):
        if game(n_doors):
            n_win += 1
    return n_win / n_games

t = time.time()

n_simulation = 500

probabilities = np.zeros((9, n_simulation))
n_games = np.array([int(math.exp(i)) for i in np.linspace(1, math.log(100_000), num=n_simulation)]) # goes exponentially from 1 to 100_000

for i in range(n_simulation):
    for n_doors in range(9):
        probabilities[n_doors][i] = simulation(n_games[i], n_doors)


# plot the results
colors = ['#03071E', '#370617', '#6A040F', '#9D0208', '#D00000', '#DC2F02', '#E85D04', '#F48C06', '#FAA307']
    
plt.figure(figsize=(12, 6))
plt.xscale('log')
plt.ylim(0, 1)

plt.title('Simulation of a Monty Hall like problem')
plt.xlabel('Number of games tried')
plt.ylabel('Win probability')

for i in range(9):
    plt.scatter(n_games, probabilities[i], c=colors[i], alpha=0.8, label=f"{i}")

# plt.colorbar(label='Number of doors opened')
plt.legend(loc='upper left', title='Doors\nopened')
plt.savefig('result2.png')

print(f"Executed in {time.time() - t:.2f}s") # around 240s on my PC
plt.show()
