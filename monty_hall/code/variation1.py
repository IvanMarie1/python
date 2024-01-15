import random as r
from matplotlib import pyplot as plt
import numpy as np
import math
import time
from general_case import simulation



t = time.time()

n_simulation = 500

probabilities = np.zeros((9, n_simulation))
n_games = np.array([int(math.exp(i)) for i in np.linspace(1, math.log(100_000), num=n_simulation)]) # goes exponentially from 1 to 100_000

for i in range(n_simulation):
    for n_open in range(9):
        probabilities[n_open][i] = simulation(n_games[i], 10, 1, n_open)


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
