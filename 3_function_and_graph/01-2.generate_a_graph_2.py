import numpy as np
import matplotlib.pyplot as plt

# Using np.linspace() to define the range of x-axis and store it in x.
x = np.linspace(1, 10, 901)

# Using np.sqrt() to calculate the square root of x-1 and store it in gx.
gx = np.sqrt(x-1)

plt.plot(x, gx)
plt.show()
