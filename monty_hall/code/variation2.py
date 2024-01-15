import random as r
from matplotlib import pyplot as plt
import numpy as np
import math
import time
from general_case import simulation


t = time.time()

n_simulations = 500

probabilities = np.zeros((3, n_simulations))
n_games = np.array([int(math.exp(i)) for i in np.linspace(1, math.log(100_000), num=n_simulations)]) # goes exponentially from 1 to 100_000

for i in range(n_simulations):
    for n_open in range(3):
        probabilities[n_open][i] = simulation(n_games[i], 5, 2, n_open)


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
print(f"Executed in {time.time() - t:.2f}s") # around 50s on my PC
plt.show()
