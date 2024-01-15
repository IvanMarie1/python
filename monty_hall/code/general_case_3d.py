from matplotlib import pyplot as plt
import numpy as np
import random as r
import math
import time
from general_case import simulation



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
plt.axes(projection='3d')

plt.title('Simulation of a variation of Monty Hall Problem')
plt.xlabel('Theoric probability')
plt.ylabel('Number of games (log)')
plt.gca().set_zlabel('Win Probability')
plt.gca().view_init(elev=10, azim=-120, roll=0)

plt.scatter(conjecture, np.flip(np.log(n_games)), zs=probabilities, s=(np.log(n_games) ** 2), c=n_winning/n_doors, alpha=.8, cmap='plasma')

plt.colorbar(label="Proportion of winning doors")

plt.savefig('result5.png')
print(f"Executed in {time.time() - t:.2f}s") # around 120s on my PC
plt.show()
