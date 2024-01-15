import random as r
from matplotlib import pyplot as plt
import numpy as np
import math
import time


def game(switch=True) -> bool:
    """Simulate the Monty Hall problem :

    Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats.
    You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
    He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?"""

    doors = [1, 0, 0] # the car is 1 and the goats are 0
    r.shuffle(doors)

    choice = r.randint(0,2) # choosing the first door

    # the host open the doors (opened door = -1)
    i = 0
    while doors[i] != 0 or i == choice:
        i += 1
    doors[i] = -1
    
    available_choice = []
    for i in range(3):
        if doors[i] >= 0 and i != choice:
            available_choice.append(i)

    if switch:
        choice = r.choice(available_choice)
    
    return doors[choice % 3] == 1 # the choice is the winning door


def simulation(N, switch):
    """Returns the probability to win the car after played N times
    Can switch doors if needed"""

    n_win = 0
    for _ in range(N):
        if game(switch):
            n_win += 1
    return n_win / N


t = time.time()

n_simulations = 1000

switch = np.zeros(n_simulations)
no_switch = np.zeros(n_simulations)
n_games = np.array([int(math.exp(i)) for i in np.linspace(1, math.log(100_000), num=n_simulations)]) # goes exponentially from 1 to 100_000

for i in range(n_simulations):
    switch[i] = simulation(n_games[i], True)
    no_switch[i] = simulation(n_games[i], False)


# plot the results
    
plt.figure(figsize=(12, 6))
plt.xscale('log')
plt.ylim(0, 1)

plt.title('Simulation of Monty Hall Problem')
plt.xlabel('Number of games tried')
plt.ylabel('Win probability')

plt.scatter(n_games, switch, c="#faa307", alpha=0.7, label='Switched door')
plt.scatter(n_games, no_switch, c="#d00000", alpha=0.7, label='No switched door')

plt.legend()

plt.savefig('result1.png')
print(f"Executed in {time.time() - t:.2f}s") # around 40s on my PC
plt.show()
