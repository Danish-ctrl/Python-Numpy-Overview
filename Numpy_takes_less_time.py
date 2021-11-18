#Prove that Numpy is faster than the List
import time

import numpy as np


size = 1000000

l1 = range(size)
l2 = range(size)

n1 = np.arange(size)
n2 = np.arange(size)

start = time.time()
result = ([(x,y) for x,y in zip(l1,l2)])
print(time.time() - start)

start = time.time()
result = n1 + n2
print(time.time() - start)

