import matplotlib.pyplot as plt
import numpy as np

# Initialise population size
population_size = 2.3e5
print('Population Size: ', population_size)

# Generate frequency value (f)
f = np.logspace(np.log10(0.001), np.log10(5), 18)
print('Frequency value (f): ', f)

inverse_f = 1 / f
print('Inverse of frequency values (1/f)', inverse_f)

plt.plot(inverse_f)
plt.show()
