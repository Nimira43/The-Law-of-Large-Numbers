import matplotlib.pyplot as plt
import numpy as np

population_size = 2.3e5
print('Population Size: ', population_size)

# Generate Population of Numbers
population = 1 / np.logspace(np.log10(0.001), np.log10(10), int(population_size))
print('Population of Numbers: ', population)

# Plot the Inverse Values with Skipping
skip = int(1e3)
plt.plot(population[::skip], 'o')
plt.show()

