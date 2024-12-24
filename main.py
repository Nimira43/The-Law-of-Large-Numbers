import matplotlib.pyplot as plt
import numpy as np

population_size = 2.3e5
print('Population Size: ', population_size)

# Sampling Parameters
sample_size = 50
number_of_samples = 500

# Generate Population of Numbers
population = 1 / np.logspace(np.log10(0.001), np.log10(10), int(population_size))

print('Random Sample of 50 from Population:', np.random.choice(population, size=sample_size))
print('Mean of Another Random Sample of 50: ', np.mean(np.random.choice(population, size=sample_size)))
