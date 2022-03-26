import numpy as np
import matplotlib.pyplot as plt

# Set the range of x as from negative infinity to positive infinity.
x = np.linspace(-5, 5, 1001)

# Define a function of f(x) = 3x + 1
fx = 3 * x + 1

plt.plot(x, fx)
plt.grid(True)

plt.show()
