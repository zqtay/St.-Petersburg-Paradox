import random
import matplotlib.pyplot as plt
import numpy as np

coin=['H','T']
trials=1000000
data=[]

for i in range(trials):
    rounds=0
    while random.choice(coin) == 'T':
        rounds+=1
    else:
        win= 2 ** (rounds + 1)

    if i == 0:
        data.append(win)
    else:
        data.append(win + data[i - 1])

avg=np.array(data)/np.array([i for i in range(1,trials+1)])

plt.plot([i for i in range(1,trials+1)],avg)
plt.title('St. Petersburg Simulation. Average Winnings vs. Number of Trials')
plt.xlabel(f'Number of Trials = {trials}')
plt.ylabel('Average Winnings')

