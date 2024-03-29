# Simulation of Monty Hall Problem with Python

Simulate the Monty Hall Problem by repeating the game thousands of times in order to calculate the win probability with a lot of parameters

---

## How to use it
You can download the source code in the [**code folder**](code/)

If you have already installed [NumPy](https://numpy.org/) and [Matplotlib](https://matplotlib.org/), you should run the file without problem

You can edit the file to change parameters and see how it works 

If you want to use variation1.py and variation2.py, you have to download general_case.py to import the simulation function

---

### Result of the simulation
Here we simulate the original game show with three doors : one is winning and the two other are losing. When you chose, the host open a losing door, do you switch door or not ?

We can see that switching doors after one is opened give a better chance to win the game ( the probability to win tends to 2/3 and not to 1/2 )

[monty_hall_problem.py](code/monty_hall_problem.py)

![Simulation's result of the Monty Hall problem](img/result1.png)


---

# Other parameters

Then I asked myself how the game would work if we change the rules like the number of doors, etc.


## Variation 1
Now there are 10 doors and only one of them is winning, the host can open 0 to 8 doors

[variation1.py](code/variation1.py)

### Result of the simulation
So it seems that the more you open doors, the higher is the chance to win which is very intuitive but the gap bewteen probabilities increase too


![Simulation's result of a Monty Hall problem with 10 doors](img/result2.png)

---

## Variation 2

There are 5 doors and two of them are winning, the host open 0 to 2 doors

[variation2.py](code/variation2.py)

### Result of the simulation
We can see that the win probability still increase but it is not equal to 0.5 when we open 1 door (it is ~0.533)

![Simulation's result of a Monty Hall problem with five doors](img/result3.png)

---

## General case

Now we can try to adapt the previous experiments to understand how this work with all the parameters as variables

[general_case.py](code/general_case.py)

By doing some maths, we get the winning probability equal to :
$$\frac{n_{winning}}{n_{doors}} \times \frac{n_{doors}-1}{n_{doors}-n_{open}-1}$$
(It is the probability of winning if we switch door after the opening)

![Calculation of the winning probability by using conditional probability](img/calculs.png)

### Result of the experiment
We compare the result of the simulation with the theoretical probability with different situations

It appears that the simulation result is equal to the theoretical probability, so the formula seems correct

![Comparaison of calculated probability with the simulation results](img/result4.png)

![3D Comparaison of calculated probability with the simulation results](img/result5.png)
