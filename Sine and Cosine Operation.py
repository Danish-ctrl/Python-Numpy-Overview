import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, np.pi*3, 0.1)

a = np.sin(x)
b = np.cos(x)
c = np.tan(x)

plt.plot(x, a)
plt.show()

plt.plot(x, b)
plt.show()

plt.plot(x, c)
plt.show()


