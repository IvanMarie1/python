import random as r
from matplotlib import pyplot as plt
import numpy as np
import math


def game(switch=True) -> bool:
    """Simulate the Monty Hall problem :

    Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats.
    You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat.
    He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?"""

    winning_door = r.randint(0,2) # the car is behind a random door
    choice = r.randint(0,2) # choosing the first door

    if switch:
        choice += 1 # the choice switch to the next door
        if choice % 3 != winning_door: # the next door is a goat, the choice switch to the next one
            choice += 1
    
    return choice % 3 == winning_door # the choice is the winning door


def simulation(N, switch):
    """Returns the probability to win the car after played N times
    Can switch doors if needed"""

    n_win = 0
    for _ in range(N):
        if game(switch):
            n_win += 1
    return n_win / N

n_exp = 100

switch = np.zeros(n_exp)
no_switch = np.zeros(n_exp)
n_games = np.array([int(math.exp(i)) for i in np.linspace(1, math.log(100_000), num=n_exp)] )# goes exponentially from 1 to 100_000

for i in range(n_exp):
    switch[i] = simulation(n_games[i], True)
    no_switch[i] = simulation(n_games[i], False)


# plot the results
    
plt.xscale('log')
plt.ylim(0, 1)

plt.title('Simulation of Monty Hall Problem')
plt.xlabel('Number of games tried')
plt.ylabel('Win probability')

plt.scatter(n_games, switch, alpha=0.8, label='Switched door')
plt.scatter(n_games, no_switch, alpha=0.8, label='No switched door')

plt.legend()

plt.savefig('test.png')
plt.show()
