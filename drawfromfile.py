import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import csv

with open('data.txt', 'rb') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     print(type(spamreader))
     mlist = list(spamreader)
     print(mlist[0][10])
     mlist[0].pop()
     floatlist = [float(i) for i in mlist[0]]

# Data for plotting
t = np.arange(0.0, 1.0, 0.001)
s = floatlist

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
