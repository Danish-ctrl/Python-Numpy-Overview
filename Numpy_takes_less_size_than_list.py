#Prove that Numpy takes less space than List

import numpy as np

import sys

s = range(1000)
print(sys.getsizeof(s) * len(s))   #In output it showed that 48000 unit of space is occupied by list in memory

d = np.arange(1000)
print(d.size * d.itemsize)         #In output it showed that 4000 unit of space is occupied by list in memory


