import matplotlib.pyplot as plt
import numpy as np

# Population Size
population_size = 2.3e5

# Sampling Parameters
sample_size = 50
number_of_samples = 500

# Generate Population of Numbers
population = 1 / np.logspace(np.log10(0.001), np.log10(10), int(population_size))

# True mean
true_mean = np.mean(population)

# Output 
print('[-----------------------------------------------]')
print('[*] Population Size: ', population_size)
print('[-----------------------------------------------]')
print('[*] Generated Population Size: ', population_size)
print('[-----------------------------------------------]')
print('[*] True Mean of Population: ', true_mean)
print('[*] Sample Size: ', sample_size)
print('[*] Number of Sample: ', number_of_samples)
print('[-----------------------------------------------]')
print

# Random Sampling

print('[*] Random Sample of 50 from Population:', np.random.choice(population, size=sample_size))
print('[*] Mean of Another Random Sample of 50: ', np.mean(np.random.choice(population, size=sample_size)))
print('[-----------------------------------------------]')