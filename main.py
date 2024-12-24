import matplotlib.pyplot as plt
import numpy as np

# Initialise population size
population_size = 2.3e5
print('Population Size: ', population_size)

# Generate frequency value (f) and handle division by zero
epsilon = 1e-10 # small value to avoid division by 0
f = np.linspace(0, 5, 18) + epsilon
print('Frequency value (f): ', f)

inverse_f = 1 / f
print('Inverse of frequency values (1/f)', inverse_f)
